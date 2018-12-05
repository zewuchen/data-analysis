import matplotlib.pyplot as plt
import pandas as pd
from numpy.polynomial.polynomial import polyfit

df = pd.read_csv("Logica CSV 09-12.csv")

xs = df["hours"]
ys = df["grade"]

a, b = polyfit(xs, ys, 1)

plt.scatter(xs,ys, color= "black")
plt.plot(xs, a + b * xs, color="red")
plt.title("Dispersão de horas por nota")
plt.show()

print("Quanto mais se estuda, maior a nota será.")