from __future__ import print_function
import sympy as sp
import matplotlib.pyplot as plt
import descenso as ds

#define variables t
x, y = sp.symbols('x y') 

#ejercicio 1 prueba
func = (x**4) + (y**4) - (4*x*y) + (0.5*y) + 1

#ejercicio 2 prueba
func1 = 100 *( (y-x**2)**2) + ((1-x)**2)

state = True


opt = input("\n1.Polinomio R2 a R \n2.Rosenbrock 2-dimensional \n3.Rosenbrock 10-dimensional\nIngrese la función a la que desea aplicarle descenso maximo: ")

while(state):
    if opt == "1":

        _X,_Y,_Z,vectorInicial,vect = ds.trainDes(func,0.001, 1000,rango=[-2,2])
        
    if opt == "2":

        _X,_Y,_Z,vectorInicial,vect = ds.trainDes(func1,0.001, 1000,rango=[-2,2])

    if opt == "3":

        _X,_Y,_Z,vectorInicial,vect = ds.rosenbrock10(func1,0.001, 1000,rango=[-2,2])


    plt.contour(_X,_Y,_Z,100)
    for point in vect:
        plt.plot(point[0],point[1],'.',c='red',alpha=0.4)
    plt.show()
    state = False