import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# image = Image.open('image.jpg')
# st.image(image, width=600)

st.title("Life Expectancy (WHO)")
st.header("Statistical Analysis on factors influencing Life Expectancy")
df = pd.read_csv("life_expectancy.csv")

st.sidebar.header("Dashboard")
st.sidebar.markdown("---")
app_mode = st.sidebar.selectbox('Select Page',['Introduction', 'Visualization'])

if app_mode == "Introduction":
    st.markdown("##### Objectives")
    st.markdown("We aim to predict life expectancy based on immunization factors, mortality factors, economic factors, social factors and other health related factors.")

    st.markdown("Although there have been lot of studies undertaken in the past on factors affecting life expectancy, it was found that the effect of immunization and the human development index were not taken into account.")


    num = st.number_input('No. of Rows', 5, 10)

    head = st.radio('View from top (head) or bottom (tail)', ('Head', 'Tail'))
    if head == 'Head':
        st.dataframe(df.head(num))
    else:
        st.dataframe(df.tail(num))

    st.text('(Rows,Columns)')
    st.write(df.shape)

    st.markdown("##### The data-set aims to answer the following key questions:")
    st.markdown("- Does various predicting factors which has been chosen initially really affect the Life expectancy? What are the predicting variables actually affecting the life expectancy?")
    st.markdown("- Should a country having a lower life expectancy value(<65) increase its healthcare expenditure in order to improve its average lifespan?")
    st.markdown("- How does Infant and Adult mortality rates affect life expectancy?")
    st.markdown("- Does Life Expectancy has positive or negative correlation with eating habits, lifestyle, exercise, smoking, drinking alcohol etc. ?")
    st.markdown("- What is the impact of schooling on the lifespan of humans?")
    st.markdown("- Does Life Expectancy have positive or negative relationship with drinking alcohol?")
    st.markdown("- Do densely populated countries tend to have lower life expectancy?")
    st.markdown("- What is the impact of Immunization coverage on life Expectancy?")

    st.markdown("##### Variables:")
    st.markdown("- Country")
    st.markdown("- Development Status")
    st.markdown("- Adult Mortality Rate (per 1000 population)")
    st.markdown("- Number of Infant Deaths (per 1000 population)")
    st.markdown("- Alcohol Consumption Per Capita")
    st.markdown("- Expenditure on Health as a Percentage of GDP")
    st.markdown("- Hepatitis B Immunization Coverage Among 1-year-olds")
    st.markdown("- Reported Cases of Measles (per 1000 population)")

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
    completeness= round(sum(nonmissing)/len(df),2)

    st.write("Completeness ratio:",completeness)
    st.write(nonmissing)
    if completeness >= 0.80:
        st.success("We have completeness ratio greater than 0.85, which is good. It shows that the vast majority of the data is available for us to use and analyze. ")
    else:
        st.success("Poor data quality due to low completeness ratio( less than 0.85).")







elif app_mode == "Visualization":
    dfviz = df.dropna()
    st.markdown("##### Visualization")
    dfHeat = df.drop(['Country', 'Status', 'Year'], axis = 1)
    
    plt.figure(figsize=(20, 12))
    sns.heatmap(dfHeat.corr(), annot=True)
    st.pyplot()

    selected_country = st.selectbox(label = "hi", options = dfviz["Country"])

    st.line_chart(data = dfviz[dfviz["Country"] == selected_country], x = "Year", y = "Life expectancy " )



