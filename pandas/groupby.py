import numpy as np
import pandas as pd

dataset = {
    "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
    "Çalışan":["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
    "Maaş":[3000,3500,2500,4500,4000,2000]
    }

df = pd.DataFrame(dataset)
print(df)

DepGroup = df.groupby("Departman")
print(DepGroup.sum())
print(int(DepGroup.sum().loc["Bilişim"]))

print(df.groupby("Departman").count())
print(df.groupby("Departman").max())
print(df.groupby("Departman").min())
print(df.groupby("Departman").min()["Maaş"])
print(df.groupby("Departman").min()["Maaş"]["Bilişim"])
print(df.groupby("Departman").mean()["Maaş"]["İnsan Kaynakları"])