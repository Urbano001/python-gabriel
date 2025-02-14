pregunta = input('agregar un numero y te dire si es impar\r\n')
pregunta = '\r\n escribe "cerrar" para salir de la app\r\n'
pregunta = True

while pregunta:
    numero = input("Ingresar un numero (o escribe 'cerrar' para salir) ")
    if numero.lower() == "cerrar":
        break
try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f"El numero es impar")
    else:
        print(f"El numero es par")
except ValueError:
    print("Debes ingresar un numero")