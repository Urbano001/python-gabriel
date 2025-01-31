a = 5
b = 3
igual = a == b
diferente = a != b
mayor = a > b
menor = a < b

#condicional

ahorro = 500
if ahorro >=0:
 print ("Nos vamos de viaje")
else:
 print ("No tenemos dinero para viajar")

#revisamos valores diferentes

lenguaje = 'Python'
if not lenguaje == 'python':
 print (f'SUPER ERES UN CRACK DE {lenguaje}')
else:
 print ("No eres un crack")

#EVALUACION BOOLEAN

usuario_autenticado = True
if usuario_autenticado:
 print ("Usuario autenticado correctamente")
else:
 print ("Usuario no autenticado")

#condicionales con list

superheroes = ['Superman', 'spiderman', 'mujer maravilla', 'hercules']
if 'superman' in superheroes:
 print ('Superman es un superheroe')
else:
 print ('Amas a batman')

 #condicionales anidados

 acceso_usuarios = True
 acceso_admin = False

if acceso_usuarios:
 if acceso_admin:
    print ('acceso total')
    else:
    print ('el usuario no es admin')
else:
 print ('acceso denegado')