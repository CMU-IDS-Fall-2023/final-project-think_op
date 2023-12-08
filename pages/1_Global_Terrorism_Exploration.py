import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
from wordcloud import WordCloud, STOPWORDS
from scipy.stats import chi2_contingency
import plotly.express as px

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Exploration of the Global Terrorism Database")

st.write("Use the filters on the left sidebar to explore the global terrorism database. All the plots are filtered on the years. Changing the time range will reset the victim country and perpetrator terrorist group filters to 'All'. The current version of the Global Terrorism Database only has data till mid-2021.")

pre_df = pd.read_csv('data/gtd_1970_2021_selective.csv')

pre_df = pre_df.dropna(subset=['latitude', 'longitude'])

filtered_years0 = st.sidebar.slider("Filter by years for all plots", min_value=pre_df["iyear"].min(), max_value=pre_df["iyear"].max(), value=(1970, 2021))
df = pre_df[(pre_df["iyear"] <= max(filtered_years0)) & (pre_df["iyear"] >= min(filtered_years0))]

all_countries_list = sorted(list(df["country_txt"].unique()) + ['All'])

filtered_country0 = st.sidebar.selectbox("Filter by Country (where applicable)", all_countries_list,index=all_countries_list.index("All"))
country_filter = False
if filtered_country0 != 'All':
    df_c = df[(df.country_txt == filtered_country0)]
    df_c_g = df_c
    country_insert = filtered_country0
    
else:
    df_c = df
    df_c_g = df
    country_insert = "the world"
    
all_gname_list = sorted(list(df["gname"].unique()) + ['All'])

filtered_gname0 = st.sidebar.selectbox("Filter by Terrorist group (where applicable)", all_gname_list,index=all_gname_list.index("All"))

if filtered_gname0 != 'All':
    df_g = df[(df.gname == filtered_gname0)]
    df_c_g = df_c_g[(df_c_g.gname == filtered_gname0)]
    tg_insert = filtered_gname0
else:
    df_g = df
    tg_insert = "terrorists"

num_killed=df_c_g['nkill'].sum()

st.write("Time filter has been set to:", min(filtered_years0),"-",max(filtered_years0))
st.write("Country filter has been set to:", filtered_country0 )
st.write("Terrorist Group filter has been set to:", filtered_gname0 )

# DONE: Line graph for terrorist incidents over years

st.header("Overall Statistics")
st.subheader("Terrorist incidents over years (filtered on country)")

line1 = alt.Chart(df_c).mark_line().encode(
   alt.X("iyear:O",bin=False,title="Year"),
   alt.Y("count()",title="Number of Terrorist incidents"),
)
st.altair_chart(line1, use_container_width=True, theme="streamlit")

st.write(num_killed, " people were killed in ", country_insert, " by ", tg_insert," in the time frame ",min(filtered_years0),"-",max(filtered_years0),".")
st.write("There was a sharp increase in the number of terrorist incidents in the past decade.")

#DONE: Line plot with nkill
st.subheader("Fatalities over the years (filtered by country and terrorist group)")

df_perp2 = df_c_g.groupby(['iyear'])['nkill'].sum().reset_index()

line2 = alt.Chart(df_perp2).mark_line().encode(
   alt.X("iyear:O",bin=False,title="Year"),
   alt.Y("nkill",title="Number of People killed"),
)
st.altair_chart(line2, use_container_width=True, theme="streamlit")

#DONE Map with nkill
st.subheader("Geospatial mapping of Number of incidents (filtered by country and terrorist group)")

st.map(df_c_g, latitude='latitude', longitude='longitude')



st.header("Targets of Attacks")

#DONE: Bar plot for top countries with highest number of attacks 
st.subheader("Most victimised countries (filtered on number of values shown and terrorist group)")

number_of_values1 = st.number_input("Number of top victim countries (1-30):",
                            min_value=1,
                            max_value=30,
                            value=10,
                            step=1)
