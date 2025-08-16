# To solve initial value problem of first order by Modified Euler method.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Input: dy/dx as a function of x and y
ode = input('Enter dy/dx in terms of x and y using python syntax: ')

# Define the function using eval for dynamic input
def F(x, y, ode):
    return eval(ode)

def f(x, y):
    return F(x, y, ode)

# Initial conditions and parameters
x = float(input('Enter the initial value of x: '))
y = float(input('Enter the initial value of y: '))
h = float(input('Enter the step size: '))
n = int(input('Enter the number of steps: '))

x_list = [x]
y_list = [y]

# Modified Euler's Method (Heun's method)
for i in range(n):
    y_predictor = y + h * f(x, y)  # Predictor
    y_corrector = y + (h / 2) * (f(x, y) + f(x + h, y_predictor))  # Corrector
    x = x + h
    y = y_corrector  # Update y with corrector

    x_list.append(x)
    y_list.append(y)

# Displaying the results
T = pd.DataFrame({'x': x_list, 'y': y_list})

print('\nSolutions:')
print(T)

# Plotting
plt.plot(T['x'], T['y'], marker='o')
plt.title("Solution of ODE using Modified Euler's Method")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()




