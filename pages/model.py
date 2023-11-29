import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Model Time")
st.markdown("Please select the number of casualties and people wounded. Then we will proceed to fit a model and build an scenario of refugee's trajectory")
number_of_countries1 = st.slider('Select the number of countries', 5, 16, 5)
#Todo: add shapvalues. Make nicer plot. 


## model

#read
df_1 = pd.read_excel("data/gtd_1970_2020.xlsx")
df_2 = pd.read_excel("data/gtd_Jan_June_2021.xlsx")

#Concact dbs
df = pd.concat([df_1, df_2], ignore_index=True)

import pandas as pd
refugee = pd.read_csv(filepath_or_buffer='data/population.csv', delimiter= ',')


df_tot = refugee.groupby("Year")["Refugees under UNHCR's mandate"]\
    .sum().reset_index().merge(
    df.groupby("iyear")[["nkill","nwound"]].sum().reset_index(),
    how = "inner",
    left_on= "Year", 
    right_on="iyear"
)

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima

# Sample DataFrame, replace this with your actual data
# df_tot = ...

# Assuming df_tot is your DataFrame
# Convert 'iyear' to datetime and set it as the index
df_tot['iyear'] = pd.to_datetime(df_tot['iyear'], format='%Y')
df_tot.set_index('iyear', inplace=True)

# Sidebar for user input
st.sidebar.header('User Input')
forecast_steps = st.sidebar.slider('Number of Forecast Steps', 1, 20, 10)

# 1. Prepare the Data
# Create lag features
df_tot['Refugees_lag1'] = df_tot['Refugees under UNHCR\'s mandate'].shift(1)
df_tot['nkill_lag1'] = df_tot['nkill'].shift(1)
df_tot['nwound_lag1'] = df_tot['nwound'].shift(1)

# Drop missing values resulting from lag operations
df_tot.dropna(inplace=True)

# 2. Optimize Order and Seasonal Order
# Using auto_arima to find optimal order and seasonal order
model = auto_arima(df_tot['Refugees under UNHCR\'s mandate'], exogenous=df_tot[['nkill_lag1', 'nwound_lag1']],
                   start_p=1, start_q=1, max_p=3, max_q=3, m=12, seasonal=True, trace=True)

# 3. Build a Time Series Forecasting Model with SARIMAX
endog_col = 'Refugees under UNHCR\'s mandate'
exog_cols = ['nkill_lag1', 'nwound_lag1']

# Specify exogenous variables separately
exog = df_tot[exog_cols]
endog = df_tot[endog_col]

model = SARIMAX(endog, order=model.order, seasonal_order=model.seasonal_order, exog=exog)
result = model.fit()

# 4. Get Fitted Values
fitted_values = result.fittedvalues

# 5. Specify New Points for Forecasting
new_exog_data = pd.DataFrame({
    'nkill_lag1': [200] * forecast_steps,
    'nwound_lag1': [200] * forecast_steps
}, index=pd.date_range(start=df_tot.index[-1] + pd.DateOffset(years=1), periods=forecast_steps, freq='YS'))

# 6. Make a Forecast
forecast = result.get_forecast(steps=forecast_steps, exog=new_exog_data)

# 7. Visualize Actual, Fitted, and Forecast Values
st.line_chart(df_tot[[endog_col, 'Refugees_lag1', 'nkill_lag1', 'nwound_lag1']])
st.line_chart(pd.concat([fitted_values, forecast.predicted_mean], axis=1, keys=['Fitted', 'Forecast']))

