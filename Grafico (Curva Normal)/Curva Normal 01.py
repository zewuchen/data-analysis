import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(30,42,100)

plt.plot(x,norm.pdf(x,np.mean(x),np.std(x)), color="red")
plt.show()