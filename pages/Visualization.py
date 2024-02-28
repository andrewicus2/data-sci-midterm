import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import numpy as np


st.title("02 - Visualization")
dfviz = pd.read_csv("life_expectancy.csv")
st.subheader("Correlation Map")
dfHeat = dfviz.drop(['Country', 'Status', 'Year'], axis = 1)

heatmap = plt.figure(figsize=(20, 12))
sns.heatmap(dfHeat.corr(), annot=True)
st.pyplot(heatmap)

print(dfviz.columns)

st.subheader("Life Expectancy by Country (2000 - 2015)")
selected_countries = st.multiselect(label = "Select Countries", options = dfviz["Country"].unique(), default=['France', 'United States of America', 'Chad', 'Sierra Leone', 'Sudan'])

dfviz2 = dfviz[dfviz["Country"].isin(selected_countries)]
chart = alt.Chart(dfviz2).mark_line().encode(
x=alt.X('Year'),
y=alt.Y('Life expectancy '),
color=alt.Color("Country")
).properties()
st.altair_chart(chart, use_container_width=True)

st.bar_chart(data = dfviz[dfviz["Year"] == 2008], x = "Country", y = "Life expectancy " )

average_life_expectancy = dfviz.groupby("Country")["Life expectancy "].mean()
average_life_expectancy = average_life_expectancy.dropna()
average_life_expectancy = average_life_expectancy.sort_values(ascending=False)

lifehighcol, lifelowcol = st.columns(2)
lifehighcol.dataframe(average_life_expectancy.head(5))
lifelowcol.dataframe(average_life_expectancy.tail(5))

avglifefig = plt.figure(figsize=(20, 12))
sns.barplot(data = average_life_expectancy)
st.pyplot(avglifefig)

selected_aspect = st.selectbox(label = "Aspect Selector", options = dfviz.columns)

st.scatter_chart(data = dfviz, x = selected_aspect, y = "Life expectancy " )