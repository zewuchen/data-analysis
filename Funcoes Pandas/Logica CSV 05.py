import pandas as pd

df = pd.read_csv("Logica CSV 01-06.csv")

media = df.loc[df["Cars Sold"] >  3].mean()

print("A média de carros é: ", media["Hours Worked"])