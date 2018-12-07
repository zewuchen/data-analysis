import numpy as np
import matplotlib.pyplot as plt

opiniao = ("Ruim/Pessimo", "Regular", "Otima/Boa", "Sem Opinião")       #Rótulos do eixo X 

x_pos = np.arange(len(opiniao))                                         #Define o tamanho do eixo X com a quantidade dos rótulos
valores = [82, 14, 3, 1]                                                #Valores de Y

plt.bar(x_pos, valores, align="center", color="r")                      #Faz o gráfico
plt.xticks(x_pos, opiniao)                                              #Coloca os rótulos no eixo X do gráfico
plt.xlabel("Opiniões")                                                  #Label para X
plt.ylabel("Porcentagem")                                               #Label para Y