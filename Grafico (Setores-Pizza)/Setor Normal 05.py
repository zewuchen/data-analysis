import matplotlib.pyplot as plt

obj = ("A", "B", "C", "D", "F")		#Rótulos
valores = [296, 198, 197, 225, 83]	#Valores dos segmentos
colors=["blue", "red", "grey", "yellow", "orange"]	#Cores
explode = (0.2, 0, 0, 0, 0)			#Valor de afastamento de cada segmento

plt.pie(valores, labels=obj, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
#explode é para separar um segmento da tabela										
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(obj)														#Insere as legendas
plt.axis("equal") 													#Deixa a tabela redonda