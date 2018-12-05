from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Regressao CSV 01.csv")

a, b = polyfit(df["Age"], df["Blood"], 1)

plt.plot(df["Age"], df["Blood"], '.')
plt.plot(df["Age"], a + b * df["Age"], '-')
plt.show()