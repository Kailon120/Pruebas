def suma_avanzada():
    x = 0
    while True:
        a = float(input("Ingresa un numero a sumar: "))
        x += a
        
        while True:
            opc = input("¿Quieres sumar otro número? (Y/N): ").upper()
            if opc in ["Y", "N"]:
                break
            print("Opción no válida. Por favor, ingresa Y o N.")
        
        if opc == "N":
            break
    print()
    print(f'Resultado: {x}\n')