# Final Project Proposal

**GitHub Repo URL**: (https://github.com/CMU-IDS-Fall-2023/final-project-think_op)

Main dataset: Global Terrorism Database (https://www.start.umd.edu/gtd/)

The Global Terrorism Database is an open-source database compiled by the National Consortium for the Study of Terrorism and Responses to terrorism (START) on terrorist attacks around the world from 1970 through June 2021. However, it does not contain data for 1993 as it was lost during transition to digital storage. We acquired the dataset by filling out the request form on the website. Overall, there are around 214,668 records of terrorist attacks and 135 columns of different features of each attack recorded in this dataset.

Secondary dataset: UN Refugee Data (https://www.unhcr.org/refugee-statistics/download/?url=sH5pnE)

The United Nations High Commissioner for Refugees (UNHCR) has an elaborate dataset of all recorded refugees in various countries. The dataset includes the year, country of origin, country of asylum, and number of refugees. We can extract the data for the years which we have in the GTD. It is also possible to add some other demographics information. We will assess the need for the exact features as we move ahead in the project.

Research question:

We have two main research pursuits in this project. First, we want to explore how the nature of terrorism changes through time and geographical location. Second, we want to investigate whether there is any correlation between the terrorist incidents and the movement of refugees. We hypothesize that regions experiencing higher rates of terrorism will also see significant refugee movements as people seek safety and stability.

Here are some steps we plan to perform:

Data Integration and Exploration: We will integrate the two datasets by aligning them on common keys such as country and date. To uncover patterns and correlations, we will do exploratory data analysis, time-series analysis for trend identification, descriptive modeling and possibly predictive modeling to forecast future trends.

Clustering: To find similarities between different regions, we plan to use clustering algorithms to categorize locations based on the frequency, types of terrorist attacks, the magnitude of refugee movements, or some other features.

Visualizations: The application will provide dynamic visualizations such as heatmaps of terrorist activity, line graphs of refugee trends, and geographical maps with overlays showing terrorism and refugee data simultaneously. Users will be able to interact with these visualizations to gain a deeper understanding of the data.

## Sketches and Data Analysis
### Data Processing and Exploration
The datasets are pretty clean, so we just had to perform minimal data cleaning. That meant handling exceptions and missing values. Most of the exceptions had to do with country names and the missing values were because there was no data. 
We are mainly interested in observing the possible interactions between refugee movement and terrorism. For this matter we analyzed how these two occurrences have fluctuated and how variables such as location, people killed, time, motives, types and many others are distributed in the dataset.

Let's explore the datasets.

#### Overall Statistics

![Total_incidents](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/total_incidents.png)

The above plot shows that the number of terrorist incidents has increased tremendously in the last decade.

![Total_refugees](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/RF_total.png)

The number of refugees under UN mandate also shows an upward trend.

#### Targets of Attacks

![Target_countries](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/vic_countries.png)

The highest number of terrorist attacks occured in Iraq, Afghanistan, Pakistan, India, and Colombia. However, we need to remember that this data is only till mid-2021. All the attacks that occured after that are not reflected in the plot. It will also be interesting to explore the "INT_LOG" variable which captures whether the nationality of the Perpetrator group and the location of attack were different. It will shows the pattern of cross-border terrorism. We can also classify organizations based on whether they are only involved in insurgency.

The following Sunburst plot shows the types of targets that were hit by the terrorists. We prominently see Private citizens and properties, military, police, governments, and businesses.

![Target_type](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/targettype_sunburst.png)

#### Perpetrators of Attacks

The following bar plot shows the terrorist organizations that committed the most number of terrorist acts. However, for around 93000+ attacks, the responsible party was "Unknown". There are also additional fields such as whether the organizations officially claimed responsibility, etc. but they have not been factored into this graph. How the activity of the different groups has changed over time and their sphere of influence has to be studied by plotting their attacks separately against year and with geospatial mapping respectively. According to the plot, the highest ranking terrorist organizations are Taliban (Afghanistan), ISIL (also known as ISIS), Shining Path (officially the Communist Party of Peru), Al-Shabaab (a Somalian militant group affiliated to Al-Qaeda), etc.  

![Perpetrator_org](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/perpetrators.png)

The Motive field in the GTD is a text field. A simple way to examine it was to plot a word cloud (below).

![Motive](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/motive_wc.png)

#### Details of Attacks

The following plot shows the number of deaths caused by different attack types. We see three attack types on Y-axis becuase we have been provided with three attacktype fields as each incident can involve multiple types of attacks.

![Attack_type](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/attack_type.png)

The weapons that were used shows some variety (check the sunburst plot below), but mostly explosives and firearms were used by these terrorists to create terror and bloodshed. 

![Weapon_type](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/weapon_type_sunburst.png)

#### Casualties

This map shows the number of casualties for each geographical region. The bubbles in the Middle East are so big that they obscure some other parts of Asia and Africa. 

![Casualty_Map](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/nkill_map.png)

#### Refugee Flow


Most of the refugees were uprooted from Afghanistan probably due to the situation with Taliban. The second country where we see poeple migrating from is Syria (due to the civil war).

![Refugee_Country_of_origin](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/Rf_co.png)

The highest number of refugees went to Pakistan. These were probably majorly from Afghanistan as Pakistan borders Afghanistan. However, this dataset is only till 2021. Currently in November 2023, Pakistan is evacuating all Afghan/Pashtun people (legal and illegal) back to Afghanistan. Due to this geopolitical development, the following plot will not look the same after 2023. The second highest asylum giving country is Iran, however, we do not know from this plot where they came from. That information can be obtained from the Sankey diagram that follows. This Sankey diagram is only a fraction of the complete pairs of Origin and Asylum countries. We should also keep in mind that this plot of total number of migrations does not reflect the effect of refugee movement by itself because the original size and population of the origin and asylum country also has to be taken into consideration.

![Refugee_Country_of_asylum](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/Rf_ca.png)

![Refugee_flow](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/RF_flow.png)


### System Design
For the global terrorism dataset, we would have an interactive map that could be adjusted to display whichever time window, countries, and other attributes of attacks the user selected. For selected columns that have  cardinalities fit for a pie chart representation, we would use a pie chart to present the composition of the selected column/feature. Additionally, we would have a line graph incorporating a forecasting model to display the number of past attacks and predictions for future attack counts.
![Sketch1](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/sketch1.png) \
For the global refugee dataset, we would include a Sankey Diagram to better illustrate the flow of refugees. As for the correlation between the terrorism data and refugee data, we would include a heatmap for the refugee count and terrorist attack count to examine their relationships, as well as a simple bar chart with two bars per country that represent the two quantities.
![Sketch2](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/sketch2.png)

The features that we are using for visualizations for GTD are from:["eventid","iyear","imonth","iday","approxdate","country","country_txt","region","region_txt","provstate","city","latitude","longitude","vicinity","location","success","suicide","attacktype1","attacktype1_txt","attacktype2","attacktype2_txt","attacktype3","attacktype3_txt","targtype1","targtype1_txt","targsubtype1","targsubtype1_txt","corp1","target1","natlty1","natlty1_txt","gname","gsubname","motive","weaptype1","weaptype1_txt","weapsubtype1","weapsubtype1_txt","weapdetail","nkill","nwound","propvalue"]. The features we are using from the Refugee dataset for exploration are from: ["Year","Country of origin","Country of origin (ISO)","Country of asylum","Country of asylum (ISO)","Refugees under UNHCR's mandate"]. For the time series analysis of GTD, we are using "nkill", "nwound" and "Refugees under UNHCR's mandate".