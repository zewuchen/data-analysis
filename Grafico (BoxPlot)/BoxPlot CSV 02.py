import pandas as pd

df = pd.read_csv("BoxPlot CSV 02.csv")

df.boxplot(column=["tempMax", "tempMin"])
