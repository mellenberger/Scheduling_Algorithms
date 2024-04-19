import random
import numpy as np
from matplotlib import pyplot as plt
import scipy.stats as stats         


x = np.linspace (0, 20, 200) 
y1 = stats.gamma.pdf(x, a=100, scale=1/10)
plt.plot(x, y1, "y-", color='black') 
plt.ylim([0,0.5])
plt.xlim([2,18])


x = np.linspace (0, 20, 200) 
y1 = stats.gamma.pdf(x, a=10, scale=1/1)
plt.plot(x, y1)

y1 = stats.gamma.pdf(x, a=16, scale=1/2)
plt.plot(x, y1)

y1 = stats.gamma.pdf(x, a=32, scale=1/4)
plt.plot(x, y1)
plt.legend([(r'$\alpha=100, \beta=10$'), (r'$\alpha=10, \beta=1$'), (r'$\alpha=16, \beta=2$'), (r'$\alpha=32, \beta=4$')])
plt.show()