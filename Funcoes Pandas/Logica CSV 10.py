import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Logica CSV 09-12.csv")

nota1 = df.loc[df["grade"] < 60]
nota1 = len(nota1) / len(df.index)

nota2 = df.loc[(df["grade"] > 60) & (df["grade"] < 70)]
nota2 = len(nota2) / len(df.index)

nota3 = df.loc[(df["grade"] > 70) & (df["grade"] < 80)]
nota3 = len(nota3) / len(df.index)

nota4 = df.loc[df["grade"] > 80]
nota4 = len(nota4) / len(df.index)

obj = ("< 60", "60 <> 70 ", "70 <> 80", "> 80")
valores = [nota1*100, nota2*100, nota3*100, nota4*100]
colors=["blue", "red", "grey", "yellow"]
explode = (0, 0, 0, 0.2)

plt.pie(valores, labels=obj, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True)
plt.legend(obj)
plt.axis("equal")