import matplotlib.pyplot as plt

times = ("Corinthians", "São Paulo", "Santos", "Palmeiras", "Outros", "Nenhum", "NS/NR")
valores = [5, 4, 0, 3, 1, 9, 9]

plt.pie(valores, labels=times, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(times)
plt.axis("equal") 