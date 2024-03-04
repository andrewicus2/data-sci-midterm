import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/2/26/World_Health_Organization_Logo.svg"
st.image(url,  output_format="PNG", width=300)

st.title("📑 Insights")
df = pd.read_csv("life_expectancy.csv")
df = df.dropna()

st.markdown('''
**Insight 1:** 3.97 percent of values within our data are missing, demonstrating that the data is accurate as the null values will not significantly alter our predictions and thus will be mostly accurate. The completeness ratio is 0.96, showing that most of the data is available for us to analyze. 

**Insight 2:** We set the Feature and Target columns to exhibit 19 explanatory variables, and we can examine which specific numerical value of each variable results in the highest and lowest life expectancies. According to the columns, in 2008, the life expectancy outcome is 81.3 years of age if the person has the following values per variable: 

* A thinness of 0.6 from the ages of 10-19, a thinness of 0.5 from the ages of 5-9
* Alcohol consumption per capita of 10.24 liters
* BMI of 62.3, a resident of a country with a GDP of 35,578.7362 
* 16.1 years of schooling
* 0 reported cases of measles
* Hepatitis B immunization coverage of 92%
* Adult mortality of 7% (in their country of residency, there is a 7% chance for them to die between the ages of 15-60 per 1,000 population)
* Infant death of 2 (in their country of residency, there are 2 infant deaths per 1,000 population)
* Percentage expenditure of 5,596.5352%
* Under-five deaths of 2 (in their country of residency, there are 2 under-five deaths per 1,000 population)
* Polio immunization coverage of 97%
* Total expenditure of 8.8% (8.8% of the the total government expenditure of their country of residency goes towards health) 
* Diphtheria immunization coverage of 97%
* Their country of residency has a probability of 0.1 deaths due to HIV/AIDS per 1,000 population
* Their country of residency has a population of 4,595,416 
* Income composition of resources of 0.854 (0.854 HDI in terms of income composition of resources within their country of residency) 

→ The life expectancy outcome we predicted based on the statistics above was 79.4 years. There is a 1.9 difference between this value and the actual value of 81.3 years, which portrays the fairly accurate nature of our predicted results. 

**Analyzing immunization coverage as an explanatory variable:** When selecting the factor "Hepatitis B" in the graph "Individual Factor Impact on Lifespan," a positive correlation is depicted between life expectancy and Hepatitis B. Therefore, more people have a higher life expectancy with increased immunization coverage. Although the curve is not directly linear, a saturated cluster of points with higher life expectancy points is present as the immunization coverage percentage increases. A more striking linear curve is present when selecting the factor "Polio" in the same graph. There is a positive correlation between life expectancy and Polio immunization percentage coverage. Another striking linear curve is present when selecting the factor "Diphtheria" in the same graph. There is a positive correlation between life expectancy and Diphtheria immunization percentage coverage. The positive correlation between immunization percentage coverage and life expectancy is evidence that the explanatory variable has a driving impact on increased life expectancy. Therefore, as seen in the statistics above, this person has high immunization coverage for the mentioned infections/ diseases and, hence, the highest life expectancy outcome. 

**Analyzing schooling as an explanatory variable:** When selecting the factor "Schooling" in the graph "Individual Factor Impact on Lifespan," a strong positive correlation is depicted between schooling and life expectancy. The more extended the amount of schooling an individual has, the longer their lifespan is. As seen in the statistics above, this person has 16.1 years of schooling, approximately 4 years more than the mean of 11.9928 schooling years of the dataset. 

**Analyzing alcohol consumption as an explanatory variable:** When selecting the factor "Alcohol" in the graph "Individual Factor Impact on Lifespan," a positive correlation is present between alcohol consumption and life expectancy. This is surprising, as alcohol consumption is scientifically proven to decrease a human's lifespan. One explanation for this positive correlation could be that many developed countries, such as in Europe, have a high alcohol consumption but also have an accredited and free universal healthcare system. Our dataset shows France has the fifth highest average life expectancy (2000-2015). The article "[Alcohol consumption per capita - 2022 World Factbook Archive](https://www.cia.gov/the-world-factbook/about/archives/2022/field/alcohol-consumption-per-capita/country-comparison)" posits France as the eighth country in the world with the highest alcohol consumption per capita. This conveys that France's esteemed universal healthcare system that does not pose barriers to people of lower socioeconomic backgrounds makes a significant difference in offsetting the adverse health effects of large alcohol consumption. 

**Analyzing alcohol consumption as an explanatory variable:** When selecting the " Population " factor in the graph "Individual Factor Impact on Lifespan," a negative correlation exists between population and life expectancy. As seen in the statistics above, this person is a resident of a country with a population of 4,595,416 people, approximately 1/3rd of the mean population of 12,743,375 in the dataset.  

**Analyzing total expenditure as an explanatory variable:** When selecting the "Total Expenditure" factor in the graph "Individual Factor Impact on Lifespan," a positive correlation exists between adult mortality and life expectancy. As seen in the statistics above, this person is a resident of a country with a total expenditure of 8.8% – 8.8% of the total government expenditure goes towards health. This is approximately 2.8% more than the average total expenditure of 5.9382% in the dataset. 

**Analyzing infant deaths as an explanatory variable:** When selecting the "Infant Deaths" factor in the graph "Individual Factor Impact on Lifespan," a negative correlation exists between infant deaths and life expectancy. As seen in the statistics above, this person is a resident of a country with two infant deaths per 1,000 population. This is approximately 1/15th of the dataset's average infant deaths of 20.3039. 

**Analyzing adult mortality rate as an explanatory variable: **When selecting the "Adult Mortality" factor in the graph "Individual Factor Impact on Lifespan," a strong negative correlation exists between adult mortality and life expectancy. As seen in the statistics above, this person is a resident of a country with an adult mortality of 7% – there is a 7% chance for them to die between the ages of 15-60 per 1,000 population). This is approximately 1/23rd of the dataset's average adult mortality of 164.7964.  

**Deduction:** I chose to analyze the seven explanatory variables with the highest impact on life expectancy – negative and positive correlations. Based on the statistics above, we can deduce that this individual comes from a developed country. They have high immunization coverage for polio, diphtheria, and Hepatitis B – accessibility to these vaccinations is significantly lower in developing countries. Additionally, they did 16.1 years of schooling, so they likely obtained their bachelor's – an opportunity available for a substantially lower percentage of the population in developing countries. The individual is a resident of a country with an alcohol consumption per capita of 10.24 liters. We can assume that they are European, as the above-average alcohol consumption is likely offset by the universal healthcare system to produce the outcome of a high average life expectancy. Their country has a total government expenditure of 8.8%. Despite not being a high percentage and only 2.8% more than the mean, we can assume that their government has a large budget. Therefore, significantly more money goes into their healthcare system than governments with lower budgets. They are from a smaller country, with a population of 4,595,416 – which we can assume has also contributed to their high life expectancy. Additionally, they are a resident of a country with 2 infant deaths per 1,000 population, which is a low mortality rate. Therefore, their country likely has good sanitary conditions, access to clean water, adequate nutrition, and health interventions in play to prevent preterm delivery and have high-quality prenatal care. Furthermore, they are residents of a country with a 7% adult mortality rate. They are likely from a country with high-tech medical treatment. 

**Insight 3:** Should a country with a lower life expectancy value (&lt;65) increase its healthcare expenditure to improve its average lifespan? 

Yes. In terms of physical health/medicine, countries with high rates of vaccinations (which we can assume indicates more significant investment in healthcare) have higher life expectancies. 

More interestingly, we can determine from this dataset that there are multiple social determinants of a longer life expectancy, including education, how the country uses its resources, development status, and food security. This means that social programs that improve quality of life also have an evident effect on longevity – that is, this dataset might provide an interesting segue to the correlation between mental and physical health that might be worth exploring further to get a complete idea of factors affecting life expectancy. In terms of the initial question we can conclude that, yes, investing further in mental healthcare can improve average lifespan. 

**Insight 4:** R2 Score (square root of the mean of the squared errors): The regression page shows that the r-squared value is never 1. This means that only part of the trends in life expectancy we have observed can be explained by what we’ve labeled “independent variables” in this experiment. Some other potentially essential factors must be missing. Most notably, there is no mention of the physical qualities of the countries this data is collected from, including climate, pollution, and effects of global warming, all of which would presumably leave an impact on human life expectancy and should be taken into account to make our predictions more accurate in the future. 
''')


