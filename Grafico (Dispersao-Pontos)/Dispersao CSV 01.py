import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Dispersao CSV 01.csv")

x = df["Terceiriza"]
y = df["Atraso"]

plt.grid(color="b")
plt.scatter(x,y,color="r")