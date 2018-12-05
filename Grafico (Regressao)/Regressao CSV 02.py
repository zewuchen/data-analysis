from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Regressao CSV 02.csv")

a, b = polyfit(df["body"], df["brain"], 1)

plt.plot(df["body"], df["brain"], '.')
plt.plot(df["body"], a + b * df["body"], '-')
plt.show()