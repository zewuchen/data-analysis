import matplotlib.pyplot as plt

aplicativos = ("WhatsApp", "Facebook", "Instagram", "Facebook Messenger", "Uber", "YouTube", 
               "Caixa", "Banco do Brasil", "Netflix", "Twitter")			#Rótulos
valores = [65, 51, 35, 19, 16, 12, 10, 10, 8, 8]							#Valores dos segmentos

plt.pie(valores, labels=aplicativos, autopct="%1.1f%%", shadow=True, startangle=12)
#autopct é para mostrar a porcentagem que o segmento vale na tabela
#shadow define a sombra
#startangle define o angulo inicial
plt.legend(aplicativos)														#Insere as legendas
plt.axis("equal")  															#Deixa a tabela redonda
