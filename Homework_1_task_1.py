import numpy as np 
import math
import matplotlib.pyplot as plt

def return_array(f, step, start, finish): #дописать декоратор для второй производной и просто функции
	dots = int((finish - start)/step)
	x_axis = []
	y_axis = []
	i=0
	while i < dots:
		dy = (f(start + i*step) - f(start + (i+1)*step))/step
		y_axis.append(dy)
		x_axis.append(start + i*step)
		i+=1

	return x_axis, y_axis

def func(x):
	return math.exp(-2*x)

start = -2
finish = 2
step = 0.1

x, y = return_array(func, step, start, finish)


#print(array)
#print(x)
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
