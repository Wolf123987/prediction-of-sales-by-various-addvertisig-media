# -*- coding: utf-8 -*-
"""prediction of sales by different addvertising media .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PuvQftlYOuVZ0fDAxWFt4MYm52qIicRT
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from google.colab import files
uploaded= files.upload()

df1=pd.read_csv("advertising.csv",encoding= "latin1")

man=df1

man.describe()

man.head(20)

man.isnull().sum()

import plotly.express as px
import plotly.graph_objects as go
figure = px.scatter(data_frame = man, x="Sales",
                    y="TV", size="TV", trendline="ols")
figure.show()

figure = px.scatter(data_frame = man, x="Sales",
                    y="Newspaper", size="Newspaper", trendline="ols")
figure.show()

figure = px.scatter(data_frame = man, x="Sales",
                    y="Radio", size="Radio", trendline="ols")
figure.show()

TV = man["TV"].sum()
Radio =man["Radio"].sum()
Newspaper = man["Newspaper"].sum()


labels = ['TV','Radio','Newspaper']
values = [TV , Radio, Newspaper]

fig = px.pie(man, values=values, names=labels, 
             title='sales  From Various addverising media ', hole=0.5)
fig.show()

correlation = man.corr()
print(correlation["Sales"].sort_values(ascending=False))

x = np.array(man.drop(["Sales"], 1))
y = np.array(man["Sales"])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, 
                                                test_size=0.2, 
                                                random_state=42)

model = LinearRegression()
model.fit(xtrain, ytrain)
print(model.score(xtest, ytest))

features = np.array([[230.1, 37.8, 69.2]]) ## here the features are taken as [TV,Radio,News paper]
print(model.predict(features))