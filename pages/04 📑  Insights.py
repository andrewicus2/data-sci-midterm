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

st.subheader("Insight 1:")
st.markdown('''
3.97 percent of values within our data are missing, demonstrating that the data is accurate as the null values will not significantly alter our predictions and thus will be mostly accurate. The completeness ratio is 0.96, showing that most of the data is available for us to analyze. 
''')
st.subheader("Insight 2:")
st.markdown('''Based on the analysis of the data values that result in the lifespan of 81.3 years, which was the highest predicted life expectancy from one of our trial runs, we can determine several factors that can improve one’s longevity. First, they tend to have high immunization coverage for polio, diphtheria, and Hepatitis B. Additionally, they have 16.1 years of schooling, so they likely obtained a Bachelor’s degree. Their country spends 8.8% of their GDP on healthcare. This is only 2.8% more than the total expenditure mean of the dataset, so we can hypothesize that their government has an overall above-average budget. Therefore, they have the ability to spend more on their healthcare system in comparison to countries with lower budgets. This person also has an above-average rate of alcohol consumption and continues to maintain a high life expectancy, showing that their potentially unhealthy habits are offset by a well-functioning healthcare system. Their country has a population of 4,595,416, which indicates that it is a smaller country with a small population – which we can assume has also contributed to their high life expectancy. Additionally, they are a resident of a country with 2 infant deaths per 1,000 population, which is a low mortality rate. Therefore, their country likely has good sanitary conditions, access to clean water, adequate nutrition, and health interventions in play to prevent preterm delivery and have high-quality prenatal care. Furthermore, they are residents of a country with a 7% adult mortality rate. All these factors indicate that the country is developed, which, we can conclude, is ultimately the most important factor for a high life expectancy.  
''')
st.subheader("Insight 3:")
st.markdown('''R2 Score (square root of the mean of the squared errors): The regression page shows that the r-squared value is never 1. This means that only part of the trends in life expectancy we have observed can be explained by what we’ve labeled “independent variables” in this experiment. Some other potentially essential factors must be missing. Most notably, there is no mention of the physical qualities of the countries this data is collected from, including climate, pollution, and effects of global warming, all of which would presumably leave an impact on human life expectancy and should be taken into account to make our predictions more accurate in the future.
''')
st.subheader("Insight 4:")
st.markdown('''
We can determine from this dataset that there are multiple social determinants of a longer life expectancy, including education, how the country uses its resources, development status, and food security. This means that social programs that improve quality of life also have an evident effect on longevity – that is, this dataset might provide an interesting segue to the correlation between mental and physical health that might be worth exploring further to get a complete idea of factors affecting life expectancy. 
''')


