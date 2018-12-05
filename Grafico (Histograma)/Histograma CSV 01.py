import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Histograma CSV 01.csv")
bins = [5,10,15,20,25,30]

plt.hist(df["Hours of Study"], bins=bins, color="red", edgecolor="black", linewidth=1.0)