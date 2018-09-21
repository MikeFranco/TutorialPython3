
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




#Estos sets son los que ocupare para los metodos
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



"""                             Difference_update
El metodo quita los elementos que esten repetidos en ambos sets, difference_update y difference son diferentes.
El metodo Difference regresa un nuevo set,  sin los items no buscados,
y difference_update() remueve los items no buscados del set original
"""
#En este caso, no debes de agregar una variable ya que se sustituye en la original
#set2.difference_update(set1)
print(set2)


"""                             Intersection
El metodo interseccion regresa un set que contiene los items similares entre 2 o mas sets.
Parametros:
Obligatorio: crear una variable que almacene el set resultante de la interseccion
Obligatorio: el set que se va a comparar
Opcional: para comparar mas de un set, simplemente separas el nombre de cada uno con un a coma ","
"""
result = set1.intersection(set2)
print(result)

"""                             Intersection_update
El metodo intersection_update remueve los items que no estan presentes en ambos sets
(o en todos los sets si la comparacion se hace entre mas de 2 sets)
Al igual que difference_update(), la interseccion se sobreescribira sobre el set que estes comparando
"""
#set1.intersection_update(set2)
#print(set1)

"""                                   IsDisJoint
El metodo isdisjoint() regresa True si ninguno de los items esta presente en ambos sets
regresa False en caso contrario
Parametros:
Obligatorio: debes de crear una variable para almacenar la respuesta del metodo
"""
set3= {"a","ver", "al", "cine"}
z = set1.isdisjoint(set3)
#print(z)


"""                                     IsSubSet
El metodo issubset regresa True si todos los items en el ser existen en el otro set especificado,
Regresa False en caso contrario
Es importante remarcar que primero pones el set que creas que es subconjunto (por llamarlo de alguna forma)
y despues pones al set universo
"""
set4 = {"computadora"}
d = set4.issubset(set1)
#print(d)


"""                                         IsSuperSer
El metodo issuperset() regresa True si todos los items del set especificado existen en el original
Este metodo es el contrario a IsSubSet, primero declaras el universo y luego el set que tiene al menos
un elemento del universo
"""
z = set1.issuperset(set4)
#print(z) 


"""                                     Symmetric_Difference
Este metodo symmetric_difference() regresa un ser que contiene a todos los elementos de ambos sets,
pero no lo elementos presentes en ambos, esto quiere decir que
se crea un set con los elementos que tengan diferentes de los que se esten comparando.
"""
#recuerda que no se imprimiran en un orden ya que los sets son no indexados
sym = set1.symmetric_difference(set2)
print(sym)

"""                                     Symmetric_Difference_Update
Este metodo symmetric_difference_update() actualiza al set original quitando los elementos
que esten en ambos sets e insertando los que falten
recuerda que en todos los metodos que tengan update, actualiza al set que usas primero,
no debes de crear una variable para almacenar los datos...
"""
#set1.symmetric_difference_update(set2)
#print(set1)


"""                                        Union
El metodo union() regresa un set que contiene a todos los items del original y todos los items de los sets especificados
puedes especificar los sets que tu quieras, solo separalos por comas ","
Si el item aparece en mas de 1 set, se reemplazara y solo aparecera 1 sola vez en el nuevo set
"""

uni = set1.union(set2, set3, set4)
print(uni)


"""                                     Update
update() actualiza el set actual, agregandole items de otro set
Si un item esta presente en ambos, solo aparecera una vez
"""
set1.update(set2)
print(set1)

