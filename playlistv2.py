playlists = {}

def crear_playlist():
    nombre_playlists = input('como deseas nombrar tu playlist')
    playlists[nombre_playlists] = []
    return nombre_playlists

def agregar_cancion(playlist_nombre):
    print ('agregando canciones a la playlist')
    while True:
        cancion = input('Ingresar el nombre de la cancion (o "x" para salir):')
        if cancion.lower() == 'x':
            break
        playlists[playlist_nombre].append(cancion)
        print ('cancion agregada:', cancion)

def eliminar_cancion(playlist_nombre):
    print('Eliminacion canciones de la playlist:', playlist_nombre)w
    while True:
     cancion_eliminar = input ('Ingresa el nombre de la cancion (o "x" para salir):')
     if cancion_eliminar.lower() == 'x':
        break
     if cancion_eliminar in playlists[playlist_nombre]:
        playlists[playlist_nombre].remove(cancion_eliminar)
    else:
       print('La cancion no se encuentra en la playlist')

def mostrar_playlist():
   if not playlists:
    print('No hay playlists creadas')
   else:
      for nombre_playlist, canciones in playlists.item():
         print('Canciones:')
         for cancion in canciones:
            print(f"-{cancion}")

def app():
    while True:
        print("\nMenu:")
        print("1. Crear playlist")
        print("2. Agregar cancion a playlist")
        print("3. Eliminar cancion de playlist")
        print("4. Mostrar playlist")
        print("5. Salir")
    
        opcion = input("Elija una opcion: ")

        if opcion == '1':
            nombre_playlist = crear_playlist()
            agregar_canciones (nombre_playlist)
        elif opcion == '2':
            playlist_nombre = input('A que ')
            if playlist_nombre in playlists:
                agregar_cancion (playlist_nombre)
            else:
                print('La playlist no existe')
        elif opcion == '3':
            playlist_nombre = input('Ingresa el nombre de la playlist: ')
            if playlist_nombre in playlists:
                eliminar_cancion (playlist_nombre)
            else:
                print('La playlist no existe')
        elif opcion == '4':
            mostrar_playlist()
        elif opcion == '5':
            break
        else:
            print("Opcion invalida")

app ()



    
    
