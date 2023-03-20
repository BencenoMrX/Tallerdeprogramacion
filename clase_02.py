##############################################################################
##############################################################################
# Clase 2 - Taller de programación: sucesiones
##############################################################################
##############################################################################

##############################################################################
# Ejemplos de sucesiones como funciones
##############################################################################
"""
def numeroE(n):
    return (1+1/n)**n

def armonica(n):
    sumandos = [1/k for k in range(1,n+1)]
    return sum(sumandos)

# Ejercicios:

# Definir factorial
def factorial(n):
    if n==0 or n == 1:
        return 1
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    return fact

# Casos de ejemplo
print(factorial(0), factorial(1), factorial(2), factorial(7))

# Hallar el primer n tal que la sucesión dada por la serie 
# armónica dé mayor a 10 y a 12. Medir el tiempo transcurrido.

import time
    
def test_armonica(valor):
    # Testea si la armónica da menor a un valor y cuando no,
    # devuelve el n
    N = 1
    while armonica(N) < valor:
        N += 1
    return N

def test_armonica_mejor(valor):
    # Uso que en realidad puedo ir sumando el último término
    # para no tener que hacer las N sumas todas las veces
    N = 1
    arm = 1
    while arm < valor:
        N += 1
        arm += 1/N
    return N

start10 = time.time()
print(test_armonica(10))
print(time.time()-start10)
# N = 12367
# Tiempo = 7.3554 s

start_mejor10 = time.time()
print(test_armonica_mejor(10))
print(time.time()-start_mejor10)

# N = 12367
# Tiempo = 0.0020 s

start_mejor12 = time.time()
print(test_armonica_mejor(12))
print(time.time()-start_mejor12)

# N = 91380
# Tiempo = 0.3800 s
# (con el mejor algoritmo)

##############################################################################
# Sucesiones como parámetros
##############################################################################

# Ejemplo
def ceros(a,n0,n1):
    # Devuelve los n entre n0 y n1 tales que a vale 0
    # Debe ser n0 <= n1
    return [n for n in range(n0,n1) if a(n)==0]

# Ejercicios:

# Definir una funcion alInfinito que dada una sucesión no acotada 
# superiormente devuelva el primer n tal que a_n > M, M > 0 dado

def alInfinito(a,M):
    # Empieza en 1 porque es una sucesión en los naturales
    contador = 1
    
    # Acá convendría ponerle una condición de terminación
    # al while
    
    maximo = 1e6
    while a(contador) <= M and contador < maximo:
        contador += 1
    
    if contador == maximo:
        return
    
    return contador

def minimo(a, n0, n1):
    # Busca el n0 <= n < n1 tal que a(n) sea mínimo. Sólo me piden
    # un valor, no todos los posibles
    if n0 > n1:
        return 'n0 tiene que ser menor que n1'
    
    minimo_n = n0
    minimo_valor = a(n0)
    for i in range(n0,n1):
        if a(i) < minimo_valor:
            minimo_n = i
            minimo_valor = a(i)
    
    return minimo_n

# Probamos las funciones

def sucesion_cubica(n):
    return (n-4)**3 - 10*(n-4)**2 + 2*(n-4) + 9


print(alInfinito(sucesion_cubica,200))
# n = 16
print(alInfinito(sucesion_cubica,0))
# n = 4

print(minimo(sucesion_cubica, 1,5))
# n = 1
print(minimo(sucesion_cubica, 5,20))
# n = 11

##############################################################################
# Sucesiones como output
##############################################################################

def suma(a,b):
    # Devuelve la sucesión obtenida de sumar término a término a y b
    def c(n):
        return a(n)+b(n)
    
    return c

# Ejemplo
def sucesion_cubica(n):
    return (n-4)**3 - 10*(n-4)**2 + 2*(n-4) + 9

def sucesion_cuadratica(n):
    return n**2 - 6*n + 14

suma_sucesiones = suma(sucesion_cubica,sucesion_cuadratica)

# Ejercicios:

# Definir una función serie que tome la sucesion a_n y devuelva la sucesión
# obtenida por la suma de los términos de k=1 hasta n

def serie(a):
    def suma_de_a(n):
        suma = 0
        for i in range(1,n+1):
            suma += a(i)
        return suma
    return suma_de_a

# Ejemplo

def sucesion_inversa_pot_de_2(n):
    return 1/(2**n)

serie_inversa_pot_de_2 = serie(sucesion_inversa_pot_de_2)

print(serie_inversa_pot_de_2(10))

print(type(serie_inversa_pot_de_2))

# Definir exponencial que dado x devuelva una sucesión que converja a exp(x)

# Definir factorial
def factorial(n):
    if n==0 or n == 1:
        return 1
    fact = 1
    for i in range(2,n+1):
        fact = fact*i
    return fact

def exponencial(x,n):
    suma = 1
    for i in range(1,n+1):
        suma += x/factorial(i)
    # Se puede hacer con el método serie:
    # def taylor_exp(x,n):
    #     return x/factorial(n)
    # return serie(taylor_exp)
    return suma

print(exponencial(0,10))
print(exponencial(1,10))

import math
print(math.e)
   

##############################################################################
# Algoritmo de Newton Raphson
##############################################################################

# Dada una función f, su derivada g, un punto inicial x_0 y un número n_max
# devuelve los n_max términos de la sucesión
# x_n - f(x_n)/g(x_n)

import math

def newtonR(f,g,x_0,n_max):
    sucesion = [x_0 - f(x_0)/g(x_0)]
    for i in range(1,n_max):
        x_n = sucesion[-1]
        sucesion.append(x_n - f(x_n)/g(x_n))
    return sucesion

def f1(x):
    return x**2

def f1_prima(x):
    return 2*x

print(newtonR(f1,f1_prima,3,10))

# Aproximar raíz de 2
# Uso la función x^2-2

def f2(x):
    return x**2-2

def f2_prima(x):
    return 2*x

print(newtonR(f2,f2_prima,3,10))
print(math.sqrt(2))

# Al 6to paso ya converge al valor que muestra math.sqrt

# Comparar la velocidad de la convergencia con otra función

def f3(x):
    return (x**2-2)**2

def f3_prima(x):
    return 2*(x**2-2)*2*x

print(newtonR(f2,f2_prima,3,10))
print(newtonR(f3,f3_prima,3,10))
print(math.sqrt(2))

# Converge más lento con esta segunda función

# Algoritmo con tolerancia
def newtonR_tol(f,g,x_0,n_max,eps):
    sucesion = [x_0 - f(x_0)/g(x_0)]
    for i in range(1,n_max):
        x_n = sucesion[-1]
        sucesion.append(x_n - f(x_n)/g(x_n))
        if abs(sucesion[-1] - sucesion[-2]) < eps:
            return sucesion
    return sucesion

print(newtonR_tol(f2,f2_prima,3,10,1e-5))
print(math.sqrt(2))

# OJO con cómo calculamos raíces de números negativos

from scipy.special import cbrt

def f4(x):
    return cbrt(x)

def f4_prima(x):
    # 1/3*(x**(-2/3)) genera conflicto
    return 1/(3*cbrt(x)**2)

def f4_prima2(x):
    # O si no separando en casos
    if x>0:
        return 1/3*(x**(-2/3))
    elif x<0:
        return -1/3*1/((-x)**(2/3))

f4_prima2(-64.0)
f4(-64.0)

print(newtonR(f4,f4_prima2,-64.0,10))

##############################################################################
# Algoritmo de bisección
##############################################################################
    
def biseccion(f,a,b,n_max):
    if a>=b or f(a)*f(b) > 0:
        return
    elif f(a) == 0:
        return [a]
    elif f(b) == 0:
        return [b]
    else:
        sucesion = []
        sucesion.append([a,b])
    
        for i in range(1,n_max):
            c = (sucesion[-1][0]+sucesion[-1][1])/2
            if f(c) == 0:
                sucesion.append([sucesion[-1][0],c])
                return sucesion
            elif f(a)*f(c) < 0:
                sucesion.append([sucesion[-1][0],c])
            else:
                sucesion.append([c,sucesion[-1][1]])
                
        return sucesion
    
print(biseccion(f4,-2,7,10))

print(biseccion(f2,1,7,10))
# Converge más lento que NR

def biseccion_tol(f,a,b,n_max,eps):
    if a>=b or f(a)*f(b) > 0:
        return
    elif f(a) == 0:
        return [a]
    elif f(b) == 0:
        return [b]
    else:
        sucesion = []
        sucesion.append([a,b])
    
        for i in range(1,n_max):
            if abs(sucesion[-1][0]-sucesion[-1][1]) < eps:
                return sucesion
            
            c = (sucesion[-1][0]+sucesion[-1][1])/2
            if f(c) == 0:
                sucesion.append([sucesion[-1][0],c])
                return sucesion
            elif f(a)*f(c) < 0:
                sucesion.append([sucesion[-1][0],c])
            else:
                sucesion.append([c,sucesion[-1][1]])
                
        return sucesion

print(biseccion_tol(f2,1,7,50,1e-4))

# Hallar con error a lo sumo 1e-5, todas las raíces de
# x^5-11x^3+14x^2-2
# f tiene a lo sumo 5 raíces, y por lo menos 1 real

def f5(x):
    return x**5-11*x**3+14*x**2-2

def f5_prima(x):
    return 5*x**4-33*x**2+14*x

# Pruebo a ver qué onda

import numpy as np

tabla_de_valores_f5 = [f5(x) for x in np.arange(-10,10.5, 0.5)]
tabla_de_valores_f5_prima = [f5_prima(x) for x in np.arange(-10,10.5, 0.5)]

print(tabla_de_valores_f5)

# Entre -4 y -3.5 cambia de signo. 
# Entre -0.5 y 0
# Entre 0 y 0.5
# Entre 1 y 1.5
# Entre 2 y 2.5

print(sum(biseccion_tol(f5,-4,-3.5,500,1e-5)[-1])/2)
print(sum(biseccion_tol(f5,-0.5,0,500,1e-5)[-1])/2)
print(sum(biseccion_tol(f5,0,0.5,500,1e-5)[-1])/2)
print(sum(biseccion_tol(f5,1,1.5,500,1e-5)[-1])/2)
print(sum(biseccion_tol(f5,2,2.5,500,1e-5)[-1])/2)

#[-3.82427978515625, -3.8242721557617188]
#[-0.3365020751953125, -0.33649444580078125]
#[0.474334716796875, 0.47434234619140625]
#[1.4954833984375, 1.4954910278320312]
#[2.1909332275390625, 2.1909408569335938]

#-3.8242759704589844
#-0.3364982604980469
#0.4743385314941406
#1.4954872131347656
#2.190937042236328

"""
##############################################################################
# Subsucesiones
##############################################################################

# Ejemplo

def subsucPositivos(a,kmax):
    # Calcula los primeros k_max índices de la subsucesión de 
    # valores positivos de a
    
    res = []
    ks = 0
    n = 1
    while ks < kmax:
        if a(n) > 0:
            res.append(n)
            ks += 1
        n += 1
    return res

# Si una sucesión no es acotada, para toda otra sucesión que tienda a
# infinito existe una subsucesión de la primera que la mayora. Se dice
# que a diverge al menos como b. Ídem si b tiende a cero, se dice que
# a tiende a 0 al menos como b.
    
def subsucDivergente(a,b,k_max):
    res = []
    ks = 0
    n = 1
    while ks < k_max:
        if abs(a(n)) > b(n):
            res.append(n)
            ks += 1
        n += 1
    return res

def subsucACero(a,b,k_max):
    res = []
    ks = 0
    n = 1
    while ks < k_max:
        if abs(a(n)) < b(n):
            res.append(n)
            ks += 1
        n += 1
    return res

# Ejercicio 2
import math

def coseno(n):
    return math.cos(n)

def inverso(n):
    return 1/n

print(subsucACero(coseno,inverso,100))
