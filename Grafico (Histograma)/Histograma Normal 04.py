import matplotlib.pyplot as plt

dados = [190,205,198,195,188,194,187,190,202,197,196,209,198,209,207,195,199,217]
groups = 10

plt.hist(dados, groups, color="yellow", edgecolor="black", linewidth=1.0)
plt.xlabel("Altura")
plt.ylabel("Quantidade de jogadores")
plt.title("Distribuição de jogadores por altura")