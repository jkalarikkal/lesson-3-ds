import pandas as pd

df = pd.DataFrame({
    "Name":["Jaanvi", "Sindhuja", "ok", "ainab" ,  "Rumaysah", "Kevin", "bok"],
    "Age":[15,27,53,24,75,32,12],
    "City":["Doha","Madurai","Paris","London","San Francisco", "New York", "Shanghai"]
})

print(df.head())
print()

print(df.head(7))

print()

print(df.shape)

print(df.info())
print(df.describe())

print(df["City"])
print(df["Age"].std())
print(df["Age"].max())

