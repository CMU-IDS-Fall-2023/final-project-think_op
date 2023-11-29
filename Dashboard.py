import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.header("Global terrorism exploration")

st.markdown("Main dataset: Global Terrorism Database (https://www.start.umd.edu/gtd/)")

st.markdown("The Global Terrorism Database is an open-source database compiled by the National Consortium for the Study of Terrorism and Responses to terrorism (START) on terrorist attacks around the world from 1970 through June 2021. However, it does not contain data for 1993 as it was lost during transition to digital storage. We acquired the dataset by filling out the request form on the website. Overall, there are around 214,668 records of terrorist attacks and 135 columns of different features of each attack recorded in this dataset.")

st.markdown("Secondary dataset: UN Refugee Data (https://www.unhcr.org/refugee-statistics/download/?url=sH5pnE)")

st.markdown("The United Nations High Commissioner for Refugees (UNHCR) has an elaborate dataset of all recorded refugees in various countries. The dataset includes the year, country of origin, country of asylum, and number of refugees. We can extract the data for the years which we have in the GTD. It is also possible to add some other demographics information. We will assess the need for the exact features as we move ahead in the project.")

st.markdown("Research question:")

st.markdown("We have two main research pursuits in this project. First, we want to explore how the nature of terrorism changes through time and geographical location. Second, we want to investigate whether there is any correlation between the terrorist incidents and the movement of refugees. We hypothesize that regions experiencing higher rates of terrorism will also see significant refugee movements as people seek safety and stability.")

st.markdown("Please choose a dashboard using the sidebar on the left.")
