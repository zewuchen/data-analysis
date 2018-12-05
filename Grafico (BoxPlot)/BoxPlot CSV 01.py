import pandas as pd

df = pd.read_csv("BoxPlot CSV 01.csv")

df.boxplot(column=["dados"])