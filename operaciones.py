"""Operaciones en Python"""
x = 2
y = 5
print("X = ",x, "\nY = ",y)
#Adicion
z = x+y
print("Suma x + y = ",z)
#Sustraccion
a = x-y
print("Resta x - y = ",a)
#Division
b = x / y
print("Division x / y = ",b)
#Multiplicacion
c = x * y
print("Multiplicacion x * y = ",c)
#Modulo
d = x % y
print("Modulo x % y = ",d)
#Exponentes
e = x ** y
print("Exponente x ** y = ",e)
#Floor Division
f = x // y
print("no se que sea esto x // y = ",f)

"""Operadores de comparacion"""

#Igual
x == y
#No igual
x != y
#Mayor que
x > y
#Menor que
x < y
#Menor igual/ mayor igual
x <= y / x >= y 

"""Operadores logicos
Son usados para combinar enunciados condicionales"""
#And. Regresa verdadero si los 2 enunciados son verdaderos
x < 5 and x < 10
#OR. Regresa verdadero si al menos 1 de los enunciados es verdadero
x < 5 or x < 10
#Not. Invierte el resultado, si es falso la salida es verdadera y viceversa
not(x < 5 and x < 10)


"""Los siguientes operadores son usados para arreglos"""
h  = ["laptop", "inteligencia artificial", "y"]
i  = ["laptop", "manzana", "celular"]


"""Operadores de identidad
Son usados para comparar objetos no si son iguales, pero son el mismo objeto
con la misma ubicacion de memoria"""
#is. regresa verdadero si ambas variables son el mismo objeto
h is i
#is not. Regresa verdadero si ambas variables no son el mismo objeto
h is not i
print("el arreglo h no esta en i?",h is not i)

"""Operadores de Afiliacion
Usados para probar si la secuencia presentada es un objeto"""
#in. Regresa verdadero si la secuencia con el valor especificado esta presente en el objeto
h in i
print(i in h)



