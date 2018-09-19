"""                                               Tuple(Tupla)
Son arreglos ORDENADOS y NO MUTABLES, esto quiere decir que una vez que has creado el arreglo
no puedes modificar sus valores como lo hacías en las "Listas" usando metodos.
A diferencia de las listas, las tuplas las declaras usando parentesis()
"""

estatupla = ("python", "es", "genial")
print(estatupla)

#Para acceder a algun objeto dentro de la tupla, es como todos los demas arreglos...
print(estatupla[0])

#Si quieres modificar un elemento, al hacer esto no se sobreescribira y se mantendra igual, de hecho, te manda error xD
#estatupla[1] = "grandioso"
#print(estatupla)

"""       Loops en Tupla
Como todo arreglo, puedes imprimir cada item por separado con un for..."""
for i in estatupla:
  print(i)

#Tambien puedes imprimir la longitud de las Tuplas
print(len(estatupla))

""" ELiminar una Tupla
Puedes eliminar una Tupla completa, pero no los elementos que hay dentro de ella, ya que las Tuplas no pueden cambiar
"""
#del estatupla
#print(estatupla) #esto es un error, porque la tupla ya no existe

"""                                 Constructor Tupla
tuple() sirve para construir una tupla e indicar que es una tupla si se deja en blanco
Parametros:
Opcional: puedes dejar en blanco lo que hay despues de los parentesis para indicar que esa variable es una tupla
Opcional: puedes agregar otros parentesis para agregar otra tupla(?)
"""

tutupla = tuple()
constupla = tuple(("probando", "constructor", "tupla"))
print(type(tutupla))
print (constupla)











