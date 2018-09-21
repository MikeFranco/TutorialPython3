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
print("------------------Borrando una llave-------------------------")
del dicci["Genero"]
print(dicci)