"""
    MENU PRINCIPAL DEL PROYECTO
"""

def menu_principal():
    print("----------------------------------------------------------------")
    print("|                        Proyecto 01                           |")
    print("----------------------------------------------------------------")
    print("|                      Menu Principal                          |")
    print("|                 1. Construir conjuntos                       |")
    print("|                 2. Operar conjuntos                          |")
    print("|                 3. Finalizar programa                        |")
    print("----------------------------------------------------------------")
    opcion = input("Selecciona una opción: ")
    return opcion

"""
    MENU DE LAS OPERACIONES ENTRE CONJUNTOS
"""

def mostrar_menu_operaciones():
    print("----------------------------------------------------------------")
    print("|                   Operaciones disponibles:                   |")
    print("|                      1. Complemento                          |")
    print("|                      2. Unión                                |")
    print("|                      3. Intersección                         |")
    print("|                      4. Diferencia                           |")
    print("|                      5. Diferencia Simétrica                 |")
    print("|                      6. Regresar al menú principal           |")
    print("----------------------------------------------------------------")
    opcion = input("Selecciona una operación: ")
    return opcion

def crear_conjuntos():
    conjunto = []
    elementos = input("Ingresa los elementos del conjunto (letras A-Z, dígitos 0-9) separados por comas: ").upper().split(',')
    for elemento in elementos:
        elemento = elemento.strip()
        if elemento.isalnum() and len(elemento) == 1 and elemento not in conjunto:
            conjunto.append(elemento)
        else:
            print(f"Elemento inválido o duplicado: {elemento}. Se omitirá.")
    return conjunto

def crear_conjunto_universo():
    return 0;
    

def complemento(conjunto, universo):
    conjuntoComplemento = []
    for elemento in universo:
        if elemento not in conjunto:
            conjuntoComplemento.append(elemento)
    return conjuntoComplemento

def union(conjunto1, conjunto2):
    conjuntoUnion = conjunto1[:]
    for elemento in conjunto2:
        if elemento not in conjuntoUnion:
            conjuntoUnion.append(elemento)
    return conjuntoUnion

def interseccion(conjunto1, conjunto2):
    conjuntoInterseccion = []
    for elemento in conjunto1:
        if elemento in conjunto2:
            conjuntoInterseccion.append(elemento)
    return conjuntoInterseccion

def diferencia(conjunto1, conjunto2):
    conjuntoDiferencia = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            conjuntoDiferencia.append(elemento)
    return conjuntoDiferencia

def diferencia_simetrica(conjunto1, conjunto2):
    conjunto_diferencia_simetrica = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            conjunto_diferencia_simetrica.append(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto1:
            conjunto_diferencia_simetrica.append(elemento)
    return conjunto_diferencia_simetrica

def formatear(conjunto):
    formateado = "{" + ", ".join(conjunto) + "}"
    return formateado


def main():
    universo = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    conjuntos = []

    while True:
        opcion = menu_principal()

        if opcion == '1':
            conjunto = crear_conjuntos()
            conjuntos.append(conjunto)
            print (f"Conjunto creado: {formatear(conjunto)}")

        elif opcion == '2':
            if len(conjuntos) < 2:
                print("Debe crear al menos dos conjuntos para realizar operaciones.")
                continue

            while True:
                operacion = mostrar_menu_operaciones()

                if operacion == '1':
                    conjunto = conjuntos[int(input("Selecciona el índice del conjunto (1 o 2): ")) - 1]
                    resultado = complemento(conjunto, universo)
                    print(f"Complemento: {formatear(resultado)}")

                elif operacion == '2':
                    resultado = union(conjuntos[0], conjuntos[1])
                    print(f"Unión: {resultado}")

                elif operacion == '3':
                    resultado = interseccion(conjuntos[0], conjuntos[1])
                    print(f"Intersección: {formatear(resultado)}")

                elif operacion == '4':
                    resultado = diferencia(conjuntos[0], conjuntos[1])
                    print(f"Diferencia: {formatear(resultado)}")

                elif operacion == '5':
                    resultado = diferencia_simetrica(conjuntos[0], conjuntos[1])
                    print(f"Diferencia Simétrica: {formatear(resultado)}")

                elif operacion == '6':
                    break

                else:
                    print("Operación no válida, por favor intenta de nuevo.")

        elif opcion == '3':
            print("Fin del programa.")
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")



main()    