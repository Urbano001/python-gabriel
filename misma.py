empresas = ()

def agregar_empresa():
    nombre_empresas = input("Ingresar nombre de la empresa: ")
    empresas[nombre_empresas] = ()
    return nombre_empresas

def agregar_proyecto(nombre_empresas):
    nombre_proyecto = input("Ingresar nombre del proyecto: ")
    while True:
        proyecto = input('Ingresar el nombre del proyecto (o "x" para salir):')
        if proyecto.lower() == 'x':
            break
    empresas[nombre_empresas].append(proyecto)
    print ('proyecto guardado', proyecto)

def eliminar_proyecto(nombre_empresas):
    print('Eliminacion canciones de la playlist:', nombre_empresas)
    while True:
     eliminar_proyecto = input ('Ingresa el nombre de la proyecto (o "x" para salir):')
     if eliminar_proyecto.lower() == 'x':
        break
     if eliminar_proyecto in empresas[nombre_empresas]:
        empresas[nombre_empresas].remove(eliminar_proyecto)
    else:
       print('La cancion no se encuentra en la playlist')
       print('El proyecto no se puede eliminar')

def mostrar_empresas():
   if not empresas:
    print('No hay empresas creadas')
   else:
      for nombre_empresa, proyectos in empresas.item():
         print('proyectos:')
         for proyecto in proyectos:
            print(f"-{proyecto}")

def app():
    while True:
        print("\nMenu:")
        print("1. Crear empresa")
        print("2. Agregar proyecto a empresa")
        print("3. Eliminar proyecto de empresa")
        print("4. Mostrar empresas")
        print("5. Salir")
    
        opcion = input("Elija una opcion: ")

        if opcion == '1':
            nombre_empresas = agregar_empresa()
            agregar_proyecto (nombre_empresas)
        elif opcion == '2':
            nombre_empresas = input('A que ')
            if nombre_empresas in empresas:
                agregar_proyecto (nombre_empresas)   
            else:
                print('La empresa no existe')
        elif opcion == '3':
            playlist_nombre = input('Ingresa el nombre de la empresa: ')
            if nombre_empresas in empresas:
                eliminar_proyecto (nombre_empresas)
            else:
                print('La empresas no existe')
        elif opcion == '4':
            mostrar_empresas()
        elif opcion == '5':
            break
        else:
            print("Opcion invalida")
app()