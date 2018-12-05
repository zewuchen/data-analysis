import matplotlib.pyplot as plt

dados = [6,6.15,6.30,6.55,7,7.15,7.40,7.50,8.05,8.50,9,9.10,9.30,9.55,10,10.45,10.55,11.15,
         12.40,12.40,12.45,13.20,13.55,13.55,15.20,15.50,17,17.05,17.15,17.30,18.30,18.40,
         18.45,19,19.20,19.30,20.05,20.35,20.55,21.55]
groups = 16

plt.hist(dados, groups, color="red", edgecolor="black", linewidth=1.0)
plt.xlabel("Quantidade de horários")
plt.ylabel("Frequência de voôs")
plt.title("Viagens de SP para GRU")
