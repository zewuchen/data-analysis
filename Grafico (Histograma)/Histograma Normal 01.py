import matplotlib.pyplot as plt

dados = [8,9,8,8,39,22,8,10,17,18,53,8,8,17,12,25,10,30,46,8,8,8,31,16,8,70,8]
groups = 10

plt.hist(dados, groups, color="green", edgecolor="black", linewidth=1.0)
plt.xlabel("Quantidade de deputados")
plt.ylabel("Frequência nos Estados")
plt.title("Deputados federais brasileiros")