nombre = input('cual es tu nombre?\r\n')
print (f'tu nombre es {nombre}')

edad = input('cual es tu edad?')
edad = int(edad)

if edad >= 18:
    print ('eres mayor de edad')
else:
    print ('eres menor de edad')


nombre = input('cual es tu nombre?')
print (f'tu nombre es {nombre}')

edad = input('cual es tu edad?')
try:
    edad = int(edad)
    if edad >= 18:
        print (f'eres mayor de edad')
    else:
        print (f'eres menor de edad')
except ValueError:
    print ('error aprende a programar >3')