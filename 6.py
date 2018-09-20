
"""                        Arreglos tipo "Set"
Estos son arreglos NO ordenados y NO indexados. NO permite duplicar a los miembros del arreglo
Los arreglos set se declaran entre llaves {}"""

elset = {"java", "c++", "javascript", "Rubi"}
print(elset)

""" Acceder a un item en un arreglo Set
Como los set son no indexados, no puedes acceder a un item por su posicion en el arreglo
para ver cada item, debes de iterarlos con un for
"""
for i in elset:
  print(i)

"""Puedes ver si un item esta en el set mandandolo a llamar asi:"""
print("java" in elset) #imprime True
print("c" in elset) #imprime False

"""Una vez que has creado un set, no puedes cambiar items, pero si puedes agregar nuevos
Los items que quieras añadir son agregados al inicio de la 
con add agregas un solo item
con update agregas varios items al mismo tiempo
"""
elset.add("sql")
elset.update(["Python", "Pascal", "Assembly"])#es importante que pongas los corchetes para que funcione el metodo
print(elset)

"""Tambien puedes saber la longitud de los arreglos set con len()"""
print(len(elset))


"""Para eliminar un elemento, puedes usar .remove() .discard() o .pop()
remove y discard hacen lo mismo, eliminan el item que tu les asignes
pop elimina siempre el ultimo elemento del arreglo, pero al ser no ordenado, no se sabe con certeza cual es,
  por lo cual tambien este metodo tambien regresa el valor que se elimino
en el caso de que el elemento no exista, la linea aparecera con error y no compilara el codigo"""

elset.remove("Assembly")
print(elset)
elset.discard("sql")
print(elset)
x = elset.pop()
print(x)
print(elset)

"""Tambien puedes limpiar el set con .clear()
o puedes eliminarlo por completo con del, si hace esto, al querer imprimir el arreglo mandara un error porque ya no existe"""
elset.clear()
#del elset
print(elset)


"""El constructor set
set() sirve para construir un arreglo set e indicar que es un set si se deja en blanco
Parametros:
Opcional: puedes dejar en blanco lo que hay despues de los parentesis para indicar que esa variable es un set
Opcional: puedes agregar otros parentesis para agregar otro set(?), es importante que uses dobles parentesis
  para agregar otro set, por que si no, no funcionara el metodo"""

esteset2 = set(("hp", "sony", "asus"))
print(esteset2)





set1 = {"computadora", "focos", "lamparas", "extensiones"} 
set2 = {"computadora", "escritorio", "plumas", "extensiones"}

"""                 Otros metodos que puedes ocupar con set         

asi como en listas, tambien puedes usar los metodos add, copy, clear discard, remove y pop
por comodidad y para no hacer mas largo el codigo, favor de checar la sintaxis y su funcion en el archivo 4.py :D"""



"""                                   Difference
Regresa los valores que solo esten en set1 y no en set2
Parametros:
  Obligatorio: Crear una variable para agregar el/los valor(es) que sean diferentes
"""
a = set1.difference(set2)
print(a)
b = set2.difference(set1)
print(b)
#Como te puedes dar cuenta, se imprimen 2 cosas diferentes, ya que estas comparando primero el set1 con set2
#y luego se compara el set2 con el set1 y cada uno tiene objetos diferentes


