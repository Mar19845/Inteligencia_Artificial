from __future__ import print_function
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#define variables t
x, y = sp.symbols('x y') 

#function that calculates the derivate of a function based on given variable
def derivate_functions(func,variables):
    return sp.diff(func, variables)

#evaluates a function based on given variable values, return a value
def solve_function(func,x_value,y_value):
    return func.subs([(x, x_value), (y, y_value)])

#return a tuple or numpy array of two dimensiones as a intial point
def get_random_point():
    # valores 4 y 2 hay que varialos
    return (np.random.rand(2) *4) - 2

def gradiente(func,x_value,y_value):
    grad = np.random.rand(2)
    
    #solve for x
    #grad[0] = derivate_functions(func,x)
    #solve for y
    #grad[1] = derivate_functions(func,y)
    
    grad[0] = solve_function(derivate_functions(func,x),x_value,y_value)
    grad[1] = solve_function(derivate_functions(func,y),x_value,y_value)
    
    return grad

def trainDes(func,alpha,maxIter,rango):
    
    resolution = 100
    _X = np.linspace(rango[0],rango[1],resolution)
    _Y = np.linspace(rango[0],rango[1],resolution)
    
    _Z = np.zeros((resolution,resolution))
    
    vectorInicial = get_random_point()
    vectores = np.copy(vectorInicial)
    vect = []
    h = 0.001
    grad = np.zeros(2)
    for iy,yv in enumerate(_Y):
        for ix,xv in enumerate(_X):
            _Z[iy,ix]= solve_function(func,xv,yv)
            
            
    for i in range(maxIter):
        for it,th in enumerate(vectorInicial):
            vectores = np.copy(vectorInicial)
            vectores[it] = vectores[it] + h
            derivada = (solve_function(func,*vectores)-solve_function(func,*vectorInicial))/h
            #grad[it] = solve_function(func,*vectores)
            grad[it] = derivada
        
        vectorInicial = vectorInicial - alpha * grad
        vect.append(vectorInicial - alpha * grad)
        
    return _X,_Y,_Z,vectorInicial,vect
'''
def trainDes(func,alpha, maxIter, e):
    num_iterations = []
    z_values = []
    x_value = []
    y_value = []
    
    vector0 = get_random_point()
    
    vector = vector0
    for i in range(maxIter):
        gradiente_f = gradiente(func,*vector)
        
        #calular vector
        vector = vector - alpha*gradiente_f
        
        #almacenar valor de z corresponding
        z_values.append(solve_function(func,*vector))
        x_value.append(vector[0])
        y_value.append(vector[1])
        num_iterations.append(i+1)
    return z_values,num_iterations,x_value,y_value
'''

def rosenbrock10(func,alpha,maxIter,rango):
    for i in range(10):

        resolution = 100
        _X = np.linspace(rango[0],rango[1],resolution)
        _Y = np.linspace(rango[0],rango[1],resolution)
        _Z = np.zeros((resolution,resolution))
    
        vectorInicial = get_random_point()
        vectores = np.copy(vectorInicial)
        vect = []
        h = 0.001
        grad = np.zeros(2)
        for iy,yv in enumerate(_Y):
            for ix,xv in enumerate(_X):
                _Z[iy,ix]= solve_function(func,xv,yv)
            
            
        for i in range(maxIter):
            for it,th in enumerate(vectorInicial):
                vectores = np.copy(vectorInicial)
                vectores[it] = vectores[it] + h
                derivada = (solve_function(func,*vectores)-solve_function(func,*vectorInicial))/h
                #grad[it] = solve_function(func,*vectores)
                grad[it] = derivada
            
            vectorInicial = vectorInicial - alpha * grad
            vect.append(vectorInicial - alpha * grad)
        
        return _X,_Y,_Z,vectorInicial,vect






