def menu_principal():
    print("----------------------------------------------------------------")
    print("|                      Menu Principal                          |")
    print("|                 1. Construir conjuntos                       |")
    print("|                 2. Operar conjuntos                          |")
    print("|                 3. Finalizar programa                        |")
    print("----------------------------------------------------------------")
    opcion = input("Selecciona una opción: ")
    return opcion

def mostrar_menu_operaciones():
    print("----------------------------------------------------------------")
    print("                   Operaciones disponibles:                     ")
    print("                      1. Complemento                            ")
    print("                        2. Unión                                ")
    print("                    3. Intersección                             ")
    print("                     4. Diferencia                              ")
    print("                 5. Diferencia Simétrica                        ")
    print("               6. Regresar al menú principal                    ")
    print("----------------------------------------------------------------")
    opcion = input("Selecciona una operación: ")
    return opcion


def main():
    while True:
        opcion = menu_principal()



main()    