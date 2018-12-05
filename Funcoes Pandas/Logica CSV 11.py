import pandas as pd

df = pd.read_csv("Logica CSV 09-12.csv")

homem = df.loc[df["gender"] ==  "male"]
hMax = homem["grade"].max()
hMin = homem["grade"].min()

homemMax = homem.loc[homem["grade"] == hMax]
homemMin = homem.loc[homem["grade"] == hMin]

mulher = df.loc[df["gender"] ==  "female"]
mMax = mulher["grade"].max()
mMin = mulher["grade"].min()

mulherMax = mulher.loc[mulher["grade"] == mMax]
mulherMin = mulher.loc[mulher["grade"] == mMin]

print("Homem com a maior nota: ", homemMax["fname"][homemMax["fname"].first_valid_index()])
print("Homem com a menor nota: ", homemMin["fname"][homemMin["fname"].first_valid_index()])

print("Mulher com a maior nota: ", mulherMax["fname"][mulherMax["fname"].first_valid_index()])
print("Mulher com a menor nota: ", mulherMin["fname"][mulherMin["fname"].first_valid_index()])
