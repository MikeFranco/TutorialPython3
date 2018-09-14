"""                     Arreglos
Hay 4 tipos de arreglos en Python:
  -Listas: es un arreglo que es ordenado y mutable. Permite duplicar a los miembros del arreglo
  -Tuple: es un arreglo ordenado y NO mutable. Permite duplicar a los miembros del arreglo
  -Set: es un arreglo NO ordenado y NO indexado. NO permite duplicar a los miembros del arreglo
  -Diccionario: arreglo NO ordenado, cambiable y NO indexado, NO se pueden duplicar los miembros
"""

"""Arreglos de Lista"""

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