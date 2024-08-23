"""
    Universidad del Valle de Guatemala 
    Curso: Matemática Discreta
    Catedrático: Ingeniero Mario Castillo
    -Integrantes:
    - Diego Fernando Patzan Marroquín - 23525
    - Aleajando Javier García García - 231136
"""

"""
    MOSTRAR CONJUNTOS DE DICCIONARIO
"""
def mostrar_conjuntos_actuales(conjuntos):
    print("\n----------------------------------------------------------------")
    print("|                    Conjuntos actuales                         |")
    print("----------------------------------------------------------------")
    for clave, conjunto in conjuntos.items():
        print(f"   {clave}: {formatear(conjunto)}")
    print("----------------------------------------------------------------")

"""
    MOSTRAR RESULTADOS
"""
def mostrar_resultados_actuales(resultados):
    print("\n----------------------------------------------------------------")
    print("|                   Resultado de Conjuntos                      |")
    print("----------------------------------------------------------------")
    for clave, resultado in resultados.items():
        print(f"   {clave}: {formatear(resultado)}")
    print("----------------------------------------------------------------")


"""
    CÓDIGO PARA GENERAR CLAVES DE DICCIONARIO
"""
def generar_clave(n):
    clave = ''
    while n >= 0:
        clave = chr(65 + (n % 26)) + clave
        n = n // 26 - 1
    return clave

"""
    SELECCIÓN DE CONJUNTO PARA OPERAR
"""
def seleccionar_conjunto(conjuntos):
    while True:
        mostrar_conjuntos_actuales(conjuntos)
        etiqueta = input(" ⮞ Ingresa la etiqueta del conjunto que desea operar: ").upper()
        if etiqueta in conjuntos:
            return etiqueta
        else:
            print(" * La etiqueta no existe. Volviendo al menú principal.")

"""
    GUARDAR RESULTADO
"""
def preguntar_guardar_conjunto(resultado, conjuntos):
    while True:
        print("\n¿Desea guardar el conjunto resultante?")
        print("1. Sí")
        print("2. No")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            conjuntos.append(resultado)
            print(f"Conjunto guardado: {formatear(resultado)}")
            return resultado
        elif opcion == '2':
            print("El conjunto no se ha guardado.")
            break
        else:
            print("Opción no válida. Por favor, selecciona '1' para Sí o '2' para No.")

"""
    MENU PRINCIPAL DEL PROYECTO
"""
def menu_principal():
    print("\n--------------------------------------------------------------")
    print("|                   Proyecto 01 - Conjuntos                    |")
    print("----------------------------------------------------------------")
    print("|                       Menu Principal                         |")
    print("|                  1. Construir conjuntos                      |")
    print("|                  2. Operar conjuntos                         |")
    print("|                  3. Finalizar programa                       |")
    print("----------------------------------------------------------------")
    opcion = input(" - Selecciona una opción: ")
    return opcion

"""
    MENU DE LAS OPERACIONES ENTRE CONJUNTOS
"""

def mostrar_menu_operaciones():
    print("\n----------------------------------------------------------------")
    print("|                   Operaciones disponibles:                   |")
    print("|                      1. Complemento                          |")
    print("|                      2. Unión                                |")
    print("|                      3. Intersección                         |")
    print("|                      4. Diferencia                           |")
    print("|                      5. Diferencia Simétrica                 |")
    print("|                      6. Regresar al menú principal           |")
    print("----------------------------------------------------------------")
    opcion = input(" - Selecciona una operación: ")
    return opcion

"""
    FINALIZACIÓN Y CRÉDITOS DEL PROGRAMA
"""
def mostrar_creditos():
    print("\n----------------------------------------------------------------")
    print("|                       Fin del programa                        |")
    print("----------------------------------------------------------------")
    print("|          Universidad del Valle de Guatemala                   |")
    print("|          Curso: Matemática Discreta                           |")
    print("|          Catedrático: Ingeniero Mario Castillo                |")
    print("|                                                               |")
    print("|          -Integrantes del proyecto:                           |")
    print("|             - Diego Fernando Patzan Marroquín - 23525         |")
    print("|             - Alejandro Javier García García - 231136         |")
    print("----------------------------------------------------------------")
    print("            ¡Gracias por utilizar nuestro programa!        ")
    print("----------------------------------------------------------------\n")

