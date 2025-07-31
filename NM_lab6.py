# To evaluateintegate( a to b  f(x)) dx by using trapezoidal rule
import numpy
import matplotlib as plt

a=float(input("Enter the lower limit of integration: "))
b=float(input("Enter the upper limit of integration: "))
n=int(input("Enter the no. of partitions: "))
h=(b-a)/n
func=input("Enter the intefrant function in x using python syntax : ")
def f(x,func):
    return eval(func)
def y(x):
    return f(x,func)


