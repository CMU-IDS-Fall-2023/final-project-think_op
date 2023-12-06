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

TODO

## Methods

We have designed four pages in our interactive webpage. We will discuss the methods used in each of the pages below:

- Global Terrorism:\
    TODO

- Global Refugee:\
    TODO

- Combined:\
  By integrating the Global Terrorism dataset with the Global Refugee dataset, based on the same countries and years, we're able to perform a comprehensive combined analysis. Initially, we filter for countries present in both datasets, addressing discrepancies such as nations that no longer exist, are not widely recognized, or are specific regions within a country. To standardize country names that might slightly vary (e.g., "US" vs. "United States of America"), we utilized the pycountry library, referring to countries by their ISO codes.

  Next, we create line charts to illustrate the count of terrorist attacks and the flow of refugees entering or leaving the country selected by the user, within their chosen time period. Alongside these visualizations, we calculate and display the correlation coefficient, providing insight into the relationship between terrorist activities and refugee movements.

  Additionally, our analysis extends to identifying the most common destinations or origins for refugees moving from or to the selected country. This aspect of the study helps ascertain if refugees tend to relocate to countries with fewer terrorist incidents, enhancing our understanding of their migration patterns.

- Model:\
    TODO

## Results

For each of the pages, we would discuss the results for each of them below:

- Global Terrorism:\
    TODO

- Global Refugee:\
    TODO

- Combined:\
  Our findings reveal that there's no one-size-fits-all answer when it comes to the relationship between terrorist attacks and refugee movements. The correlation varies significantly from country to country, and the selected time period also greatly influences the correlation coefficient. Contrary to the common belief that refugees might increase the incidence of terrorist attacks in their destination countries, our data does not universally support this claim. Indeed, while some countries show a slight positive correlation between refugee influx and terrorist attacks, many others exhibit little or even negative correlation. This suggests that other factors, such as religious demographics, age and gender composition, and socio-cultural differences between origin and destination countries, might play a crucial role in this complex dynamic.

  Additionally, our analysis indicates that in countries experiencing high levels of terrorism, refugees often seek asylum in nations with fewer terrorist incidents. Conversely, in countries where terrorist attacks are less frequent, this factor becomes less pivotal in influencing refugee destinations, pointing to other motivations behind their choice of asylum.

- Model:\
    TODO

## Discussion

While we don't have all the answers to the myriad questions around refugee movements and terrorism, we've created an interactive space for users to explore and draw their own insights.

In our final observations, we note a varying degree of correlation between terrorist activities and the flow of refugees to and from a country. This complexity is understandable considering the multitude of factors that influence someone to leave their home, such as natural calamities, political unrest, and yes, terrorism too—which is just one of the potential drivers we're examining.

Our analysis of the primary destinations and origins of refugees from specific countries has revealed diverse trends. Some patterns indicate that refugees tend to move away from regions with higher levels of terrorist violence, while others suggest alternative motivations, like the pursuit of better living conditions or the simplicity of geographic proximity.

## Future Work

Looking ahead, our aim is to broaden our understanding of refugee movements by integrating additional datasets that provide deeper insights into the forces driving people to seek asylum. Enhanced monitoring and potentially predicting refugee flows could significantly aid in maintaining social stability and optimizing the distribution of humanitarian aid. As for terrorism, bringing in supplementary data, like the Human Development Index, might yield a more nuanced view of how terrorism affects various facets of societal progress.

Moreover, expanding our analytical toolkit could enrich user interaction. Currently, our approach utilizes a basic ARIMA model for time-series forecasting. However, other advanced models like Prophet or LSTM offer promising alternatives for such analysis. We plan to introduce a variety of these models down the line, allowing users to compare their performance directly on our datasets.
