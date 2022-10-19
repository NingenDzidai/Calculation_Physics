import matplotlib.pyplot as plt
import numpy as np

def g(x, y):
  return y

def Sol_Dif_eq(f, x_0, y_0):
  dx = 0.001
  x = np.arange(x_0, 100, dx)
  y = []
  y.append(y_0)
  #y = [y_0]
  for i in range(1, len(x)):
    y.append(y[-1] + dx*f(x[-1], y[-1]))
  return y

x = np.arange(0, 100, 0.001)
y_sol = Sol_Dif_eq(g, 0, 1)
plt.figure()
plt.plot(x, y_sol)
plt.plot(x, np.exp(x))
plt.show()