import streamlit as st
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from pmdarima import auto_arima
import pickle
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Model Time")
st.markdown("We modeled the refugee's trajectory as a function of past refugee's data, number of people wounded and killed in a given year."+
            "The idea is to explore different scenarios and measure how the future of refugee's may look like given different trends in terrorism."+
            "For this purpose we combined both datasets and used a Sarimax model.")
st.markdown("Please select the number of casualties and people wounded due to terrorism attacks. Then we will proceed to fit a model and build an scenario of refugee's trajectory")
kill = st.slider('Select the number of casualties', 100, 60000, 5)
wound = st.slider('Select the number of wounds', 100, 60000, 5)



## model
# this model was created in model.ipynb
#read model
model_filename = 'data/sarimax_model.pkl'
with open(model_filename, 'rb') as file:
    result = pickle.load(file)




# Sample DataFrame
with open("data/df_model.pkl", 'rb') as file:
    df_tot= pickle.load(file)

# 4. Get Fitted Values
fitted_values = result.fittedvalues

# 5. Specify New Points for Forecasting
forecast_steps = 10
endog_col = 'Refugees under UNHCR\'s mandate'
exog_cols = ['nkill_lag1', 'nwound_lag1']
new_exog_data = pd.DataFrame({
    'nkill_lag1': [kill] * forecast_steps,
    'nwound_lag1': [wound] * forecast_steps
}, index=pd.date_range(start=df_tot.index[-1] + pd.DateOffset(years=1), periods=forecast_steps, freq='YS'))

# 6. Make a Forecast
forecast = result.get_forecast(steps=forecast_steps, exog=new_exog_data)
forecast = forecast.predicted_mean
forecast.index = new_exog_data.index
# 7. Visualize Actual, Fitted, and Forecast Values
df = df_tot[[endog_col, 'Refugees_lag1']]\
    .rename(columns={"Refugees under UNHCR\'s mandate":"Real","Refugees_lag1":"Fitted"})
st.title('Real vs Fitted Values')
st.line_chart(df)
st.title('Forecast with current scenario')
st.line_chart(pd.concat([fitted_values, forecast], axis=1, keys=['Fitted', 'Forecast']))







# Extract coefficients for exogenous variables
exog_coeffs = result.params.loc[new_exog_data.columns]

# Calculate the expected change in the forecast for each exogenous variable
expected_changes = new_exog_data.std() * exog_coeffs

# Display coefficients and expected changes in a table
table_data = pd.DataFrame({
    'Exogenous Variable': ["casualties","wounded"],
    'Coefficient': exog_coeffs.values,
   
})

# Display the table
st.subheader("Expected Changes for Unit Increment In Exogenous Variables")
st.table(table_data)










## kmeans plot
# this image was created in models.ipynb
# Create a new chart for saving as an image

image_filename = 'data/Kmeans.png'
st.title("Time Series Clustering")
st.markdown("We want to explore how the terrorism bevahves in different countries."+
            " For this purpose we agregate the number of casualties per country. We then"+
            " create k clusters using K-means. This groups indicate similar terrorism behaviour across countries."+
            "K is calculated via the silhouette method. We finally plot the results in a biplot, which resembles the original space with high accuracy."+
            "Countries are colored per region and clusters are depicted via convex hulls.")
# Display the saved image
st.image(image_filename, caption='Forecast Plot', use_column_width=True)




