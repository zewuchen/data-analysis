import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Logica CSV 14.csv")

etniasLabel = ["White", "Hawaiian", "Black", "Asian", "Multiracial", "Other", "Native"]
etniasValues = [df["pop_white"][3], df["pop_hawaiian"][3], df["pop_black"][3], df["pop_asian"][3],
          df["pop_2ormore"][3] , df["pop_other"][3] , df["pop_native"][3]]

total = sum(etniasValues)

for i in range(len(etniasValues)):
    etniasValues[i] = (etniasValues[i] / total) * 100

plt.grid()
plt.title("Porcentagem de pessoas")
plt.bar(etniasLabel, etniasValues, color="red")
plt.show()