import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BoxPlot CSV 03.csv")
dados = []

for i in range(len(df)):
    if (df['property_type'][i] == 'Apartment'):
        dados.append(df['price'][i])
        
plt.boxplot(dados)