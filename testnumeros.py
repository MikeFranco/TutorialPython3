"""los comentarios se rompen
si les pongo acento, hay que evitar esto"""
#esto se rompe los acentos valen verga aqui
x=6
y=9
if x>y:
  print("esto no es cierto")
else:
  print("El 6 no es mayor a 9")

print("esto vale x: ",  x)
print("esto vale y:",  y)

"""tipos de numeros en python:    interger, float y complejos
el complejo se hace asi:"""
z= 3j
x= 1 #interger
y= 4.2 #float
print(type(z))

#se pueden usar exponentes en python poniendo la E para indicar 10^
a = -87.7e-10
print(a)
#transformar el valor dentro de () en el tipo que se le indique antes
x = str(1.55555)
y = int("3")
z = float("3.2324")
print(y)
print(x)
print(z)