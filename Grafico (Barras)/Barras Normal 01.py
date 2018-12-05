import numpy as np
import matplotlib.pyplot as plt

opiniao = ("Ruim/Pessimo", "Regular", "Otima/Boa", "Sem Opinião") 

x_pos = np.arange(len(opiniao))
valores = [82, 14, 3, 1]

plt.bar(x_pos, valores, align="center", color="r")
plt.xticks(x_pos, opiniao)
plt.xlabel("Opiniões")
plt.ylabel("Porcentagem")