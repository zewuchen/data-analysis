import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = 1011
desvio=216
x = np.linspace(media-3*desvio,media+3*desvio,1500000)
fill = np.arange(820, media+3*desvio)

plt.plot(x,norm.pdf(x,media,desvio), color="purple")
plt.fill_between(fill, norm.pdf(fill,media,desvio), color="purple")
plt.show()