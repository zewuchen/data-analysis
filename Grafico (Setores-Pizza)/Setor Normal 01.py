import matplotlib.pyplot as plt

opinioes = ("Ruim/Péssimo", "Regular", "Ótima/Boa", "Sem Opinião")					#Rótulos
valores = [82, 14, 3, 1]															#Valores dos segmentos
colors=["blue", "red", "grey", "yellow"]											#Cores
explode = (0.1, 0, 0, 0) 															#Valor de afastamento de cada segmento

plt.pie(valores, labels=opinioes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
#explode é para separar um segmento da tabela										
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(opinioes)																#Insere as legendas
plt.axis("equal") 																	#Deixa a tabela redonda