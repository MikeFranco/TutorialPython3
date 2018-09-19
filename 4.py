

"""Arreglos de Lista
Son arreglos ordenados y mutables. Permiten duplicar a los miembros del arreglo
Este tipo de arreglos se declaran entre corchetes []
"""

estalista = ["manzana", "computadora", "pera"]
print(estalista)#imprime toda la lista
print(estalista[2])#imprime la posicion 2 del arreglo
estalista[1] = "kiwi" #cambia el valor en la posicion 1 del arreglo
print(estalista) 

#Agregar valores al arreglo
for i in estalista:
  print(i) #imprime en forma de lista el arreglo
estalista.append("frutas")#agrega un valor al final de la lista
estalista.insert(1, "naranja")#inserta en el lugar 1, se recorren todos los valores dentro del arreglo
print(estalista)
print(len(estalista))#imprime la longitud del arreglo

#Eliminar valores al arreglo
estalista.remove("manzana")#elimina el valor indicado
estalista.pop()#si no se especifica, se elimina el ultimo valor del arreglo
print(estalista)
del estalista[0] #borra el lugar especificado

#del estalista #borra la lista completa
print(estalista)#se marcaria como error ya que la lista se borro en la linea anterior, si se descomenta
estalista.clear()#limpia la lista, pero sigue existiendo
print(estalista)


estalista.insert(0, "frutas")
print(estalista)
x = estalista.copy()#copia la lista en otra variable
print(x)




"""Métodos que se pueden usar con las listas:
Mencionare todos los metodos que puedes usar, solo como recordatorio y que parametros requieren """
#estare ocupando estas listas para mostrar todos los metodos:

cars= ["BMW", "Mercedez Benz", "Volkswagen", "Aston Martin", 5j, 14]
puntos=[1,2,3,4,1,2,3,5,8,1,2,7,8,1,6]


#sort()   organiza la lista por orden alfabetico
#nombredelalista.sort(reverse = True, key=mifuncion)    esta es la sintaxis para el metodo
"""                                 Sort

Parametros para sort:
Opcionales los 2:
reverse=True: va a organizar la lista en orden descendente, por default esta en false que es ascendente
key=mifuncion: puedes crear una funcion para organizar la lista y la puedes mandar a llamar aqui

Un ejemplo de funcion que puedes usar:

def mifuncion(e):
  return len(e) #ordena cada elemento de la lista dependiendo de su longitud
cars.sort(key=mifuncion)
print(cars)

"""


"""                                 Reverse
Ordena la lista de atras hacia adelante
Parametros:
No requiere ningun parametro

Syntaxis:
cars.reverse()
print(cars)

"""
"""                                 Remove
Elimina un tipo de variable

Parametros para Remove:
Obligatorio: El objeto dentro de la lista que quieras eliminar

Syntaxis:
cars.remove(5j)
print(cars)
"""


"""                                 Pop
Elimina un objeto en un lugar especifico, tambien puede regresar el valor removido

Parametros:
Obligatorio: La posicion dentro de la lista que quieras eliminar

Syntaxis
cars.pop(5)
print(cars)
"""

"""                                 Insert
Ingresa un objeto a la lista en la posicion deseada
Parametros:
Obligatorio: La posicion en donde se ingresara el objeto
Obligatorio: El objeto que se agregara

Syntaxis:
cars.insert(2, "Honda")
print(cars)
"""

"""                                 Index
Regresa la posicion del objeto mencionado
Parametros:
Obligatorio: El elemento del que se quiere obtener su posicion

En este metodo hay que agregar una variable para que se guarde el valor de la posicion del objeto
Syntaxis:
a = cars.index("BMW")
print(a)
"""

"""                                   Extend
Puedes fusionar arreglos con este metodo, al agregarlos al 1er arreglo, el 2do arreglo se agrega al final
Parametros:
Obligatorio: el arreglo que vas a agregar

Syntaxis:
celulares = ["OnePlus", "Xiaomi", "Samsung"]
cars.extend(celulares)
print(cars)
"""

"""                                       Count
Cuenta la cantidad de objetos si mismo que hay en el arreglo
Parametros:
Obligatorio: El objeto que se quiere contar

Syntaxis:
b = puntos.count(1)
print(b)
"""

"""                                         Copy
Copia el arreglo en otra variable
Parametros:
Sin parametros

Syntaxis:
c = cars.copy()
print(c)
"""

"""                                             Clear
Limpia todos los elementos de la lista, solo elimina los elementos, el arreglo sigue en la memoria pero esta vacio
Parametros:
Sin Parametros

Syntaxis:
puntos.clear()
print(puntos)
"""

"""                                              Append
Agrega un elemento o arreglo al final  de la lista
Parametros:
Obligatorio: Elemento que se va a agregar al arreglo

Syntaxis:
cars.append("Hyundai")
cars.append(puntos)
print(cars)
"""
