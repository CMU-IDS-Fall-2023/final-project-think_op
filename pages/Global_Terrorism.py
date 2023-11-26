import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Placeholder title")
st.markdown("Placeholder markdown")

df = pd.read_csv('data\gtd_1970_2021.csv')

df = df.dropna(subset=['latitude', 'longitude'])

filtered_years = st.slider("Filter for years", min_value=df["iyear"].min(), max_value=df["iyear"].max(), value=(1990, 2000))

df = df[(df["iyear"] <= max(filtered_years)) & (df["iyear"] >= min(filtered_years))]

st.map(df, latitude='latitude', longitude='longitude')