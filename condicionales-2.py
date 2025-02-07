#condisional el if ifel else

tipo = 'estudiante'

if tipo == 'estudiante':
    print('Tienes un descuento del 50%')
elif tipo=='profesor':
    print('Tienes un descuento del 75%')
elif tipo=='invitado':
    print('tienes un descuento del 10%')
else:
    print('No tienes un descuento')

usuario = 'romanlg'
tipousuario = 'admin'
tiposusuarios = ['admin','superadmin','usuario']

if usuario in tiposusuarios and usuario == 'romanlg':
    print (f'puedes entrar {tiposusuarios}')
else:
    print('No puedes entrar')