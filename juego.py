numero = input('agrega un numero y te dire si es impar\r\n')
numero = int (numero)

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')