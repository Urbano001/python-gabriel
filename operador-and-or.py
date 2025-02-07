acceso_usuario = True
acceso_admin = True
if acceso_usuario or acceso_admin:
    print('Acceso total')
elif acceso_usuario:
    print('El usuario esta autorizado')
else:
    print('Acceso denegado')