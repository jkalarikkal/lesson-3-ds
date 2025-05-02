import pandas as pd

df = pd.DataFrame({
    "colour":["red", "orange", "yellow", "green" ,  "blue", "purple", "pink"],
    "texture":[ "soft","rough","smooth","matte","shiny","clear","hard"],
    "object":["pillow","bed","sofa","book","jacket", "table", "pencilcase"]
})

print(df.head())
print()

print(df.head(7))

print()

print(df.shape)

print(df.info())
print(df.describe())