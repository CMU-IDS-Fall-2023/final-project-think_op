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
st.markdown("Overall Statistics")

df = pd.read_csv('data\gtd_1970_2021_selective.csv')

df = df.dropna(subset=['latitude', 'longitude'])

filtered_years1 = st.slider("Filter for years", min_value=df["iyear"].min(), max_value=df["iyear"].max(), value=(1990, 2000))

df_fil1 = df[(df["iyear"] <= max(filtered_years1)) & (df["iyear"] >= min(filtered_years1))]

st.map(df, latitude='latitude', longitude='longitude')

# Barplot over years

col1, col2 = st.columns(2)

with col1:
    filtered_years2 = st.slider("Second filter for years", min_value=df["iyear"].min(), max_value=df["iyear"].max(), value=(1970, 2021))

with col2:
    filtered_country2 = st.selectbox("Filter by Country", df["country_txt"].unique())


df_fil2 = df[(df["iyear"] <= max(filtered_years2)) & (df["iyear"] >= min(filtered_years2))]
df_fil2 = df_fil2[(df_fil2.country_txt == filtered_country2)]

hist = alt.Chart(df_fil2).mark_bar().encode(
    alt.X("iyear:O",bin=False,title="Year"),
    alt.Y("count()",title="Number of Terrorist incidents"),
).properties(title="Terrorist incidents over years for specific countries").configure_title(anchor='start')

st.altair_chart(hist, use_container_width=True, theme="streamlit")

st.markdown("Targets of Attacks")

st.markdown("Perpetrators of Attacks")

st.markdown("Details of Attacks")

st.markdown("Casualties")
