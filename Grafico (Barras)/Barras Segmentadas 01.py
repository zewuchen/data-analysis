import numpy as np
import matplotlib.pyplot as plt

notas = ['A-B', 'C', 'D-F']

jogou = np.array([736, 450, 193])
njogou = np.array([205, 144, 80])

index = np.arange(len(notas))

plt.bar(index, jogou, label="Jogou", color="red", bottom=njogou)
plt.bar(index, njogou, label="Não jogou", color="blue")

plt.xticks(index, notas)
plt.xlabel("Notas")
plt.legend()
plt.title("Barras de quem jogou e não jogou videogame")

plt.show()