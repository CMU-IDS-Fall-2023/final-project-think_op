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

### System Design
For the global terrorism dataset, we would have an interactive map that could be adjusted to display whichever time window, countries, and other attributes of attacks the user selected. We would also have a pie chart displaying the composition of attributes the user chose and a line graph incorporating a forecasting model to display the number of past attacks and predictions for future attack counts.
![Sketch1](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/sketch1.png) \
For the global refugee dataset, we would include a Sankey Diagram to better illustrate the flow of refugees. As for the correlation between the terrorism data and refugee data, we would include a heatmap for the refugee count and terrorist attack count to examine their relationships, as well as a simple bar chart with two bars per country that represent the two quantities.
![Sketch2](https://github.com/CMU-IDS-Fall-2023/final-project-think_op/blob/main/images/sketch2.png)
