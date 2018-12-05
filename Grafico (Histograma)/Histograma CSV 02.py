import pandas as pd

df = pd.read_csv("Histograma CSV 02.csv")
bins = [0,100,200,300,400,500,600]

df.hist(column=["dados"], bins=bins)