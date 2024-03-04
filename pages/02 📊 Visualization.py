import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import numpy as np
from PIL import Image

url = "https://upload.wikimedia.org/wikipedia/commons/2/26/World_Health_Organization_Logo.svg"
st.image(url,  output_format="PNG", width=300)

st.title("📊 Visualization")
dfviz = pd.read_csv("life_expectancy.csv")
dfviz = dfviz.dropna(subset=['Life Expectancy'])

st.header("Life Expectancy by Country (2000 - 2015)")
selected_countries = st.multiselect(label = "Select Countries", options = dfviz["Country"].unique(), default=['France', 'United States of America', 'Chad', 'Sierra Leone', 'Sudan'])

dfviz2 = dfviz[dfviz["Country"].isin(selected_countries)]

country_line_chart = alt.Chart(dfviz2).mark_line().encode(
    x=alt.X('Year'),
    y=alt.Y('Life Expectancy'),
    color=alt.Color("Country")
).properties()
st.altair_chart(country_line_chart, use_container_width = True)

st.header("Average Life Expectancy (2000 - 2015)")
average_life_expectancy = dfviz.groupby(["Country"])["Life Expectancy"].mean()
average_life_expectancy = average_life_expectancy.sort_values(ascending=False)
average_life_expectancy = average_life_expectancy.reset_index()

lifehighcol, lifelowcol = st.columns(2)
lifehighcol.subheader("Top 5 Countries")
lifehighcol.dataframe(average_life_expectancy.head(5), use_container_width = True, hide_index = True)
lifelowcol.subheader("Lowest 5 Countries")
lifelowcol.dataframe(average_life_expectancy.tail(5), use_container_width = True, hide_index = True)

# japan_life_expectancy = dfviz[dfviz["Country"] == "Japan"]
# japan_life_expectancy = japan_life_expectancy.drop(labels = ["Status", "Country", "Year"], axis = 1)
# st.bar_chart(japan_life_expectancy.mean())



st.header("Correlation Map")

dfHeat = dfviz.drop(['Country', 'Status', 'Year'], axis = 1)

heatmap = plt.figure(figsize=(20, 12))
sns.heatmap(dfHeat.corr(), annot=True)
st.pyplot(heatmap)
st.subheader("Individual Factor Impact on Lifespan")

selected_aspect = st.selectbox(label = "Factor Selector", options = dfviz.columns.drop(["Life Expectancy", "Country", "Year", "Status"]))

if selected_aspect == "Adult Mortality":
    st.text("Adult Mortality Rates of both sexes (probability of dying between 15 and 60 years per 1000 population)")
elif selected_aspect == "Infant Deaths":
    st.text("Number of Infant Deaths per 1000 population")
elif selected_aspect == "Alcohol Consumption":
    st.text("Alcohol, recorded per capita (15+) consumption (in litres of pure alcohol)")
elif selected_aspect == "Percentage Expenditure":
    st.text("Expenditure on Health as a Percentage of GDP (%)")
elif selected_aspect == "Hepatitis B":
    st.text("Hepatitis B (HepB) immunization coverage among 1-year-olds (%)")
elif selected_aspect == "Measles":
    st.text("Number of reported cases per 1000 population")
elif selected_aspect == "BMI":
    st.text("Average Body Mass Index of entire population")
elif selected_aspect == "Under-five Deaths":
    st.text("Number of under-five deaths per 1000 population")
elif selected_aspect == "Polio":
    st.text("Polio (Pol3) immunization coverage among 1-year-olds (%)")
elif selected_aspect == "Total Expenditure":
    st.text("General government expenditure on health as a percentage of total government expenditure (%)")
elif selected_aspect == "Diphtheria":
    st.text("Diphtheria tetanus toxoid and pertussis (DTP3) immunization coverage among 1-year-olds (%)")
elif selected_aspect == "HIV/AIDS":
    st.text("Deaths per 1,000 live births HIV/AIDS (0-4 years)")
elif selected_aspect =="GDP":
    st.text("Gross Domestic Product per capita (in USD)")
elif selected_aspect == "Population":
    st.text("Population of the country")
elif selected_aspect =="Thinness 10-19 Years":
    st.text("Prevalence of thinness among children and adolescents for Age 10 to 19 (%)")
elif selected_aspect == "Thinness 5-9 Years":
    st.text("Prevalence of thinness among children for Age 5 to 9 (%)")
elif selected_aspect == "Income composition of resources":
    st.text("Human Development Index in terms of income composition of resources (index ranging from 0 to 1)")
elif selected_aspect == "Schooling":
    st.text("Number of years of Schooling (years)")

st.scatter_chart(data = dfviz, x = selected_aspect, y = "Life Expectancy")