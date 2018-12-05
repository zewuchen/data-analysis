import pandas as pd

df = pd.read_csv("Logica CSV 01-06.csv")

media = df["Cars Sold"].mean()

print("A média de carros é: ", media)