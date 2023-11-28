import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Analysis of Global Refugee Datatset")
#st.markdown("Placeholder markdown")

dataset = pd.read_csv(filepath_or_buffer='./data/population.csv', delimiter= ',')

### 1. Number of null values in Country of Origin, (ISO as well), Country of Asylum, Refugees under UNHCR’s mandate,
co_null  = dataset['Country of origin'].isna().sum()
iso_null = dataset['Country of origin (ISO)'].isna().sum()
ca_null = dataset['Country of asylum'].isna().sum()
ref_null  = dataset['Refugees under UNHCR\'s mandate'].isna().sum()





col1, col2, col3= st.columns(3)
df_years = dataset.groupby('Year')['Refugees under UNHCR\'s mandate'].sum().reset_index()

with col1:
    start_year, end_year = st.slider('Select Year Range', min_value=int(df_years['Year'].min()), max_value=int(df_years['Year'].max()), value=(int(df_years['Year'].min()), int(df_years['Year'].max())))
    selected_year_range = df_years[(df_years['Year'] >= start_year) & (df_years['Year'] <= end_year)]

fig = px.line(selected_year_range, x='Year', y='Refugees under UNHCR\'s mandate', title='Refugees under UNHCR\'s Mandate Over Years')
st.plotly_chart(fig)




col1, col2, col3= st.columns(3)

number_of_countries1 = 5
number_of_countries2 = 5

st.header("Origin Country of Refugees")
with col1:
    number_of_countries1 = st.slider('Select the number of countries', 5, 16, 5)

df_refugeesfrom = dataset.groupby('Country of origin')['Refugees under UNHCR\'s mandate'].sum().reset_index()
df_refugeesfrom = df_refugeesfrom.sort_values(by= 'Refugees under UNHCR\'s mandate', ascending=False)
fig1 = px.bar(df_refugeesfrom.head(number_of_countries1), x='Country of origin', y='Refugees under UNHCR\'s mandate')
st.plotly_chart(fig1)


col1, col2, col3 = st.columns(3)

st.header("Asylum Countries of Refugees")
# Add content to the first column
with col1:
    number_of_countries2 = st.slider('Countries to Display', 5, 16, 5)

df_refugeesto = dataset.groupby('Country of asylum')['Refugees under UNHCR\'s mandate'].sum().reset_index()
df_refugeesto = df_refugeesto.sort_values(by= 'Refugees under UNHCR\'s mandate', ascending=False)

fig2 = px.bar(df_refugeesto.head(number_of_countries2), x='Country of asylum', y='Refugees under UNHCR\'s mandate')
st.plotly_chart(fig2)



