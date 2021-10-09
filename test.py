import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data =pd.read_csv("veri_setleri/polinomsal_regresyon_veriseti.csv",sep=";")
print(data.head())
X=data.iloc[:,[0]].values
y=data.iloc[:,[1]].values
pol_reg=PolynomialFeatures(degree=4)
x_pol = pol_reg.fit_transform(X)
lr=LinearRegression()
lr.fit(x_pol,y)
y_pol_tahmin=lr.predict(x_pol)
x_t=[[800]]
x_pol_t=pol_reg.fit_transform(x_t)
tahmin=lr.predict(x_pol_t)
print(tahmin)

