import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = 496
desvio= 115
x = np.linspace(media-3*desvio,media+3*desvio,1500000)
fill = np.arange(643.4, media+3*desvio)

plt.plot(x,norm.pdf(x,media,desvio), color="purple")
plt.fill_between(fill, norm.pdf(fill,media,desvio), color="purple")
plt.show()