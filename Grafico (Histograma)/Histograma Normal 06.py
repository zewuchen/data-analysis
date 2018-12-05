import numpy as np
import matplotlib.pyplot as plt

dados = [43,45,53,56,56,57,58,66,67,73,74,79,80,80,81,81,81,82,83,
         83,84,88,89,91,91,92,92,97,99,99,100,100,101,102,102,102,
         103,104,107,108,109,113,114,118,121,123,126,128,137,138,139,
         144,145,147,156,162,174,178,179,184,191,198,211,214,243,249,329,
         380,403,511,522,598]

bins = [0,100,200,300,400,500,600]
plt.grid(color="red", linestyle="-", zorder=1)
#plt.hist(dados, bins=bins, zorder=2)

arr = plt.hist(dados, bins=bins, zorder=2)

for i in np.arange(len(bins)-1):
    plt.text(arr[1][i]+30, arr[0][i], str(arr[0][i]))
    #               X          Y            VALOR