def crear_conjuntos():
    conjunto = []
    elementos = input("   ⮞ Ingresa los elementos del conjunto (letras A-Z, dígitos 0-9) separados por comas: ").upper()
    if "," in elementos or len(elementos)==1:
        elementos = elementos.split(",")
        for elemento in elementos:
            elemento = elemento.strip()
            if elemento.isalnum() and len(elemento) == 1 and elemento not in conjunto:
                conjunto.append(elemento)
            else:
                print(f" *Elemento inválido o duplicado: {elemento}. Se omitirá.")        
        conjunto = sorted(conjunto)
        return conjunto
    else:
        print(" * Elementos ingresados no válidos")
        return None

def crear_conjunto_universo():
    universo = [chr(i) for i in range(65, 91)]
    universo.extend([str(i) for i in range(10)])
    return universo
    

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
    universo = crear_conjunto_universo()
    print(universo)
    conjuntos = {}
    resultados = {}
    indice = 0
    repetido = False
    while True:
        opcion = menu_principal()
        if opcion == '1':
            conjunto = crear_conjuntos()
            for clave, lista in conjuntos.items():
                if lista == conjunto:
                    repetido = True
                    break

            if repetido:
                print(" * El conjunto ya se ha registrado, vuelva a intentarlo.")
                repetido = False
            else:
                if conjunto is not None:
                    clave = generar_clave(indice)
                    conjuntos[clave] = conjunto
                    print(f" - Conjunto creado: {clave} = {formatear(conjunto)}")
                    indice += 1

        elif opcion == '2':
            if len(conjuntos) == 0:
                print(" * Debe crear al menos un conjunto para realizar operaciones.")
                continue

            mostrar_conjuntos_actuales(conjuntos)

            while True:
                operacion = mostrar_menu_operaciones()
                if operacion == '1':
                    etiqueta = seleccionar_conjunto(conjuntos)
                    seleccion= conjuntos[etiqueta]
                    clave_nueva = etiqueta + "'"
                    resultado = complemento(seleccion, universo)
                    resultados[clave_nueva] = resultado
                    mostrar_resultados_actuales(resultados)
                    print(f"Complemento: {formatear(resultado)}")

                elif operacion == '2': 
                    etiqueta1 = seleccionar_conjunto(conjuntos)
                    etiqueta2 = seleccionar_conjunto(conjuntos)
                    seleccion1 = conjuntos[etiqueta1]
                    seleccion2 = conjuntos[etiqueta2]
                    clave_nueva = etiqueta1 + "U" + etiqueta2
                    resultado = union(seleccion1, seleccion2)
                    resultados[clave_nueva] = resultado
                    mostrar_resultados_actuales(resultados)
                    print(f"Unión: {resultado}")

                elif operacion == '3':
                    etiqueta1 = seleccionar_conjunto(conjuntos)
                    etiqueta2 = seleccionar_conjunto(conjuntos)
                    seleccion1 = conjuntos[etiqueta1]
                    seleccion2 = conjuntos[etiqueta2]
                    clave_nueva = etiqueta1 + "∩" + etiqueta2
                    resultado = interseccion(seleccion1, seleccion2)
                    resultados[clave_nueva] = resultado
                    mostrar_resultados_actuales(resultados)
                    print(f"Intersección: {formatear(resultado)}")

                elif operacion == '4':
                    etiqueta1 = seleccionar_conjunto(conjuntos)
                    etiqueta2 = seleccionar_conjunto(conjuntos)
                    seleccion1 = conjuntos[etiqueta1]
                    seleccion2 = conjuntos[etiqueta2]
                    clave_nueva = etiqueta1 + "-" + etiqueta2
                    resultado = diferencia(seleccion1, seleccion2)
                    resultados[clave_nueva] = resultado
                    mostrar_resultados_actuales(resultados)
                    print(f"Diferencia: {formatear(resultado)}")

                elif operacion == '5':
                    etiqueta1 = seleccionar_conjunto(conjuntos)
                    etiqueta2 = seleccionar_conjunto(conjuntos)
                    seleccion1 = conjuntos[etiqueta1]
                    seleccion2 = conjuntos[etiqueta2]
                    clave_nueva = etiqueta1 + "Δ" + etiqueta2
                    resultado = diferencia_simetrica(seleccion1, seleccion2)
                    resultados[clave_nueva] = resultado
                    mostrar_resultados_actuales(resultados)
                    print(f"Diferencia Simétrica: {formatear(resultado)}")

                elif operacion == '6':
                    break

                else:
                    print(" * Operación no válida, por favor intenta de nuevo.")

        elif opcion == '3':
            mostrar_creditos()
            break

        else:
            print("Opción no válida, por favor intenta de nuevo.")
main()    