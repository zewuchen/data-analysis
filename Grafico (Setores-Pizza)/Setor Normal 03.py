import matplotlib.pyplot as plt

aplicativos = ("WhatsApp", "Facebook", "Instagram", "Google", "Google Chrome", "Uber", "Outros")	#Rótulos
valores = [49, 9, 5, 2, 2, 2, 31]																	#Valores dos segmentos

plt.pie(valores, autopct="%1.1f%%", shadow=True, startangle=12)
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(aplicativos)											#Insere as legendas
plt.axis("equal") 												#Deixa a tabela redonda