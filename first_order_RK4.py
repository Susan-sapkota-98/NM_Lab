# To solve initial value problem of first order by R-K-4 method.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

ode = input('Enter dy/dx in terms of x and y using python syntax: ')
def F(x, y, ode):
    return eval(ode)
def f(x, y):
    return F(x, y, ode)

x = float(input('Enter the initial value of x: '))
y = float(input('Enter the initial value of y: '))
h = float(input('Enter the step size: '))
n = int(input('Enter the number of steps: '))

x_list = []
y_list = []

for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)

    y = y + (1/6) * (k1 + 2*k2 + 2*k3 + k4)
    x = x + h
    x_list.append(x)
    y_list.append(y)


T = pd.DataFrame({'x': x_list, 'y': y_list})

print('\nSolutions:')
print(T)

plt.plot(T['x'], T['y'], marker='o')
plt.title("Solution of ODE using RK4 Method")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()




