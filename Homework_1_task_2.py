# метод бисекции -- простейший метод решения нелинейных уравнений вида f(x) = 0 
# если знаки функции на краях выбранного отрезка отличаются по знаку, то есть хотя бы один такой x, что f(x) = 0
import numpy as np
import math

def func(x):
	return -1 + math.exp(-x)

eps = 0.01 
a = -5 
b = 5 

while b - a > eps:

	if func(a) == 0:
		break
	if func(b) == 0:
		break

	dx = (b-a)/2
	if np.sign(func(a + dx)) != np.sign(func(b)):
		a = a + dx
	else:
		b = a + dx

print(a)