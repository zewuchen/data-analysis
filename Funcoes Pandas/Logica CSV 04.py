import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Logica CSV 01-06.csv")
obj = ("F", "M")
valores = [len(df.loc[df["Gender"] ==  "F"]), 
           len(df.loc[df["Gender"] ==  "M"])]

colors=["blue", "red"]

plt.pie(valores, labels=obj, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(obj)
plt.axis("equal")