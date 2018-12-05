import numpy as np
import matplotlib.pyplot as plt

regioes = ['SUDESTE', 'NORDESTE', 'SUL', 'NORTE', 'CENTRO-OESTE']

bolsonaro = np.array([53.965, 28.187, 58.446, 50.357, 57.677])
haddad = np.array([20.74, 49.824, 19.213, 30.331, 20.59])
ciro = np.array([11.937, 16.214, 8.786, 7.657, 9.707])

index = np.arange(len(regioes))

plt.bar(index, ciro, label="Ciro", color="yellow")
plt.bar(index, haddad, label="Haddad", color="blue", bottom= ciro)
plt.bar(index, bolsonaro, label="Bolsonaro", color="red", bottom= ciro+haddad)

plt.xticks(index, regioes)
plt.xlabel("Regiões")
plt.legend()
plt.title("Distribuição de presidenciáveis nas regiões brasileiras")

plt.show()