import numpy as np
import matplotlib.pyplot as plt

notas = ['A-B', 'C', 'D-F']                                             #Rótulos do eixo X

jogou = np.array([736, 450, 193])                                       #Primeiro valor do segmento Y
njogou = np.array([205, 144, 80])                                       #Segundo valor do segmento Y

index = np.arange(len(notas))                                           #Define o tamanho do eixo X com a quantidade dos rótulos

plt.bar(index, jogou, label="Jogou", color="red", bottom=njogou)        #Faz o gráfico com a parte de cima
plt.bar(index, njogou, label="Não jogou", color="blue")                 #Faz o gráfico com a parte de baixo

plt.xticks(index, notas)                                                #Coloca os rótulos no eixo X do gráfico
plt.xlabel("Notas")                                                     #Label do eixo X    
plt.legend()                                                            #Coloca a legenda  
plt.title("Barras de quem jogou e não jogou videogame")                 #Define um título
plt.show()                                                              #Mostra o gráfico final