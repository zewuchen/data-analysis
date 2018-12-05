import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Dispersao CSV 05.csv")

x = df["Mph"]
y = df["Mpg"]

plt.grid(color="gray")
plt.scatter(x, y, s=50)
    
plt.xlabel("Mph")
plt.ylabel("Mpg")
plt.title("Consumo vs Velocidade")
plt.legend()