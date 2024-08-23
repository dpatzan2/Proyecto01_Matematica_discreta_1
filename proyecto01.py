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
    print("\n\n----------------------------------------------------------------")
    print("|                   Resultado de Conjuntos                      |")
    print("----------------------------------------------------------------")
    for clave, resultado in resultados.items():
        print(f"   {clave}: {formatear(resultado)}")
    print("----------------------------------------------------------------")
    print("  *Recordatorio*")
    print("    - ∩  (Intersección) y ∆  (Delta): Es posible copiar y pegar el símbolo")


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
def seleccionar_conjunto(conjuntos,resultados,tipo,n):
    if tipo == 1:
        while True:
            mostrar_conjuntos_actuales(conjuntos)
            print(f" - Conjunto #{n}:")
            etiqueta = input(" ⮞ Ingresa la etiqueta del conjunto que desea operar: ").upper().strip()
            if etiqueta in conjuntos:
                return etiqueta
            else:
                print("  * La etiqueta no existe. Vuelva a intentarlo.")
    elif tipo == 2:
        while True:
            mostrar_resultados_actuales(resultados)
            print(f" - Conjunto #{n}:")
            etiqueta = input(" ⮞ Ingresa la etiqueta del conjunto que desea operar: ").upper().strip()
            if etiqueta in resultados:
                return etiqueta
            else:
                print("  * La etiqueta no existe. Vuelva a intentarlo.")

"""
    GUARDAR RESULTADO
"""
def opcion_conjuntos():
    while True:
        print("\n\n--------------------------------------------------------------")
        print("|         ¿Con qué conjuntos desea hacer la operación?         |")
        print("----------------------------------------------------------------")
        print("|               1. Conjuntos contruidos                        |")
        print("|               2. Conjuntos de resultados anteriores          |")
        print("----------------------------------------------------------------")
        opcion = input(" - Seleccione una opción: ").strip()

        if opcion == '1':
            return 1
        elif opcion == '2':
            return 2
        else:
            print("Opción no válida. Por favor, vuelva a intentarlo.")

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
    print("|                  3. Mostrar todo los conjuntos                       |")
    print("|                  4. Finalizar programa                       |")
    print("----------------------------------------------------------------")
    opcion = input(" - Selecciona una opción: ")
    return opcion

"""
    MENU DE LAS OPERACIONES ENTRE CONJUNTOS
"""

def mostrar_menu_operaciones():
    print("\n\n----------------------------------------------------------------")
    print("|                   Operaciones disponibles:                   |")
    print("----------------------------------------------------------------")
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
            while True:
                operacion = mostrar_menu_operaciones()
                if operacion == '1':
                    if len(resultados) == 0:
                        etiqueta = seleccionar_conjunto(conjuntos,resultados,1,1)
                        seleccion= conjuntos[etiqueta]

                    else:
                        mostrar = opcion_conjuntos()
                        etiqueta = seleccionar_conjunto(conjuntos,resultados,mostrar,1)
                        if(mostrar==1):
                            seleccion = conjuntos[etiqueta]
                        else:
                            seleccion= resultados[etiqueta]
                    clave_nueva = etiqueta + "'"
                    resultado = sorted(complemento(seleccion, universo))
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '2':
                    if len(resultados) == 0:
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,1,1)
                        seleccion1 = conjuntos[etiqueta1]
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,1,2)
                        seleccion2 = conjuntos[etiqueta1]

                    else:
                        mostrar = opcion_conjuntos()
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,mostrar,1)
                        if(mostrar==1):
                            seleccion1 = conjuntos[etiqueta1]
                        else:
                            seleccion1 = resultados[etiqueta1]
                        mostrar = opcion_conjuntos()
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,mostrar,2) 
                        if(mostrar==1):
                            seleccion2 = conjuntos[etiqueta2]
                        else:
                            seleccion2 = resultados[etiqueta2]

                    clave_nueva = etiqueta1 + "U" + etiqueta2
                    resultado = sorted(union(seleccion1, seleccion2))
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '3':
                    if len(resultados) == 0:
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,1,1)
                        seleccion1 = conjuntos[etiqueta1]
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,1,2)
                        seleccion2 = conjuntos[etiqueta1]
                    else:
                        mostrar = opcion_conjuntos()
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,mostrar)
                        if(mostrar==1):
                            seleccion1 = conjuntos[etiqueta1]
                        else:
                            seleccion1 = resultados[etiqueta1]
                        mostrar = opcion_conjuntos()
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,mostrar) 
                        if(mostrar==1):
                            seleccion2 = conjuntos[etiqueta2]
                        else:
                            seleccion2 = resultados[etiqueta2]
                    clave_nueva = etiqueta1 + "∩" + etiqueta2
                    resultado = sorted(interseccion(seleccion1, seleccion2))
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '4':
                    if len(resultados) == 0:
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,1,1)
                        seleccion1 = conjuntos[etiqueta1]
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,1,2)
                        seleccion2 = conjuntos[etiqueta1]

                    else:
                        mostrar = opcion_conjuntos()
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,mostrar,1)
                        if(mostrar==1):
                            seleccion1 = conjuntos[etiqueta1]
                        else:
                            seleccion1 = resultados[etiqueta1]
                        mostrar = opcion_conjuntos()
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,mostrar,2) 
                        if(mostrar==1):
                            seleccion2 = conjuntos[etiqueta2]
                        else:
                            seleccion2 = resultados[etiqueta2]
                    clave_nueva = etiqueta1 + "-" + etiqueta2
                    resultado = sorted(diferencia(seleccion1, seleccion2))
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '5':
                    if len(resultados) == 0:
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,1,1)
                        seleccion1 = conjuntos[etiqueta1]
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,1,2)
                        seleccion2 = conjuntos[etiqueta1]

                    else:
                        mostrar = opcion_conjuntos()
                        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,mostrar,1)
                        if(mostrar==1):
                            seleccion1 = conjuntos[etiqueta1]
                        else:
                            seleccion1 = resultados[etiqueta1]
                        mostrar = opcion_conjuntos()
                        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,mostrar,2) 
                        if(mostrar==1):
                            seleccion2 = conjuntos[etiqueta2]
                        else:
                            seleccion2 = resultados[etiqueta2]
                    clave_nueva = etiqueta1 + "Δ" + etiqueta2
                    resultado = sorted(diferencia_simetrica(seleccion1, seleccion2))
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '6':
                    break

                else:
                    print(" * Operación no válida, por favor intenta de nuevo.")

        elif opcion == '3':
            if len(conjuntos) ==0 and len(resultados) ==0:
                print(" * Actualmnete no se han contruido conjuntos")
            else:
                mostrar_conjuntos_actuales(conjuntos)
                if len(resultados)!=0:
                    mostrar_resultados_actuales(resultados)

        elif opcion == '4':
            mostrar_creditos()
            break


        else:
            print("Opción no válida, por favor intenta de nuevo.")
main()    