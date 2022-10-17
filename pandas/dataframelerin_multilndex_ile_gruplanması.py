import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]

print(list(zip(outerIndex,innerIndex)))
hierarchy = list(zip(outerIndex,innerIndex))
hierarchy = pd.MultiIndex.from_tuples(hierarchy)
print(hierarchy)

df = pd.DataFrame(randn(9,3),hierarchy,columns=["Column1","Column2","Column3"])
print(df)

print(df["Column1"])
print(df.loc["Group1"])
print(df.loc[["Group1","Group2"]])
print(df.loc["Group1"].loc["Index1"]["Column1"])
df.index.names = ["Groups","Indexes"]
print(df)
print(df.xs("Group3").xs("Index1").xs("Column1"))
print(df.xs("Index1",level = "Indexes"))