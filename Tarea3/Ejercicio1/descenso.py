import sympy as sp
import numpy as np

x = sp.Symbol('x')

#ecuacion1
f = 
dfdx = (x**4)+1-4*x+0.5
gradient = sp.diff(dfdx)

print(gradient)

#ecuacion2

dfdx1 =(x**2)-(100*x**2)-(2*x)
gradient1 = sp.diff(dfdx1)

print(gradient1)

#ecuacion3

dfdx2 = 0 #sepaputas
gradient2 = sp.diff(dfdx2)

print(gradient2)

def trainDes(f, df, x0, alpha, maxIter, e):
    iterCounter = 0


