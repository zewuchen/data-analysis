import pandas as pd

df = pd.read_csv("Logica CSV 09-12.csv")

nota1 = df.loc[df["grade"] < 60]
nota1 = len(nota1) / len(df.index)

nota2 = df.loc[df["grade"] == 70]
nota2 = len(nota2) / len(df.index)

nota3 = df.loc[df["grade"] == 80]
nota3 = len(nota3) / len(df.index)

nota4 = df.loc[df["grade"] > 90]
nota4 = len(nota4) / len(df.index)

print("Alunos com notas <60: %.1f %%" %(nota1 * 100))
print("Alunos com notas =70: %.1f %%" %(nota2 * 100))
print("Alunos com notas =80: %.1f %%" %(nota3 * 100))
print("Alunos com notas >90: %.1f %%" %(nota4 * 100))