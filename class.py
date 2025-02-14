class Restaurant():
    def agregar_restaurant(self,nombre):
        self.nombre = nombre
        print (f"agregar restaurante")
    def mostrar_informacion(self):
        print (f"el nombre del restaurante agregado es: {self.nombre}")

#intanciar la clase

restaurante = Restaurant()
restaurante.agregar_restaurant("El Café del Sol")
restaurante.mostrar_informacion()

#en esta clase se crea un método para agregar restaurantes y otro para mostrar la información del restaurante agregado.

#puedo crear diferentes objetos usando una misma clase

restaurante2 = Restaurant()
restaurante2.agregar_restaurant("La Parrilla del Sol")
restaurante2.mostrar_informacion()

#esto generará dos restaurantes diferentes con su información mostrada en pantalla.

#imprimir los objetos

print(f"el nombre del restaurante es:' {restaurante.nombre}")

print(f"el nombre del restaurante es:' {restaurante2.nombre}")





class carro:
    def _init_(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        
    def encender (self):
        self.encender = True
        print("El carro {self,marca} esta encendido")

    def apagar (self):
        self.encender = False
        print("El carro {self,marca} esta apagado")
    
    def apagar (self):
        self.enceder = False
        print("El carro esta apagado")

    def acelerar(self):
        if self.encender:
            print("El carro esta acelerando")
        else:
            print("El carro esta apagado, no se puede acelerar")

mi_carro = carro ("Ford", "Mustang", "Rojo")

print(mi_carro.marco)

mi_carro.encender

mi_carro.acelerar()
        







