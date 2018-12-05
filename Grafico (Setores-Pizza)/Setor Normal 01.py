import matplotlib.pyplot as plt

opinioes = ("Ruim/Péssimo", "Regular", "Ótima/Boa", "Sem Opinião")
valores = [82, 14, 3, 1]
colors=["blue", "red", "grey", "yellow"]
explode = (0.1, 0, 0, 0) 

plt.pie(valores, labels=opinioes, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(opinioes)
plt.axis("equal") 