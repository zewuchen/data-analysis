import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Logica CSV 08.xls")

plt.plot( 'Real GDP growth (Annual percent change)', 'Africa (Region)', data=df, marker='', color='olive', linewidth=2)
plt.plot( 'Real GDP growth (Annual percent change)', 'Asia and Pacific', data=df, marker='', color='blue', linewidth=2)
plt.plot( 'Real GDP growth (Annual percent change)', 'Europe', data=df, marker='', color='red', linewidth=2)
plt.plot( 'Real GDP growth (Annual percent change)', 'Middle East (Region)', data=df, marker='', color='tomato', linewidth=2)
plt.plot( 'Real GDP growth (Annual percent change)', 'Western Hemisphere (Region)', data=df, marker='', color='gold', linewidth=2)

plt.legend()
plt.show()
