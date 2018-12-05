import pandas as pd

nome = []
df = pd.read_csv("Logica CSV 01-06.csv")

minimo = df["Cars Sold"].min()

for i in range(len(df)):
    if(df["Cars Sold"][i] == minimo):
        nome.append(df["Fname"][i])
    
nome.sort()

print(nome)