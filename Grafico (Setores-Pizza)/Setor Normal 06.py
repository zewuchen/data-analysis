import matplotlib.pyplot as plt

obj = ("Homens A", "Mulheres A")	#Rótulos
valores = [156, 140]				#Valores dos segmentos
colors=["blue", "red"]				#Cores

plt.pie(valores, labels=obj, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(obj)														#Insere as legendas
plt.axis("equal") 													#Deixa a tabela redonda