df_vic1= df_g.groupby(['country_txt'])['country_txt'].count().sort_values(ascending=False).head(number_of_values1)
df_vic1 = df_vic1.rename("count_c").reset_index()

bar1 = alt.Chart(df_vic1).mark_bar().encode(
   alt.X("count_c",bin=False,title="Number of terrorist attacks"),
   alt.Y("country_txt",title="Victim Country",sort=alt.EncodingSortField(field="country_txt", op="count", order='descending')),
)
st.altair_chart(bar1, use_container_width=True, theme="streamlit")


#DONE: Sunburst on number of attacks
st.subheader("Types of targets (filtered by country and terrorist group)")

df_vic = df_c.groupby(['targtype1_txt','targsubtype1_txt'])['targtype1_txt'].count().to_frame()
df_vic = df_vic.rename(columns={'targtype1_txt':'Count'}).reset_index()

fig_target = px.sunburst(
    df_vic, path = ['targtype1_txt', 'targsubtype1_txt'],
    values='Count',
)

fig_target.update_layout(
    width=750,  
    height=750 
)

st.plotly_chart(fig_target)

st.header("Perpetrators of Attacks")

#DONE: Bar plot for top perpetrator organizations with highest number of attacks 
st.subheader("Most active terrorist groups (filtered on number of values shown and country)")

number_of_values2 = st.number_input("Number of top perpetrator groups (1-30):",
                            min_value=1,
                            max_value=30,
                            value=10,
                            step=1)
df_perp1= df_c.groupby(['gname'])['gname'].count().sort_values(ascending=False).head(number_of_values1)
df_perp1 = df_perp1.rename("count_org").reset_index()

bar2 = alt.Chart(df_perp1).mark_bar().encode(
   alt.X("count_org",bin=False,title="Number of terrorist attacks"),
   alt.Y("gname",title="Perpetrator Organization",sort=alt.EncodingSortField(field="gname", op="count", order='descending')),
)
st.altair_chart(bar2, use_container_width=True, theme="streamlit")

#DONE: Word cloud
st.subheader("Word cloud on motive of attack(filtered by country and terrorist group)")


motive_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in df_c_g.motive:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    motive_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 700, height = 700,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(motive_words)
 
fig5, ax5 = plt.subplots(figsize=(7, 7), facecolor=None)
ax5.imshow(wordcloud)
ax5.axis("off")
plt.tight_layout(pad=0)

### fig_to_image function reference: ChatGPT
def fig_to_image(fig):
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return image

wordcloud_image = fig_to_image(fig5)

st.image(wordcloud_image, use_column_width=True)


st.header("Details of Attacks")

#DONE Bar plot for top types of attacks by number of casualties 
st.subheader("Types of attacks (filtered by country and terrorist group)")

df_perp3= df_c_g.groupby('attacktype1_txt')['nkill'].count().sort_values(ascending=False).head(10)
df_perp3 = df_perp3.rename("num_fatalties").reset_index()

bar3 = alt.Chart(df_perp3).mark_bar().encode(
   alt.X("num_fatalties",bin=False,title="Number of terrorist attacks"),
   alt.Y("attacktype1_txt",title="Major attack type",sort=alt.EncodingSortField(field="gname", op="count", order='descending')),
)

st.altair_chart(bar3, use_container_width=True, theme="streamlit")


#DONE: Sunburst on types of weapons
st.subheader("Types of weapons used (filtered by country and terrorist group)")

df_weap = df_c_g.groupby(['weaptype1_txt','weapsubtype1_txt'])['weaptype1_txt'].count().to_frame()
df_weap = df_weap.rename(columns={'weaptype1_txt':'Count'}).reset_index()
fig_weap = px.sunburst(
    df_weap, path = ['weaptype1_txt', 'weapsubtype1_txt'],
    values='Count',
)

fig_weap.update_layout(
    width=750,  
    height=750 
)

st.plotly_chart(fig_weap)

