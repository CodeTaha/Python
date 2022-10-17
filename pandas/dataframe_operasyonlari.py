import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Column1": [1,2,3,4,5,6],
    "Column2": [100,100,200,300,300,100],
    "Column3": ["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
    })

print(df)
print(df.head(n = 3))
print(df["Column2"].unique())
print(df["Column2"].nunique())
print(df["Column2"].value_counts())
print(df[(df["Column1"] >= 4) & (df["Column2"] == 300)])

def times3(x):
    return x * 3

df["Column2"] = df["Column2"].apply(times3)
print(df)

taha = lambda x : x * 2
print(taha(5))

timesx3 = lambda x : x * 3
print(df["Column2"].apply(timesx3))

print(df["Column3"].apply(len))

print(df.drop("Column3",axis = 1,inplace=True))
print(df.columns)
print(df.index)
print(len(df.index))
print(df.index.names)
                        #ascending default olarak true ve küçükten büyüğe sıralar ama false yaparsak büyükten küçüğe sıralar
df.sort_values("Column2",ascending = False,inplace=True)
print(df)

df = pd.DataFrame({
    "Ay": ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir": ["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem": [10,20,50,21,67,80,30,70,75]
    })

print(df)
print(df.pivot_table(index = "Ay",columns = "Şehir",values = "Nem"))