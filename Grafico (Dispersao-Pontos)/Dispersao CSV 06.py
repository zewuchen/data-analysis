import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Dispersao CSV 06.csv')

x= np.arange(1, len(df['Percentual'])+1)
y=df['Percentual']


msg = list(set(df['MsgTempo']))

for i in range(len(msg)):
    index = df['MsgTempo'] == msg[i]
    plt.grid(color="gray")
    plt.scatter(x[index], y[index], s=15, label=msg[i])

plt.ylabel('Percentual')
plt.title('Distribuição das gorjetas')
plt.legend(loc='upper right')
plt.show()