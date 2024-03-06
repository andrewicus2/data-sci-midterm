import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time

url = "https://upload.wikimedia.org/wikipedia/commons/2/26/World_Health_Organization_Logo.svg"
st.image(url, output_format = "PNG", width = 300)

st.title("🤖 Linear Regression")
df = pd.read_csv("life_expectancy.csv")
df = df.dropna()
df["Status"] = df["Status"].replace({"Developing": 0, "Developed": 1})


prediction_type = st.sidebar.selectbox('Select Type of Prediction', ['Linear Regression'])

list_variables = df.columns
select_variable = st.sidebar.selectbox('Select Variable to Predict', ['Life Expectancy'])
train_size = st.sidebar.number_input("Train Set Size", min_value=0.00, step=0.01, max_value=1.00, value=0.70)
new_df = df.drop(labels= ['Life Expectancy','Country'], axis=1)
list_var = new_df.drop(labels = ['Year'], axis = 1).columns

output_multi = st.multiselect(label = "Select Explanatory Variables", options = list_var, default=['Thinness 10-19 Years', 'Thinness 5-9 Years', 'Alcohol', 'BMI', 'GDP', 'Schooling', 'Measles', 'Hepatitis B'])

new_df2 = new_df[output_multi]
x = new_df2
y = df['Life Expectancy']

# scaler = StandardScaler()
# scaler.fit(df.drop('Life Expectancy', axis=1))
# scaled_features = scaler.transform(df.drop('Life Expectancy', axis=1))

# df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
x = df[output_multi]
y = df['Life Expectancy']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=train_size)

if prediction_type == 'Linear Regression':

    lr_start_time = time.time()
    lr_model = LinearRegression()

    lr_model.fit(x_train, y_train)
    lr_pred = lr_model.predict(x_test)
    lr_end_time = time.time()
    lr_execution_time = lr_end_time - lr_start_time

    st.write("Execution time:", lr_execution_time, "seconds")

    col1, col2 = st.columns(2)
    col1.subheader("Feature Columns top 25")
    col1.write(x_test.head(25))
    col2.subheader("Target Column top 25")
    col2.write(y_test.head(25))

    st.subheader('Results')
    # Note: You may want to adjust or remove this part since Linear Regression
    # predictions are continuous and may not directly apply to classification metrics.
    from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    mae = mean_absolute_error(y_test, lr_pred)
    mse = mean_squared_error(y_test, lr_pred)
    r2 = r2_score(y_test, lr_pred)

    pred_df = pd.DataFrame(lr_pred, columns=["Predicted Value"])

    y_test = y_test.reset_index()

    results_dfs = pd.concat([y_test['Life Expectancy'], pred_df['Predicted Value']], axis = 1)
    results_dfs.insert(2, "Difference", y_test["Life Expectancy"] - pred_df.squeeze(), True)

    st.dataframe(results_dfs.head(25), hide_index = True, use_container_width = True)

    maeCol, mseCol, rCol = st.columns(3)
    maeCol.metric(f"Mean Absolute Error:", round(mae, 2))
    mseCol.metric(f"Mean Squared Error:", round(mse, 2))
    rCol.metric(f"R2 Score: ", round(r2, 4))

    feature_names = [f'Feature_{i}' for i in list(x.columns)]

    df_X = pd.DataFrame(x, columns = feature_names)

    coefficients = lr_model.coef_

    importance = np.abs(coefficients)

    correlation_fig = plt.figure(figsize = (10,8))
    plt.barh(feature_names, importance)
    st.pyplot(correlation_fig)

    st.subheader('Prediction Engine')
    inputs = {}
    for col in x.columns:
        inputs[col] = st.number_input(f"Enter value for {col}")

    # Make predictions
    input_data = pd.DataFrame([inputs])

    if(st.button("Run Prediction", type = "primary")):
        prediction = lr_model.predict(input_data)
        st.metric(f"Predicted Life Expectancy:", prediction[0])
