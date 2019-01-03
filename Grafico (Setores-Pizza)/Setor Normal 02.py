import matplotlib.pyplot as plt

times = ("Corinthians", "São Paulo", "Santos", "Palmeiras", "Outros", "Nenhum", "NS/NR")	#Rótulos
valores = [5, 4, 0, 3, 1, 9, 9]																#Valores dos segmentos

plt.pie(valores, labels=times, autopct="%1.1f%%", shadow=True, startangle=12)									
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(times)												#Insere as legendas
plt.axis("equal") 												#Deixa a tabela redonda