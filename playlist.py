playlist = {}
playlist['canciones'] = []

def app():
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar tu playlist:\n')
    
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False
            agregar_canciones()

def agregar_canciones():
    print ('agregando canciones a la playlist:', playlist['nombre'])
while True:
    cancion = input ('Ingresar el nombre de la cancion (o "x" para salir):')
    if cancion.lower() == 'x':
        break
playlist['canciones'].append(cancion)
print ('cancion agregada:', cancion)
print ('playlist completa')
print(playlist)

def eliminar_canciones:
print('Eliminacion canciones de la playlist', playlist['nombre'])
while True:
    cancion_eliminar = input ('Ingresa el nombre de la cancion (o "x" para salir):')
    if cancion_eliminar.lower() == 'x':
        break

