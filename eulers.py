# To solve initial value problem of first order by Euler's method.
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
    y_predictor=y+h*f(x,y)
    y_corrector=y+h/2*(f(x,y)+f(x+h,y_predictor))
    x=x+h
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




