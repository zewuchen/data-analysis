import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Dispersao CSV 04.csv")

x = df["Graus"]
y = df["Vendas"]

plt.grid(color="gray")
plt.scatter(x, y, s=15)
    
plt.xlabel("ºC")
plt.ylabel("Vendas")
plt.title("Venda em relação aos graus")
plt.legend()