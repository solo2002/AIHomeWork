import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-2, 2, 200, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.show()