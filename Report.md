# Final Project Report

**Project URL**: TODO
**Video URL**: TODO

This project seeks to decipher the complex relationship between terrorism and refugee movements, utilizing comprehensive data from the Global Terrorism Database and UN Refugee Data. The former encompasses over 200,000 records from 1970 to 2021, cataloging terrorist incidents with detailed attributes including location, casualties, and motives. Conversely, the UN Refugee Data chronicles annual refugee figures, specifying their countries of origin and destinations for asylum.

The principal aim is to analyze the progression of terrorist activities over time and across regions and to investigate any potential correlation between the incidence of terrorism and the patterns of refugee migration. We hypothesize a direct link between regional terrorism rates and the resultant movements of refugees. Integrating these datasets allows us to conduct a thorough exploration and time-series analysis, aligning the information based on country and date.

Our deliverable includes a suite of interactive visualizations, designed to engage users and offer profound insights into the dynamics of global terrorism and refugee trends.

The dashboard comprises four interactive pages. Each page enables users to delve into the relationship between the two datasets through various interactive plots. One dedicated page for each dataset provides an overview of recent trends and general patterns in terrorist attacks and refugee flows, acquainting users with the broader context of these complex issues. The other two pages offer a deeper examination of the interconnection between these datasets.

## Introduction

The past few years have been pretty shaky when it comes to world peace. Conflicts have been flaring up in different spots around the globe, causing people to leave their homes in search of a safer place to live. Along with this movement of refugees, there are growing concerns and stereotypes. Some folks worry that refugees might bring conflicts into their new homes. Others wonder if finding safety is the real reason behind their migration. We can't claim to have the definitive answers to all those questions, but what we do have is a data science project that takes a closer look at these complex issues from a statistical point of view.

We have put together an interactive webpage with Streamlit where anyone can play around with the data we've gathered. We designed several pages, each with its own goal and way to dive into the info. It's designed for people to explore and perhaps get a fresh angle on the whole situation with terrorism and refugees.

## Related Work

## Methods

We have designed four pages in our interactive webpage. We will discuss the methods used in each of the pages below:

- Global Terrorism:

- Global Refugee:

- Combined:

- Model:

## Results

For each of the pages, we would discuss the results of each pages below:

- Global Terrorism:

- Global Refugee:

- Combined:

- Model:

## Discussion

While we don't have all the answers to the myriad questions around refugee movements and terrorism, we've created an interactive space for users to explore and draw their own insights.

In our final observations, we note a varying degree of correlation between terrorist activities and the flow of refugees to and from a country. This complexity is understandable considering the multitude of factors that influence someone to leave their home, such as natural calamities, political unrest, and yes, terrorism too—which is just one of the potential drivers we're examining.

Our analysis of the primary destinations and origins of refugees from specific countries has revealed diverse trends. Some patterns indicate that refugees tend to move away from regions with higher levels of terrorist violence, while others suggest alternative motivations, like the pursuit of better living conditions or the simplicity of geographic proximity.

## Future Work

Looking ahead, our aim is to broaden our understanding of refugee movements by integrating additional datasets that provide deeper insights into the forces driving people to seek asylum. Enhanced monitoring and potentially predicting refugee flows could significantly aid in maintaining social stability and optimizing the distribution of humanitarian aid. As for terrorism, bringing in supplementary data, like the Human Development Index, might yield a more nuanced view of how terrorism affects various facets of societal progress.

Moreover, expanding our analytical toolkit could enrich user interaction. Currently, our approach utilizes a basic ARIMA model for time-series forecasting. However, other advanced models like Prophet or LSTM offer promising alternatives for such analysis. We plan to introduce a variety of these models down the line, allowing users to compare their performance directly on our datasets.