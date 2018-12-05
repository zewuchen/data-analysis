import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Dispersao CSV 02.csv")

x = df["Graus"]
y = df["Vendas"]

plt.grid(color="b")
plt.scatter(x,y,color="r")