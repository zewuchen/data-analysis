import matplotlib.pyplot as plt

obj = ("Homens A", "Mulheres A")
valores = [156, 140]
colors=["blue", "red"]

plt.pie(valores, labels=obj, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(obj)
plt.axis("equal")