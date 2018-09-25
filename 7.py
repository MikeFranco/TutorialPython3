"""                                     Arreglos tipo: "Diccionario"
Estos arreglos son NO ordenados, Cambiables e indexados
Este tipo de arreglos se declaran entre llaves {}, como si estuvieras haciendo un JSON
Es importante poner una coma al final de cada linea para separarlas y asi no te mande un error"""

dicci =	{
  "Pelicula": "Star Wars IV",
  "Genero": "Sci-Fic",
  "Año": 1977
}
print(dicci)

"""Para acceder a un valor dentro del diccionario, tienes que poner el nombre de la llave de 
la que quieres obtener su valor
Es importante que pongas tal cual el valor de la llave, si no, te marcara un error

Tambien hay un metodo llamado get() que hace la misma funcion
"""
x = dicci["Pelicula"]
y = dicci.get("Genero")
print(x)
print(y)

"""Para cambiar un valor, debes de hacer referencia a la llave
"""
dicci["Pelicula"] = "Star Wars V"
print(dicci)

"""Puedes hacer un loop en el diccionario para obtener el nombre de todas las llaves.
OJO: Solo es el nombre de las llaves!!!!
"""
for i in dicci:
  print(i)

"""Con este loop imprimes los VALORES de las llaves, cualquiera de los 2 puedes usar"""
print("------------------Con dicci.values()-------------------------")
for i in dicci.values():
  print(i)
print("-------------------------------------------------------------")

for i in dicci:
  print(dicci[i])

"""Imprimes todo lo que hay dentro del diccionario, tanto llaves como valores"""
print("-----------------Se imprime llave y seguido el valor----------")
for i,j in dicci.items():
  print(i,":", j)  

"""Puedes imprimir la longitud del diccionario con len()"""
print("--------------------Longitud del diccionario-----------------")
print(len(dicci))  


"""Puedes agregar llaves nuevas y sus valores declarandolos asi:"""
print("----------------Agregando una llave con su valor--------------")
dicci["Personaje Principal"] = "Luke Skywalker"
print(dicci)


"""Puedes remover alguna llave con el metodo del"""
print("------------------Borrando la llave Genero-------------------------")
del dicci["Genero"]
print(dicci)
"""Tambien puedes borrar el diccionario con este metodo..."""
#del dicci

"""Con el metodo pop() tambien puedes borrar llaves"""
print("--------Borrando item con el metodo pop() Personaje Principal-------")
dicci.pop("Personaje Principal")
print(dicci)


"""con popitem() se borra el ultimo item ingresado 
(en versiones 3.7 en adelante se borra un item al azar)"""
print("----------------borrando con popitem()------------------------")
x = dicci.popitem()
print("Esto es lo que se borra: ",x)
print(dicci)


"""Con el metodo clear() puedes limpiar todo el diccionario"""
print("-------------limpiando el diccionario--------------------------")
dicci.clear()
print(dicci)

"""Con el constructor dict() tambien puedes hacer un diccionario"""
print("-------------Creando el diccionario con dict()-----------------")
dicci = dict(Pelicula = "Star Wars VI", Genero = "Sci-Fi", Año = "1983")
for i,j in dicci.items():
  print(i,":", j)  


"""Metodos que puedes usar en tu diccionario
clear()	copy()	fromkeys()	get()	items()	keys()	pop()	popitem()	setdefault() update()  values()

"""
eje = {
  "Marca" :"Chevrolet",
  "Modelo":"Corvette",
  "Año"   : 1954
}

"""Metodo fromkeys()
Puedes crear llaves a partir de una variable
Hay que destacar que si usas una segunda variable para agregar valores (en este caso y),
se agregaran a todas las llaves que tu ingreses
"""
print("----------------Agregando llaves con fromkeys()---------------")
x = ("llave1", "llave2", "llave3")
y = ("valor1")
eje2 = dict.fromkeys(x,y)
print(eje2)


