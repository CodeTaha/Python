import pandas as pd

dataset = pd.read_csv("USvideos.csv")
print(dataset)

newDataset1 = dataset.drop(["video_id","trending_date"],axis = 1)
print(newDataset1)

newDataset1.to_csv("USvideosNew.csv",index = False)

excelset = pd.read_excel("Kitap1.xlsx")
print(excelset)

excelset["Column5"] = ["Recep","Taha","Konyar","Udemy"]
print(excelset)

excelset.to_excel("excelFileNew.xlsx",index = False)