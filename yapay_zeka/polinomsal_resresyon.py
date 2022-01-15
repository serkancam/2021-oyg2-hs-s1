import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
data =pd.read_csv("veri_setleri/polinomsal_regresyon_veriseti.csv",sep=";")
print(data.head())
X=data.iloc[:,[0]].values
y=data.iloc[:,[1]].values
lr=LinearRegression()
lr.fit(X,y)
y_tahmin=lr.predict(X)


pol_reg=PolynomialFeatures(degree=4)
x_pol = pol_reg.fit_transform(X)
lr2=LinearRegression()
lr2.fit(x_pol,y)
y_pol_tahmin=lr2.predict(x_pol)

plt.scatter(x=data.araba_fiyat,y=data.araba_max_hiz)
plt.plot(X,y_tahmin,color="red")
plt.plot(X,y_pol_tahmin,color="green")
plt.show()


