import matplotlib.pyplot as plt

dados=[1434,3692,4482,4119,1043,4520,432,618,4564,4086,4371,2918,141,127,929,3130,3174,2181,
         559,940,5123,5674,1423,1316,901,943,3041,3870,5564,353,1161,1732,3322,8608,659]
groups = 10

plt.hist(dados, groups, color="violet", edgecolor="black", linewidth=1.0)
plt.xlabel("Gastos (DOLÁRES)")
plt.ylabel("Quantidade de países")
plt.title("Distribuição de países em investimentos")