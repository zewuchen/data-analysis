import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Logica CSV 07.csv')

states = df['State']

percent_people = df['Percentage']

labels = df['State']
plt.bar(states,percent_people,)
plt.xticks(states, labels, rotation='vertical',fontsize=7)
plt.show()