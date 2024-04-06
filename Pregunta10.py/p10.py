class circulo:  
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.radio**2 * 3.1415

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return self.largo * self.ancho

def calcular_area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = circulo(radio)
    print("El área del círculo es:", circulo.area())

def calcular_area_rectangulo():
    largo = float(input("Ingrese el largo del rectángulo: "))
    ancho = float(input("Ingrese el ancho del rectángulo: "))
    rectangulo = RECTANGULO(largo, ancho)
    print("El área del rectángulo es:", rectangulo.area())

def calcular_area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    cuadrado = RECTANGULO(lado, lado)
    print("El área del cuadrado es:", cuadrado.area())

def menu():
    while True:
        print("\nMenú:")
        print("1. Calcular el área de un círculo")
        print("2. Calcular el área de un rectángulo")
        print("3. Calcular el área de un cuadrado")
        print("4. Salir")
        
        opcion = input("Ingrese su opción: ")
        
        if opcion == '1':
            calcular_area_circulo()
        elif opcion == '2':
            calcular_area_rectangulo()
        elif opcion == '3':
            calcular_area_cuadrado()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()