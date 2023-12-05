import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(layout="wide")

st.markdown("""
    <h1 style='text-align: center; color: white;'>Combined Analysis</h1>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    .big-font {
        font-size:32px !important;
        color: yellow !important;
    }
    </style>
    
    <p class='big-font'>Correlation Analysis</p>
    """, unsafe_allow_html=True)
st.write("This platform enables users to explore the intricate relationship between the frequency of terrorist incidents and the resulting refugee flows, both from and into a selected country, over a specified time period.")
st.write("Select a country and time period to view the correlation between the frequency of attacks and the patterns of refugee flow.")
st.write("Accompanying each plot, correlation coefficients provide a statistical measure of the relationship between these two phenomena, offering insights into how terrorism may drive refugee flows or how an influx of refugees may correlate with the frequency of attacks.")

df_terror_refugee_dest = pd.read_csv("data/terror_refugee_dest.csv")
df_terror_refugee_origin = pd.read_csv("data/terror_refugee_origin.csv")
df_refugee_grouped = pd.read_csv("data/refugee_grouped.csv")
df_terror_grouped = pd.read_csv("data/terror_grouped.csv")


if 'selected_country' not in st.session_state or st.session_state.selected_country not in df_terror_refugee_dest["country"].unique():
    st.session_state.selected_country = sorted(list(df_terror_refugee_dest["country"].unique()))[0]

st.session_state.selected_country = st.selectbox("Select a country", sorted(list(df_terror_refugee_dest["country"].unique())))
# Choose a country
df_terror_refugee_origin = df_terror_refugee_origin[df_terror_refugee_origin['country'] == st.session_state.selected_country]

min_year = max(df_terror_refugee_origin["iyear"].min(), df_terror_refugee_dest["iyear"].min())
max_year = min(df_terror_refugee_origin["iyear"].max(), df_terror_refugee_dest["iyear"].max())

filtered_years = st.slider("Filter for years", min_value=min_year, max_value=max_year, value=(min_year, max_year))

df_terror_refugee_dest = df_terror_refugee_dest[(df_terror_refugee_dest["iyear"] <= max(filtered_years)) & (df_terror_refugee_dest["iyear"] >= min(filtered_years))]
df_terror_refugee_origin = df_terror_refugee_origin[(df_terror_refugee_origin["iyear"] <= max(filtered_years)) & (df_terror_refugee_origin["iyear"] >= min(filtered_years))]

# Calculate correlation coefficient
corr_origin = df_terror_refugee_origin['Attack Count'].corr(df_terror_refugee_origin['Refugee Count (origin)'])
corr_origin = round(corr_origin, 4)

origin_base = alt.Chart(df_terror_refugee_origin).encode(
    alt.X('iyear:Q', axis=alt.Axis(title='Year', format='')),
)

origin_line1 = origin_base.mark_line(color='red').encode(
    alt.Y('Attack Count:Q', axis=alt.Axis(title='Attack Count')).axis(titleColor='red')
)

origin_line2 = origin_base.mark_line(color='green').encode(
    alt.Y('Refugee Count (origin):Q', axis=alt.Axis(title='Refugee Count (origin)')).axis(titleColor='green')
)

chart1 = alt.layer(origin_line1, origin_line2).resolve_scale(
    y = 'independent'
).properties(
    title="Origin Data Correlation"
)

# Choose a country
df_terror_refugee_dest = df_terror_refugee_dest[df_terror_refugee_dest['country'] == st.session_state.selected_country]

# Calculate correlation coefficient
corr_dest = df_terror_refugee_dest['Attack Count'].corr(df_terror_refugee_dest['Refugee Count (destination)'])
corr_dest = round(corr_dest, 4)

dest_base = alt.Chart(df_terror_refugee_dest).encode(
    alt.X('iyear:Q', axis=alt.Axis(title='Year', format='')),
)

dest_line1 = dest_base.mark_line(color='red').encode(
    alt.Y('Attack Count:Q', axis=alt.Axis(title='Attack Count')).axis(titleColor='red')
)

dest_line2 = dest_base.mark_line(color='cyan').encode(
    alt.Y('Refugee Count (destination):Q', axis=alt.Axis(title='Refugee Count (destination)')).axis(titleColor='cyan')
)

chart2 = alt.layer(dest_line1, dest_line2).resolve_scale(
    y = 'independent'
).properties(
    title="Destination Data Correlation"
)

country_selected = st.session_state.selected_country

# Origin
col1, col2 = st.columns([3, 1])
with col1:
    st.subheader(f"Terrorist attacks and refugees fleeing from {country_selected}")
    st.altair_chart(chart1, use_container_width=True)
with col2:
    delta_text_origin = ""
    if corr_origin >= 0.7:
        delta_text_origin = "Highly correlated"
    elif corr_origin >= 0.5:
        delta_text_origin = "Moderately correlated"
    else:
        delta_text_origin = "Weakly correlated"
    
    if corr_origin < 0:
        delta_text_origin = "-" + delta_text_origin
    else:
        delta_text_origin = "+" + delta_text_origin

    st.metric(label="Correlation Coefficient", value=corr_origin, delta=delta_text_origin)

# Destination
col3, col4 = st.columns([3, 1])
with col3:
    st.subheader(f"Terrorist attacks and refugees coming to {country_selected}")
    st.altair_chart(chart2, use_container_width=True)
