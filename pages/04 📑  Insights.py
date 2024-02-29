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

st.header("Insight 1")
st.write("Insight body text")

st.header("Insight 2")
st.write("Insight body text")

st.header("Insight 3")
st.write("Insight body text")

st.header("Insight 4")
st.write("Insight body text")

