import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(data = randn(3,3),index = ["A","B","C"],columns = ["Column1","Column2","Column3"])
print(df)

print(df["Column1"])
print(df.loc["A"])
print(df[["Column1","Column3"]])
df["Column4"] = pd.Series(randn(3),["A","B","C"])
print(df)
df["Column5"] = df["Column1"] + df["Column2"] + df["Column3"] + df["Column4"]
print(df)

df.drop("Column4", axis = 1,inplace=True)
print(df)

print(df.iloc[1])
print(df.loc["A","Column1"])
print(df.loc[["A","B"],["Column1","Column2"]])