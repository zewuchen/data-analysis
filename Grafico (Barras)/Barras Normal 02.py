import numpy as np
import matplotlib.pyplot as plt

times = ("Corinthians", "São Paulo", "Santos", "Palmeiras", "Outros", "Nenhum", "NS/NR")    #Rótulos do eixo X 

x_pos = np.arange(len(times))                                                               #Define o tamanho do eixo X com a quantidade dos rótulos
valores = [5, 4, 0, 3, 1, 9, 9]                                                             #Valores de Y

plt.bar(x_pos, valores, align="center", color="g")                                          #Faz o gráfico
plt.xticks(x_pos, times)                                                                    #Coloca os rótulos no eixo X do gráfico
plt.xlabel("Times")                                                                         #Label para X
plt.ylabel("Votos")                                                                         #Label para Y