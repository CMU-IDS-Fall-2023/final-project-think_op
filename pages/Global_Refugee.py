import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Analysis of Global Refugee Datatset")
#st.markdown("Placeholder markdown")

dataset = pd.read_csv(filepath_or_buffer='./data/population.csv', delimiter= ',')


st.header('Refugees under UNHCR\'s Mandate Over Years')

st.write('The line chart below shows the change in the number of refugees under the UNHCR mandate over the years 1970-2021')

df_years = dataset.groupby('Year')['Refugees under UNHCR\'s mandate'].sum().reset_index()

start_year, end_year = st.slider('Select Year Range', min_value=int(df_years['Year'].min()), max_value=int(df_years['Year'].max()), value=(int(df_years['Year'].min()), int(df_years['Year'].max())))
selected_year_range = df_years[(df_years['Year'] >= start_year) & (df_years['Year'] <= end_year)]

fig = px.line(selected_year_range, x='Year', y='Refugees under UNHCR\'s mandate')
st.plotly_chart(fig, use_container_width=True)

st.write('')

#

number_of_countries1 = 5
number_of_countries2 = 5

st.header("Origin Country of Refugees")
st.write('The bar chart below shows the countries producing the most refugees per year')
#

col1, col2 = st.columns(2)
with col1:
    number_of_countries1 = st.slider('Select the number of countries to display', 5, 20, 5)

with col2:
    y1= st.slider('Select Year', min_value=int(df_years['Year'].min()), max_value=int(df_years['Year'].max()), value=2021)


df_refugeesfrom = dataset[dataset['Year'] == y1]
df_refugeesfrom = df_refugeesfrom.groupby('Country of origin')['Refugees under UNHCR\'s mandate'].sum().reset_index()
df_refugeesfrom = df_refugeesfrom.sort_values(by='Refugees under UNHCR\'s mandate', ascending=False)
fig1 = px.bar(df_refugeesfrom.head(number_of_countries1), x='Country of origin', y='Refugees under UNHCR\'s mandate', title=f"Top {number_of_countries1} Origin Countries of Refugees in {y1}")
st.plotly_chart(fig1, use_container_width=True)



st.header("Country of Asylum")
st.write('The bar chart below shows the countries where refugees have seeked Asylum per-year')

col1, col2 = st.columns(2)
with col1:
    number_of_countries1 = st.slider('Select the number of countries', 5, 20, 5)

with col2:
    y2 = st.slider('Select Desired Year', min_value=int(df_years['Year'].min()), max_value=int(df_years['Year'].max()), value=int(df_years['Year'].max()))


df_refugeesto= dataset[dataset['Year'] == y2]
df_refugeesto = df_refugeesto.groupby('Country of asylum')['Refugees under UNHCR\'s mandate'].sum().reset_index()
df_refugeesto = df_refugeesto.sort_values(by='Refugees under UNHCR\'s mandate', ascending=False)
fig2 = px.bar(df_refugeesto.head(number_of_countries1), x='Country of asylum', y='Refugees under UNHCR\'s mandate', title=f"Top {number_of_countries1} Countries where Refugees have seeked Asylum in {y1}")
st.plotly_chart(fig2, use_container_width=True)



st.header("Country-wise Refugee Flows - A Year-wise View")

col1, col2 = st.columns(2)


df = dataset.copy()

with col1:
    year = st.slider('Desired Year for Flow', min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=int(df['Year'].max()))
    
    

df = df[df['Year'] == year]


df = df[df['Refugees under UNHCR\'s mandate']>0]
df['Log scaled Refugees under UNHCR\'s mandate'] = np.log(df['Refugees under UNHCR\'s mandate'])

grouped_data = df.groupby(['Country of origin', 'Country of asylum'])['Refugees under UNHCR\'s mandate'].sum().reset_index()
#grouped_data = grouped_data.head(20)

all_countries = list(set(grouped_data['Country of origin']).union(set(grouped_data['Country of asylum'])))

country_index = {country: idx for idx, country in enumerate(all_countries)}

#selected_country_of_origin = st.selectbox('Select Country of Origin', all_countries)  # Replace with your country of choice


    
with col2:
    max_flows = st.slider('Max Flows', min_value=0, max_value=20, value=10)


selected_country_of_origin = st.selectbox('Select Country of Origin', all_countries, index=all_countries.index(all_countries[0] if "Afghanistan" not in all_countries else "Afghanistan"))

# Filter and sort the data for the selected country
filtered_data = grouped_data[grouped_data['Country of origin'] == selected_country_of_origin]
sorted_data = filtered_data.sort_values(by='Refugees under UNHCR\'s mandate', ascending=False).head(max_flows)

# Update the node and link information
source = [country_index[selected_country_of_origin] for _ in range(len(sorted_data))]
target = [country_index[asylum] for asylum in sorted_data['Country of asylum']]
value = sorted_data['Refugees under UNHCR\'s mandate'].tolist()

colors = px.colors.qualitative.Plotly
link_colors = [colors[i % len(colors)] for i in range(len(value))]

# Update the figure
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=all_countries
    ),
    link=dict(
        source=source,
        target=target,
        value=value,
        color=link_colors
    ))])

fig.update_layout(title_text=f"Refugee Flows from {selected_country_of_origin} in {year}", font_size=15, height = 600)

# Display the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)



