# To evaluate the fx integrate limit(a,b) using Trapezoidal rule.
import numpy as np
import matplotlib.pyplot as plt  

a = float(input("Enter the lower limit of integration: "))
b = float(input("Enter the upper limit of integration: "))
n = int(input("Enter the no. of partitions: "))
h = (b - a) / n
func = input("Enter the integrant function in x using python syntax : ")

def f(x, func):
    return eval(func)

def y(x):
    return f(x, func)

x = np.linspace(a, b, n + 1)
I = 0
S = 0

for i in range(1, n):
    S += y(x[i])

I = (h / 2) * (y(x[0]) + 2 * S + y(x[n]))

print(f"The approximation integral by Trapezoidal rule is {I}")

ypoints = [y(val) for val in x]
plt.plot(x, ypoints, color='r', label='Best fit curve')

xval = np.linspace(a - 10, b + 10, 1000)
plt.plot(xval, [y(val) for val in xval], label='Eqn in curve')

for i in range(n):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, ypoints[i], ypoints[i+1], 0]
    plt.fill(xs, ys, color='pink', edgecolor='none', alpha=0.2)

plt.title("Trapezoidal Rule Approximation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()
