import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")
x = df.drop(df.columns[[0, 3, 4, 5, 8, 9, 19, 21, 22]], axis=1)
y = df.iloc[:, 10].values

# Encoding categorical data
# from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# labelencoder_x = LabelEncoder()
# x[:, 7] = labelencoder_x.fit_transform(x[:, 7])
# onehotencoder = OneHotEncoder(categorical_features=[7])
# x = onehotencoder.fit_transform(x).toarray(x)