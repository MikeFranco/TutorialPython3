x = "esto es un string"
y = '      .esto tambien es un string.      '
z = "ESTO ESTA EN MAYUSCULAS"
a = "esto esta en minusculas"
print(x + y)

print(x[1])
#sirve para escoger las letras dentro de la cadena de caracteres pero
#no se incluye el ultimo
print(x[2:6])
#strip() borra los espacios antes y despues de la cadena
print(y.strip())
#len() imprime el largo del string, como todos los demas
print(len(y))
#lower imprime todo el string  en minuscula
print(z.lower())
#upper lo mismo que lower pero a mayuscula
print(a.upper())
#replace cambia una letra por otra (letra del string, letra a la que se va a cambiar)
print(x.replace("e", "E"))
#split divide el string si se encuentra un separador
b = "esto es 1, .esto es 2"
print(b.split("."))
#ingresar unn string desde la consola
print("Ingresa tu nombre: ") 
x = input()
print("Hola, " + x)