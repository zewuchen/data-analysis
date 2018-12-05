import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Dispersao CSV 03.csv')

x=df['Area']
y=df['Population']


continentes = list(set(df['Continent']))

for i in range(len(continentes)):
    index = df['Continent'] == continentes[i]
    plt.scatter(x[index], y[index], s=15, label=continentes[i])

plt.xlabel('Área KM² (Milhões)')
plt.ylabel('População (Milhões)')
plt.title('População vs Área')
plt.legend(loc='upper right')
plt.show()