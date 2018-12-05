import numpy as np
import matplotlib.pyplot as plt

times = ("Corinthians", "São Paulo", "Santos", "Palmeiras", "Outros", "Nenhum", "NS/NR")

x_pos = np.arange(len(times))
valores = [5, 4, 0, 3, 1, 9, 9]

plt.bar(x_pos, valores, align="center", color="g")
plt.xticks(x_pos, times)
plt.xlabel("Times")
plt.ylabel("Votos")