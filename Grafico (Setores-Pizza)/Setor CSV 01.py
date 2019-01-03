import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Setor CSV 01.csv")			#Pega o dataset
obj = ("A", "B", "C", "D", "F")					#Rótulos
valores = [len(df.loc[df["Grade"] ==  "A"]), 	#Localiza as notas A
           len(df.loc[df["Grade"] ==  "B"]), 	#Localiza as notas B
           len(df.loc[df["Grade"] ==  "C"]), 	#Localiza as notas C
           len(df.loc[df["Grade"] ==  "D"]), 	#Localiza as notas D
           len(df.loc[df["Grade"] ==  "F"])]	#Localiza as notas F

colors=["blue", "red", "grey", "yellow", "orange"]	#Cores
explode = (0.2, 0, 0, 0, 0)							#Valor de afastamento de cada segmento

plt.pie(valores, labels=obj, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
#explode é para separar um segmento da tabela										
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(obj)											#Insere as legendas
plt.axis("equal") 										#Deixa a tabela redonda