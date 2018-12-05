import matplotlib.pyplot as plt

dados = [76,106,87,83,83,76,81,82,95,85,89,93,70,101,107,79,99,92]
groups = 10

plt.hist(dados, groups, color="gray", edgecolor="black", linewidth=1.0)
plt.xlabel("Peso")
plt.ylabel("Quantidade de jogadores")
plt.title("Distribuição de jogadores por peso")