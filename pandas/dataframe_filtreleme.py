import numpy as np
import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(4,3),["A","B","C","D"],["Column1","Column2","Column3"])
print(df)

print(df > -1)

booleanDf = df > 0
print(booleanDf)
print(df[booleanDf])

print(df[df["Column1"] > 0])
df["Column4"] = pd.Series(randn(4),["A","B","C","D"])
print(df)
df["Column5"] = randn(4)
print(df)
df["Column6"] = ["newValue1","newValue2","newValue3","newValue4"]
print(df)

print(df.set_index("Column6",inplace=True))
print(df)
print(df.index.names)