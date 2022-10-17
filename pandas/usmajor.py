import pandas as pd

soccer = pd.read_csv("mls-salaries-2017.csv")
print(soccer.head(n = 10))

print(len(soccer.index))
print(soccer["base_salary"].mean())
print(soccer["base_salary"].max())
print(soccer["base_salary"].min())

print(soccer[soccer["guaranteed_compensation"] == soccer["guaranteed_compensation"].max()]["last_name"].iloc[0])

print(soccer[soccer["last_name"] == "Gonzalez Pirez"]["position"].iloc[0])

print(soccer.groupby("position").mean())
print(soccer["position"].nunique())
print(soccer["position"].value_counts())
print(soccer["club"].value_counts())

def findland_finder(last_name):
    if "son" in last_name.lower():
        return True
    else:
        return False
   
print(soccer[soccer["last_name"].apply(findland_finder)])