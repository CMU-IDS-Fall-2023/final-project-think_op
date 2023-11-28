import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pycountry

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Placeholder title")
st.markdown("Placeholder markdown")

df_terror_refugee_dest = pd.read_csv("data/terror_refugee_dest.csv")
df_terror_refugee_origin = pd.read_csv("data/terror_refugee_origin.csv")


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
# Plot the attack count and refugee population by year with altair
# Use two y-axis and show legend

origin_base = alt.Chart(df_terror_refugee_origin).encode(
    alt.X('iyear:Q', axis=alt.Axis(title='Year')),
)

origin_line1 = origin_base.mark_line(color='red').encode(
    alt.Y('Attack Count:Q', axis=alt.Axis(title='Attack Count')).axis(titleColor='red')
)

origin_line2 = origin_base.mark_line(color='green').encode(
    alt.Y('Refugee Count (origin):Q', axis=alt.Axis(title='Refugee Count (origin)')).axis(titleColor='green')
)

chart1 = alt.layer(origin_line1, origin_line2).resolve_scale(
    y = 'independent'
)

# Choose a country
df_terror_refugee_dest = df_terror_refugee_dest[df_terror_refugee_dest['country'] == st.session_state.selected_country]

dest_base = alt.Chart(df_terror_refugee_dest).encode(
    alt.X('iyear:Q', axis=alt.Axis(title='Year')),
)

dest_line1 = dest_base.mark_line(color='red').encode(
    alt.Y('Attack Count:Q', axis=alt.Axis(title='Attack Count')).axis(titleColor='red')
)

dest_line2 = dest_base.mark_line(color='yellow').encode(
    alt.Y('Refugee Count (destination):Q', axis=alt.Axis(title='Refugee Count (destination)')).axis(titleColor='yellow')
)

chart2 = alt.layer(dest_line1, dest_line2).resolve_scale(
    y = 'independent'
)

col1, col2 = st.columns(2)

with col1:
    st.altair_chart(chart1, use_container_width=True)

with col2:
    st.altair_chart(chart2, use_container_width=True)