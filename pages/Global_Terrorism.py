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

st.title("Analysis of the Global Terrorism Database")
st.header("Overall Statistics")

pre_df = pd.read_csv('data/gtd_1970_2021_selective.csv')

pre_df = pre_df.dropna(subset=['latitude', 'longitude'])

filtered_years1 = st.slider("Filter on years for all plots", min_value=pre_df["iyear"].min(), max_value=pre_df["iyear"].max(), value=(1970, 2021))

df = pre_df[(pre_df["iyear"] <= max(filtered_years1)) & (pre_df["iyear"] >= min(filtered_years1))]

#st.map(pre_df, latitude='latitude', longitude='longitude')

# DONE: Line graph for terrorist incidents over years (Filter for years and country)

all_countries_list = sorted(list(df["country_txt"].unique()) + ['All'])

filtered_country2 = st.selectbox("Filter by Country", all_countries_list,index=all_countries_list.index("All"))


#df_fil2 = df[(df["iyear"] <= max(filtered_years1)) & (df["iyear"] >= min(filtered_years1))]
# count2_1 = df_fil2.groupby('iyear').country_txt.count().reset_index()
#count2_2 = df_fil2.groupby('iyear').country_txt.nunique().reset_index()
# count2_2.rename(columns={'country_txt': 'ncountries'}, inplace=True)
# df_fil2_2 = pd.merge(count2_1, count2_2, on = ["iyear","iyear"])
# df_fil2_2['mean_per_year'] = df_fil2_2.country_txt/df_fil2_2.ncountries
#st.table(count2_2)
if filtered_country2 != 'All':
    df_fil2 = df[(df.country_txt == filtered_country2)]
else:
    df_fil2=df

line1 = alt.Chart(df_fil2).mark_line().encode(
   alt.X("iyear:O",bin=False,title="Year"),
   alt.Y("count()",title="Number of Terrorist incidents"),
).properties(title="Terrorist incidents over years for specific countries").configure_title(anchor='start')

st.altair_chart(line1, use_container_width=True, theme="streamlit")

st.header("Targets of Attacks")

#DONE: Bar plot for top countries with highest number of attacks (Filter on number and year range)
number_of_values1 = st.number_input("Number of top victim countries (1-30):",
                            min_value=1,
                            max_value=30,
                            value=10,
                            step=1)
df_vic1= df.groupby(['country_txt'])['country_txt'].count().sort_values(ascending=False).head(number_of_values1)
df_vic1 = df_vic1.rename("count_c").reset_index()

bar1 = alt.Chart(df_vic1).mark_bar().encode(
   alt.X("count_c",bin=False,title="Number of terrorist attacks"),
   alt.Y("country_txt",title="Victim Country",sort=alt.EncodingSortField(field="country_txt", op="count", order='descending')),
).properties(title="Terrorist incidents over years for specific countries").configure_title(anchor='start')

st.altair_chart(bar1, use_container_width=True, theme="streamlit")


#DONE: Sunburst on number of attacks

filtered_country4 = st.selectbox("Filter on Country", all_countries_list,index=all_countries_list.index("All"))

if filtered_country4 != 'All':
    df_vic = df[(df.country_txt == filtered_country4)]
else:
    df_vic=df
df_vic = df_vic.groupby(['targtype1_txt','targsubtype1_txt'])['targtype1_txt'].count().to_frame()
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

#DONE: Bar plot for top perpetrator organizations with highest number of attacks (Filter on number and year range)

number_of_values2 = st.number_input("Number of top perpetrator organizations (1-30):",
                            min_value=1,
                            max_value=30,
                            value=10,
                            step=1)
df_perp1= df.groupby(['gname'])['gname'].count().sort_values(ascending=False).head(number_of_values1)
df_perp1 = df_perp1.rename("count_org").reset_index()

bar2 = alt.Chart(df_perp1).mark_bar().encode(
   alt.X("count_org",bin=False,title="Number of terrorist attacks"),
   alt.Y("gname",title="Perpetrator Organization",sort=alt.EncodingSortField(field="gname", op="count", order='descending')),
).properties(title="Terrorist incidents over years by specific organizations").configure_title(anchor='start')

st.altair_chart(bar2, use_container_width=True, theme="streamlit")

#DONE: Line plot with nkill filtered by gname
all_gname_list = sorted(list(df["gname"].unique()) + ['All'])

filtered_gname1 = st.selectbox("Filter by Terrorist organization", all_gname_list,index=all_gname_list.index("All"))

if filtered_gname1 != 'All':
    df_perp2 = df[(df.gname == filtered_gname1)]
else:
    df_perp2=df

df_perp2 = df_perp2.groupby(['iyear'])['nkill'].sum().reset_index()

#st.table(df_perp2)
line2 = alt.Chart(df_perp2).mark_line().encode(
   alt.X("iyear:O",bin=False,title="Year"),
   alt.Y("nkill",title="Number of People killed"),
).properties(title="Fatalities over the years").configure_title(anchor='start')

st.altair_chart(line2, use_container_width=True, theme="streamlit")

#DONE: Word cloud
motive_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in df.motive:
     
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

#DONE Bar plot for top types of attacks by number of casualties (Filter on number and year range)

df_perp3= df.groupby('attacktype1_txt')['nkill'].count().sort_values(ascending=False).head(10)
df_perp3 = df_perp3.rename("num_fatalties").reset_index()

bar3 = alt.Chart(df_perp3).mark_bar().encode(
   alt.X("num_fatalties",bin=False,title="Number of terrorist attacks"),
   alt.Y("attacktype1_txt",title="Major attack type",sort=alt.EncodingSortField(field="gname", op="count", order='descending')),
).properties(title="Terrorist incidents over years by specific organizations").configure_title(anchor='start')

st.altair_chart(bar3, use_container_width=True, theme="streamlit")


#DONE: Sunburst on types of weapons

df_weap = df.groupby(['weaptype1_txt','weapsubtype1_txt'])['weaptype1_txt'].count().to_frame()
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

st.header("Geospatial mapping of Casualties")

#DONE Map with nkill (Filter on year)
filtered_gname2 = st.selectbox("Filter for Terrorist organization", all_gname_list,index=all_gname_list.index("All"))

if filtered_gname2 != 'All':
    df_map = df[(df.gname == filtered_gname2)]
else:
    df_map=df
    
filtered_countries5 = st.selectbox("Filter for Victim Country", all_countries_list,index=all_countries_list.index("All"))

if filtered_countries5 != 'All':
    df_map = df_map[(df_map.country_txt == filtered_countries5)]

st.map(df_map, latitude='latitude', longitude='longitude',size='nkill'*10)