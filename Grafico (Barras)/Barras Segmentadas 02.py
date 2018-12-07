import numpy as np
import matplotlib.pyplot as plt

regioes = ['SUDESTE', 'NORDESTE', 'SUL', 'NORTE', 'CENTRO-OESTE']                   #Rótulos do eixo X

bolsonaro = np.array([53.965, 28.187, 58.446, 50.357, 57.677])                      #Primeiro valor do segmento Y
haddad = np.array([20.74, 49.824, 19.213, 30.331, 20.59])                           #Segundo valor do segmento Y
ciro = np.array([11.937, 16.214, 8.786, 7.657, 9.707])                              #Terceiro valor do segmento Y

index = np.arange(len(regioes))                                                     #Define o tamanho do eixo X com a quantidade dos rótulos

plt.bar(index, ciro, label="Ciro", color="yellow")                                  #Faz o gráfico com a parte de cima
plt.bar(index, haddad, label="Haddad", color="blue", bottom= ciro)                  #Faz o gráfico com a parte do meio    
plt.bar(index, bolsonaro, label="Bolsonaro", color="red", bottom= ciro+haddad)      #Faz o gráfico com a parte de baixo    

plt.xticks(index, regioes)                                                          #Coloca os rótulos no eixo X do gráfico
plt.xlabel("Regiões")                                                               #Label do eixo X    
plt.legend()                                                                        #Coloca a legenda 
plt.title("Distribuição de presidenciáveis nas regiões brasileiras")                #Define um título

plt.show()                                                                          #Mostra o gráfico final