import matplotlib.pyplot as plt

obj = ("A", "B", "C", "D", "F")
valores = [296, 198, 197, 225, 83]
colors=["blue", "red", "grey", "yellow", "orange"]
explode = (0.2, 0, 0, 0, 0)

plt.pie(valores, labels=obj, explode=explode, colors=colors, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(obj)
plt.axis("equal")