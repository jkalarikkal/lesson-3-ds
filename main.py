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

#started titanic csv file

data = pd.read_csv("titanic.csv")

print(data.head())
print(data.info())

print(data[["Name","Age"]])

print(data["Age"]>18)

age35 = data[data["Age"]>35]

print(age35.head())
print(age35.shape)

p2p3 =  data[(data["Pclass"]== 2)| (data["Pclass"] == 3)]

print(p2p3[["Name","Pclass"]].head(20))


#Task - Get the mean fare of Male travelling in Pclass 1
