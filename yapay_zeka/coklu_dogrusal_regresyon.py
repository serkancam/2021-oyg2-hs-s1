
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = pd.read_csv("veri_setleri/coklu_dogrusal_regresyon_veriseti.csv",sep=";")
print(data.head())
X=data.iloc[:,[0,2]].values
y=data.iloc[:,[1]].values#data["maas"].values.reshape(-1,1)
print(y)

cdm=LinearRegression()
cdm.fit(X,y)

a=cdm.coef_
b=cdm.intercept_
print(f"a={a}\nb={b}")

kisiler=[[5,15],[5,14],[4,13],[15,39]]
maaslar=cdm.predict(kisiler)
print(maaslar)
