import numpy as np
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt

ys=np.array((-94,-57,-29,135,143,151,245,355,392,473,486,535,571,580,620,690))
xs=np.array([4.2,3,3.7,2.7,3.2,3.6,2.4,1.3,3.8,1.7,1.6,2.2,1,0.4,2.3,1.1])

a, b = polyfit(xs, ys, 1)

plt.plot(xs, ys, '.')
plt.plot(xs, a + b * xs, '-')
plt.show()