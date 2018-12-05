import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Setor CSV 01.csv")
obj = ("A", "B", "C", "D", "F")
valores = [len(df.loc[df["Grade"] ==  "A"]), 
           len(df.loc[df["Grade"] ==  "B"]), 
           len(df.loc[df["Grade"] ==  "C"]), 
           len(df.loc[df["Grade"] ==  "D"]), 
           len(df.loc[df["Grade"] ==  "F"])]

colors=["blue", "red", "grey", "yellow", "orange"]
explode = (0.2, 0, 0, 0, 0)

plt.pie(valores, labels=obj, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(obj)
plt.axis("equal")