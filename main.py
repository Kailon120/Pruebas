import suma
import resta
import multiplicacion
import dividir
import suma_avanzada



def menu():
    print("Selecciona la operación a realizar\n")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- Dividir")
    print("5.- Suma avanzada")
    print("6.- Salir")
    
print("-----------------------------------")
print("----Bienvenido a tu calculadora----")
print("-----------------------------------\n")

while True:
    menu()
    opc = int(input("R: "))

    match opc:
        case 1:
            suma.suma()
        case 2:
            resta.resta()
        case 3:
            multiplicacion.multiplicacion()
        case 4:
            dividir.dividir()
        case 5:
            suma_avanzada.suma_avanzada()
        case 6:
            break


