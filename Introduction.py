import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/2/26/World_Health_Organization_Logo.svg"
st.image(url,  output_format="PNG", width=300)

df = pd.read_csv("life_expectancy.csv")

st.title("Life Expectancy Data Analysis")
st.subheader("Statistical Analysis on factors influencing Life Expectancy")
st.markdown("##### Objectives")
st.markdown("We aim to predict life expectancy based on immunization factors, mortality factors, economic factors, social factors and other health related factors.")

st.markdown("Although there have been lot of studies undertaken in the past on factors affecting life expectancy, it was found that the effect of immunization and the human development index were not taken into account.")


headcol1, headcol2 = st.columns(2)
num = headcol1.number_input('No. of Rows', 5, 10)

head = headcol2.radio('View from top (head) or bottom (tail)', ('Head', 'Tail'), horizontal = True)
if head == 'Head':
    st.dataframe(df.head(num))
else:
    st.dataframe(df.tail(num))

st.text('(Rows,Columns)')
st.write(df.shape)

st.markdown("##### The data-set aims to answer the following key questions:")
st.markdown("- Do the various predicting factors which have been chosen affect life expectancy? What are the predicting variables actually affecting")
st.markdown("- Should a country with a lower life expectancy value (<65) increase its healthcare expenditure in order to improve its average lifespan?")
st.markdown("- How do Infant and Adult mortality rates affect life expectancy?")
st.markdown("- Does life expectancy have a positive or negative correlation with eating habits, lifestyle, exercise, smoking, drinking alcohol etc.?")
st.markdown("- What is the impact of schooling on the lifespan of humans?")
st.markdown("- Does life expectancy have positive or negative relationship with drinking alcohol?")
st.markdown("- Do densely populated countries tend to have lower life expectancies?")
st.markdown("- What is the impact of immunization coverage on life expectancy?")

st.markdown("##### Fields:")
st.markdown("- **Country** - Name of country")
st.markdown("- **Year** - Year")
st.markdown("- **Development Status** - Developed or Developing status")
st.markdown("- **Life Expectancy** - Life Expectancy in age")
st.markdown("- **Adult Mortality** - Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)")
st.markdown("- **Infant Deaths** - Number of Infant Deaths per 1000 population")
st.markdown("- **Alcohol Consumption** - Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)")
st.markdown("- **Percentage Expenditure** - Expenditure on Health as a Percentage of GDP (%)")
st.markdown("- **Hepatitis B** - Hepatitis B (HepB) immunization coverage among 1-year-olds (%)")
st.markdown("- **Measles** - number of reported cases per 1000 population")
st.markdown("- **BMI** - Average Body Mass Index of entire population")
st.markdown("- **Under 5 Deaths** - Number of under-five deaths per 1000 population")
st.markdown("- **Polio** - Polio (Pol3) immunization coverage among 1-year-olds (%)")
st.markdown("- **Total Expenditure** - General government expenditure on health as a percentage of total government expenditure (%)")
st.markdown("- **Diphtheria** - Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)")
st.markdown("- **HIV/AIDS** - Deaths per 1,000 live births HIV/AIDS (0-4 years)")
st.markdown("- **GDP** - Gross Domestic Product per capita (in USD)")
st.markdown("- **Population** - Population of the country")
st.markdown("- **Thinness 10-19 Years** - Prevalence of thinness among children and adolescents for Age 10 to 19 (%)")
st.markdown("- **Thinness 5-9 Years** - Prevalence of thinness among children for Age 5 to 9 (%)")
st.markdown("- **Income composition of resources** - Human Development Index in terms of income composition of resources (index ranging from 0 to 1)")
st.markdown("- **Schooling** - Number of years of Schooling (years)")

st.markdown("### Description of Data")
st.markdown("Descriptions for all quantitative data **(rank and streams)** by:")
st.dataframe(df.describe())


st.markdown("### Missing Values")
st.markdown("Null or NaN values.")

dfnull = df.isnull().sum()/len(df)*100
totalmiss = dfnull.sum().round(2)
totalmiss = round(totalmiss/len(df.columns),2)
st.write("Percentage of total missing values: ",totalmiss)
st.write(dfnull)
if totalmiss <= 30:
    st.success("We have less then 30 percent of missing values, which is good. This provides us with more accurate data as the null values will not significantly affect the outcomes of our conclusions. And no bias will steer towards misleading results. ")
else:
    st.warning("Poor data quality due to greater than 30 percent of missing value.")
    st.markdown(" > Theoretically, 25 to 30 percent is the maximum missing values are allowed, there's no hard and fast rule to decide this threshold. It can vary from problem to problem.")

st.markdown("### Completeness")
st.markdown(" The ratio of non-missing values to total records in dataset and how comprehensive the data is.")

st.write("Total data length:", len(df))
nonmissing = (df.notnull().sum().round(2))
completeness= round(sum(nonmissing)/df.size,2)
st.write("Completeness ratio:",completeness)
st.write(nonmissing)
if completeness >= 0.80:
    st.success("We have completeness ratio greater than 0.85, which is good. It shows that the vast majority of the data is available for us to use and analyze. ")
else:
    st.success("Poor data quality due to low completeness ratio( less than 0.85).")
