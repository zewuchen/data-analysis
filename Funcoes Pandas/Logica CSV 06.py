import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Logica CSV 01-06.csv")

rotulos = ["1 Ano", "2 Anos", "3 Anos", "4 Anos", "5 Anos"]

mediaEXP1 = df.loc[df["Years Experience"] == 1]
mediaEXP1 = mediaEXP1["Hours Worked"].mean()

mediaEXP2 = df.loc[df["Years Experience"] == 2]
mediaEXP2 = mediaEXP2["Hours Worked"].mean()

mediaEXP3 = df.loc[df["Years Experience"] == 3]
mediaEXP3 = mediaEXP3["Hours Worked"].mean()

mediaEXP4 = df.loc[df["Years Experience"] == 4]
mediaEXP4 = mediaEXP4["Hours Worked"].mean()

mediaEXP5 = df.loc[df["Years Experience"] == 5]
mediaEXP5 = mediaEXP5["Hours Worked"].mean()

valores = [mediaEXP1, mediaEXP2, mediaEXP3, mediaEXP4, mediaEXP5]

index = np.arange(len(rotulos))

plt.bar(index, valores)
plt.xticks(index, rotulos, fontsize=20, rotation=30)
plt.title("Média de horas trabalhadas por experiência")