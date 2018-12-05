import pandas as pd

nome = []
df = pd.read_csv("Logica CSV 01-06.csv")

maximo = df["Cars Sold"].max()

for i in range(len(df)):
    if(df["Cars Sold"][i] == maximo):
        nome.append(df["Fname"][i])
    
nome.sort()

print(nome)