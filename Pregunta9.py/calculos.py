import operaciones

def main():
    print("Suma:", operaciones.suma(5, 3))
    print("Resta:", operaciones.resta(10, 4))
    print("Producto:", operaciones.producto(6, 7))
    print("División:", operaciones.division(8, 2))

    # Manejo de errores
    print("División por cero:", operaciones.division(10, 0))
    print("Tipo de dato no válido:", operaciones.suma(5, '3'))

if __name__ == "__main__":
    main()