import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

df = pd.read_csv('Life Expectancy Data.csv')

df = df.dropna()

X = df.drop(['Country', 'Status', 'Life expectancy '], axis = 1)
y = df['Life expectancy ']

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

pred = lr.predict(X_test)

from sklearn import metrics

print("MAE: ", metrics.mean_absolute_error(y_test, pred))
print("MSE: ", metrics.mean_squared_error(y_test, pred))

from sklearn.metrics import r2_score

print(r2_score(y_test,pred,multioutput='variance_weighted'))