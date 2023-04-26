# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 22:52:18 2023

@author: Administrador
"""

def interseccion(A,B):
    res = []
    for x in A:
        if x in B:
            res.append(x)
    return res

def diferencia(A,B):
    # Hace la diferencia de conjuntos A-B
    res = []
    for x in A:
        if x not in B:
            res.append(x)
    return res

def diferenciaSimetrica(A,B):
    # Hace la diferencia simetrica de conjuntos A triangulito B
    res_A_B = diferencia(A,B)
    res_B_A = diferencia(B,A)
    res = set(res_A_B + res_B_A)
    return res

############################################################################
    
# Defino una relación como una lista de tuplas (x,y) con
# x \in A, y \in B que cumplen cierta condición

def productoCartesiano(A,B):
    lista = [(x,y) for x in A for y in B]
    return set(lista)

def rel_ej_1_27():
    rel = []
    for x in range(1,93):
        for y in range(1,93):
            if x**2-y**2 == 93*x-93*y:
                rel.append((x,y))
    return set(rel)

def dominioNatural(relacion):
    dominio = []
    for elem in relacion:
        dominio.append(elem[0])
    return set(dominio)

def imagen(relacion):
    img = []
    for elem in relacion:
        img.append(elem[0])
    return set(img)

def esReflexiva(relacion):
    dom = dominioNatural(relacion)
    for x in dom:
        if (x,x) not in relacion:
            return False
    return True

def esSimetrica(relacion):
    dom = dominioNatural(relacion)
    img = imagen(relacion)
    for x in dom:
        for y in img:
            if (x,y) in relacion and (y,x) not in relacion:
                return False
    return True      

def esAntiSimetrica(relacion):
    dom = dominioNatural(relacion)
    img = imagen(relacion)
    for x in dom:
        for y in img:
            if (x,y) in relacion and (y,x) in relacion:
                if x != y:
                    return False
    return True

def esTransitiva(relacion):
    for (a,b) in relacion:
        for (c,d) in relacion:
            if b == c and (a,d) not in relacion:
                return False
    return True

def esEquivalencia(relacion):
    if esReflexiva(relacion) and esSimetrica(relacion) and esTransitiva(relacion):
        return True
    return False

def esOrden(relacion):
    if esReflexiva(relacion) and esAntiSimetrica(relacion) and esTransitiva(relacion):
        return True
    return False

# Casos de prueba
    
rel1 = rel_ej_1_27() # Es refl, sim, trans
rel2 = {(1,1), (1,2), (1,4), (2,1), (2,2), (3,3), (4,1), (4,4)}
# Es refl, sim
S = [1,2,3,4,5,6]
rel3 = [ (x,y) for x in S for y in S if y%x==0]
# Es refl, antisim, trans
rel4 = {(1,1), (2,2), (3,3), (4,4)} # Es todo
rel5 = {(1,1), (1,2), (2,1), (2,2), (3,3), (3,4), (4,3), (4,4)} # Es de equiv
rel6 = {(1,1), (1,2), (2,1), (2,2), (3,3), (4,4)} # Es de equiv

############################################################################

def clasesDeEquivalencia(relacion):
    if not esEquivalencia(relacion):
        print("No es relacion de equivalencia")
        return 
    dom = dominioNatural(relacion)
    clases = []
    for x in dom:
        clase_x = {x}
        for y in dom:
            if (x,y) in relacion:
                clase_x.add(y)
        if clase_x not in clases:
            clases.append(clase_x)
    return clases

"""
clasesDeEquivalencia(rel4)
[{1}, {2}, {3}, {4}]

clasesDeEquivalencia(rel3)
No es relacion de equivalencia

clasesDeEquivalencia(rel2)
No es relacion de equivalencia

clasesDeEquivalencia(rel5)
[{1, 2}, {3, 4}]
clasesDeEquivalencia(rel6)
[{1, 2}, {3}, {4}]

