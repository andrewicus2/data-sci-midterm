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

st.header("Correlation Map")

dfHeat = dfviz.drop(['Country', 'Status', 'Year'], axis = 1)

heatmap = plt.figure(figsize=(20, 12))
sns.heatmap(dfHeat.corr(), annot=True)
st.pyplot(heatmap)

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

selected_aspect = st.selectbox(label = "Factor Selector", options = dfviz.columns.drop(["Life Expectancy", "Country", "Year", "Status"]))

st.scatter_chart(data = dfviz, x = selected_aspect, y = "Life Expectancy")