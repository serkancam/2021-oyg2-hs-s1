import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures

data =pd.read_csv("veri_setleri/polinomsal_regresyon_veriseti.csv",sep=";")
print(data.head())