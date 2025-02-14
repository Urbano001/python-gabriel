playlist = {}
playlist['canciones'] = [] #cree un diccionario

def app(): #funcion principal para el ejercicio 
    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('Como deseas nombrar tu playlist:\n')
    
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist
            agregar_playlist = False #ya tenemos un nombre desactivamos el true
            agregar_canciones()

def agregar_canciones():
    print ('agregando canciones a la playlist:', playlist['nombre'])
while True:
    cancion = input ('Ingresar el nombre de la cancion (o "x" para salir):')
    if cancion.lower() == 'x':

        break  #dejar de agregar canciones

playlist['canciones'].append(cancion)
print ('cancion agregada:', cancion)
print ('playlist completa')
print(playlist)

def eliminar_canciones():
    print('Eliminacion canciones de la playlist:', playlist['nombre'])
while True:
    cancion_eliminar = input ('Ingresa el nombre de la cancion (o "x" para salir):')
    if cancion_eliminar.lower() == 'x':
        break
    if cancion_eliminar in playlist['canciones']:
        playlist['canciones'].remove(cancion_eliminar)
        print('La canción {cancion_eliminar} ha sido eliminada de la playlist.')
    else:
        print('La cancion no se encuentra en la playlist')

print('!Playlist actualizada!')
print(playlist)  

def mostrar_resumen():
    print(f'Playlist: {playlist["nombre"]}')
    print(f'Canciones de la playlist:\r\n')
    for cancion in playlist['canciones']:
        print(cancion)
app()

