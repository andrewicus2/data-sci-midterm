import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time

st.title("Life Expectancy Data Analysis - 03 Prediction Page")
df = pd.read_csv("life_expectancy.csv")
df = df.dropna()

prediction_type = st.sidebar.selectbox('Select Type of Prediction', ['Linear Regression'])

list_variables = df.columns
select_variable = st.sidebar.selectbox('Select Variable to Predict', ['Life expectancy '])
train_size = st.sidebar.number_input("Train Set Size", min_value=0.00, step=0.01, max_value=1.00, value=0.70)
new_df = df.drop(labels= ['Life expectancy ', 'Country', 'Status'], axis=1)
list_var = new_df.columns

output_multi = st.multiselect("Select Explanatory Variables", list_var, default=[' thinness  1-19 years', ' thinness 5-9 years', 'Alcohol', ' BMI ', 'GDP', 'Schooling', 'Measles ', 'Hepatitis B'])

new_df2 = new_df[output_multi]
x = new_df2
y = df['Life expectancy ']

# scaler = StandardScaler()
# scaler.fit(df.drop('Life expectancy ', axis=1))
# scaled_features = scaler.transform(df.drop('Life expectancy ', axis=1))

# df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
x = df[output_multi]
y = df['Life expectancy ']

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
    col1.write(x.head(25))
    col2.subheader("Target Column top 25")
    col2.write(y.head(25))

    st.subheader('Results')
    # Note: You may want to adjust or remove this part since Linear Regression
    # predictions are continuous and may not directly apply to classification metrics.
    from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
    mae = mean_absolute_error(y_test, lr_pred)
    mse = mean_squared_error(y_test, lr_pred)
    r2 = r2_score(y_test, lr_pred)

    pred_df = pd.DataFrame(lr_pred, columns=["Age"])

    print(pred_df)

    y_test = y_test.reset_index()
    realcol, predcol, calcol = st.columns(3)
    realcol.subheader("Actual")
    realcol.write(y_test["Life expectancy "].head(25))
    predcol.subheader("Predicted")
    predcol.write(pred_df.head(25))
    calcol.subheader("Difference")
    difference = y_test["Life expectancy "] - pred_df.squeeze()
    calcol.write(difference.head(25))

    st.write(f"Mean Absolute Error:", mae)
    st.write(f"Mean Squared Error:", mse)
    st.write(f"R2 Score: ",r2)

    feature_names = [f'Feature_{i}' for i in list(x.columns)]

    df_X = pd.DataFrame(x, columns = feature_names)

    coefficients = lr_model.coef_

    importance = np.abs(coefficients)

    correlation_fig = plt.figure(figsize = (10,8))
    plt.barh(feature_names, importance)
    st.pyplot(correlation_fig)