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

print(df)

st.map(df, latitude='latitude', longitude='longitude')