clasesDeEquivalencia(rel1)
[{1, 92}, {2, 91}, {3, 90}, {4, 89}, {5, 88}, {6, 87}, {7, 86}, {8, 85},
 {9, 84}, {10, 83}, {11, 82}, {12, 81}, {13, 80}, {14, 79}, {15, 78}, 
 {16, 77}, {17, 76}, {18, 75}, {19, 74}, {20, 73}, {21, 72}, {22, 71},
 {23, 70}, {24, 69}, {25, 68}, {26, 67}, {27, 66}, {28, 65}, {29, 64}, 
 {30, 63}, {31, 62}, {32, 61}, {33, 60}, {34, 59}, {35, 58}, {36, 57},
 {37, 56}, {38, 55}, {39, 54}, {40, 53}, {41, 52}, {42, 51}, {43, 50}, 
 {44, 49}, {45, 48}, {46, 47}]
"""

############################################################################
        
def funcionARelacion(dominio, funcion):
    R = [(x,funcion(x)) for x in dominio]
    return  set(R)

def evaluar(F,x0):
    for (x,y) in F:
        if x == x0:
            y = F(x0)
    return y
                 
def preimagen(funcion_como_rel, y0):
    dom = dominioNatural(funcion_como_rel)
    preimg = []
    for x in dom:
        if (x,y0) in funcion_como_rel:
            preimg.append(x)
    return set(preimg)

def esBiyectiva(funcion_como_rel):
    dom = dominioNatural(funcion_como_rel)
    img = imagen(funcion_como_rel)
    if len(dom) == len(img):
        return True
    return False

def inversa(funcion_como_rel):
    if not esBiyectiva(funcion_como_rel):
        print('La función no es biyectiva')
        return 
    inversa = []
    for (x,y) in funcion_como_rel:
        inversa.append((y,x))
    return set(inversa)

############################################################################
# Conjuntos de funciones
    
from itertools import product

def productoCartesianoN(Y, n):
    return set(product(Y,repeat=n))

# t es un elemento de productoCartesianoN(Y, n), n = len(X)

def tuplaAFuncion(X, t):
    lista_X = list(X)
    R = set()
    for i in range(len(t)):
        R.add((lista_X[i],t[i]))
    return R

def funciones(X,Y):
    n = len(X)
    Y_n = productoCartesianoN(Y, n)
    lista_funcs = []
    for t in Y_n:
        lista_funcs.append(tuplaAFuncion(X, t))
    return lista_funcs

def ej3_14():
    X = set([1,2,3,4,5,6,7])
    #lista_de_funciones = funciones(X,X)
    contador = 0
    I = set([3,4,5,6,7])
    for f in productoCartesianoN(X, len(X)):
        if set(f) == X:
            if f[0] in I and f[1] in I and f[2] in I:
                contador += 1
    return contador
# Respuesta: 5*4*3*4*3*2*1 = 1440

###########################################################################
# Partes
# Veo a partes como las funciones de X a {0,1}

# from more_itertools import powerset
    
def partes(X):
    Y = set([0,1])
    return funciones(X,Y)

def partes2(X):
    Y = set([0,1])
    subconjs = set(product(Y,repeat=len(X)))
    lista_X = list(X)
    partes = []
    for t in subconjs:
        subconj_t = []
        for i in range(len(X)):
            if t[i] == 1:
                subconj_t.append(lista_X[i])
        partes.append(subconj_t)
    partes.sort(key=len)
    return partes
    
def clase4_ej19():
    X = {267, 493, 869, 961, 1000, 1153, 1246, 1598, 1766, 1922} 
    partes_X = partes2(X)
    for subconj in partes_X:
        if sum(subconj) == 5842:
            return subconj
    return

def clase4_ej20(n):
    X = set(range(1,n))
    partes_X = partes2(X)
    contador = 0
    for subconj in partes_X:
        if sum(subconj) % 5 == 0:
            contador += 1
    return contador

#valores_ej20 = []
#for i in range(1,20):
#    valores_ej20.append(clase4_ej20(i))
#print(valores_ej20)
# [1, 1, 1, 2, 4, 8, 14, 26, 52, 104, 208, 412, 
# 820, 1640, 3280, 6560, 13112, 26216, 52432]
# Esta es OEIS A068011
# s(k+1) = 2s(k) if k == 2, 3, or 4 mod 5, 
# 2s(k)-2^(k/5) if k == 0 mod 5, 
# 2s(k)-2^((k-1)/5) if k == 1 mod 5
# Empirical G.f.: -(x^2-x+1)*(2*x^3+2*x^2-1) / ((2*x-1)*(2*x^5-1))   