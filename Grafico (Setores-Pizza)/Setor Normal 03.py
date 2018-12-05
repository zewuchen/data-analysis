import matplotlib.pyplot as plt

aplicativos = ("WhatsApp", "Facebook", "Instagram", "Google", "Google Chrome", "Uber", "Outros")
valores = [49, 9, 5, 2, 2, 2, 31]

plt.pie(valores, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(aplicativos)
plt.axis("equal") 