with col4:
    delta_text_dest = ""
    if corr_dest >= 0.7:
        delta_text_dest = "Highly correlated"
    elif corr_dest >= 0.5:
        delta_text_dest = "Moderately correlated"
    else:
        delta_text_dest = "Weakly correlated"
    
    if corr_dest < 0:
        delta_text_dest = "-" + delta_text_dest
    else:
        delta_text_dest = "+" + delta_text_dest

    st.metric(label="Correlation Coefficient", value=corr_dest, delta=delta_text_dest)

# ---------------------------------------------------------------------------------------------------------------------------------

st.markdown("""
    <style>
    .big-font {
        font-size:32px !important;
        color: yellow !important;
    }
    </style>
    
    <p class='big-font'>Refugees Flows</p>
    """, unsafe_allow_html=True)

df_refugee_grouped_origin = df_refugee_grouped[df_refugee_grouped['Country of origin'] == st.session_state.selected_country]
df_refugee_grouped_origin = df_refugee_grouped_origin[(df_refugee_grouped_origin["Year"] <= max(filtered_years)) & (df_refugee_grouped_origin["Year"] >= min(filtered_years))]

# Get the most popular destination for refugees
df_refugee_grouped_origin = df_refugee_grouped_origin.groupby(["Country of asylum"]).sum().sort_values(by=["Refugees under UNHCR's mandate"], ascending=False).reset_index()
most_popular_dest = df_refugee_grouped_origin.iloc[0]["Country of asylum"]

# Calculate the average attackas per year of that country in that time period
df_terror_grouped_dest = df_terror_grouped[df_terror_grouped['country'] == most_popular_dest]
df_terror_grouped_dest = df_terror_grouped_dest[(df_terror_grouped_dest["iyear"] <= max(filtered_years)) & (df_terror_grouped_dest["iyear"] >= min(filtered_years))]
avg_attacks_dest = df_terror_grouped_dest["count"].mean()
avg_attacks_dest = int(avg_attacks_dest)

# Calculate the average attackas per year of that country in that time period
df_terror_grouped_origin = df_terror_grouped[df_terror_grouped['country'] == st.session_state.selected_country]
df_terror_grouped_origin = df_terror_grouped_origin[(df_terror_grouped_origin["iyear"] <= max(filtered_years)) & (df_terror_grouped_origin["iyear"] >= min(filtered_years))]
avg_attacks_origin = df_terror_grouped_origin["count"].mean()
avg_attacks_origin = int(avg_attacks_origin)

st.markdown("""
    <style>
    .highlight {
        font-size:22px !important;
        color: green !important;
    }
    </style>
    
    Refugees fleeing from <span class='highlight'>""" + country_selected + """</span>""" + """ are most likely to flee to <span class='highlight'>""" + most_popular_dest + """</span> in search of asylum"""
    , unsafe_allow_html=True)

year_range_str = str(min(filtered_years)) + " - " + str(max(filtered_years))

st.markdown("""
    <style>
    .highlight {
        font-size:22px !important;
        color: green !important;
    }
    .number {
        font-size:22px !important;
        color: red !important;
    }
    </style>
    
    Compared to <span class='highlight'>""" + country_selected + """</span> that has <span class='number'>""" + str(avg_attacks_origin) + """</span> attacks per year on average during <span class='number'>""" + year_range_str + """</span>, <span class='highlight'>""" + most_popular_dest + """</span> has <span class='number'>""" + str(avg_attacks_dest) + """</span> attacks per year on average during the same time period"""
    , unsafe_allow_html=True)

df_refugee_grouped_dest = df_refugee_grouped[df_refugee_grouped['Country of asylum'] == st.session_state.selected_country]
df_refugee_grouped_dest = df_refugee_grouped_dest[(df_refugee_grouped_dest["Year"] <= max(filtered_years)) & (df_refugee_grouped_dest["Year"] >= min(filtered_years))]

# Get the most popular destination for refugees
df_refugee_grouped_dest = df_refugee_grouped_dest.groupby(["Country of origin"]).sum().sort_values(by=["Refugees under UNHCR's mandate"], ascending=False).reset_index()
most_popular_origin = df_refugee_grouped_dest.iloc[0]["Country of origin"]

avg_attacks_dest = avg_attacks_origin

# Calculate the average attackas per year of that country in that time period
df_terror_grouped_origin = df_terror_grouped[df_terror_grouped['country'] == most_popular_origin]
df_terror_grouped_origin = df_terror_grouped_origin[(df_terror_grouped_origin["iyear"] <= max(filtered_years)) & (df_terror_grouped_origin["iyear"] >= min(filtered_years))]
avg_attacks_origin = df_terror_grouped_origin["count"].mean()
avg_attacks_origin = int(avg_attacks_origin)

st.markdown("""
    <style>
    .highlight {
        font-size:22px !important;
        color: green !important;
    }
    </style>
    
    Refugees fleeing to <span class='highlight'>""" + country_selected + """</span>""" + """ in search of asylum are most likely from <span class='highlight'>""" + most_popular_origin + """</span>"""
    , unsafe_allow_html=True)

year_range_str = str(min(filtered_years)) + " - " + str(max(filtered_years))

st.markdown("""
    <style>
    .highlight {
        font-size:22px !important;
        color: green !important;
    }
    .number {
        font-size:22px !important;
        color: red !important;
    }
    </style>
    
    Compared to <span class='highlight'>""" + country_selected + """</span> that has <span class='number'>""" + str(avg_attacks_dest) + """</span> attacks per year on average during <span class='number'>""" + year_range_str + """</span>, <span class='highlight'>""" + most_popular_origin + """</span> has <span class='number'>""" + str(avg_attacks_origin) + """</span> attacks per year on average during the same time period"""
    , unsafe_allow_html=True)