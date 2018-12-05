import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

media = 75
desvio=8
x = np.linspace(media-3*desvio,media+3*desvio,500)
fill = np.arange(68.953, 80.063)

plt.plot(x,norm.pdf(x,media,desvio), color="blue")
plt.fill_between(fill, norm.pdf(fill,media,desvio), color="blue")
plt.show()