import matplotlib.pyplot as plt

aplicativos = ("WhatsApp", "Facebook", "Instagram", "Facebook Messenger", "Uber", "YouTube", 
               "Caixa", "Banco do Brasil", "Netflix", "Twitter")
valores = [65, 51, 35, 19, 16, 12, 10, 10, 8, 8]

plt.pie(valores, labels=aplicativos, autopct="%1.1f%%", shadow=True, startangle=12)
plt.legend(aplicativos)
plt.axis("equal") 
