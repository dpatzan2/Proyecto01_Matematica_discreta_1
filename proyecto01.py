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
    ORDENAIENTO DE CONJUNTOS
"""
def comparcion_conjuntos(conjunto,conjuntos):
    # Comparar si existe algún conjunto dentro del diccionario conjuntos con el mismo tamaño que conjunto
    coincidencias = 0
    iteracion = 0
    for clave, conjunto_existente in conjuntos.items():
        iteracion += 1
        if len(conjunto_existente) == len(conjunto):

            # Comparar si la posición i del conjunto existente está en conjunto y así hasta que llegue hasta el final
            for i in range(len(conjunto)):
                for j in range(len(conjunto_existente)):
                    if conjunto[i] in conjunto_existente:
                        coincidencias += 1
                    else:
                        break
            if len(conjunto_existente)==coincidencias:
                return True
        else:
            iteracion=+1

    if iteracion==len(conjuntos):
        return False

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


def gestor_operacion_conjuntos(conjuntos,resultados):
    if len(resultados) == 0:
        etiqueta1 = seleccionar_conjunto(conjuntos,resultados,1,1)
        seleccion1 = conjuntos[etiqueta1]
        etiqueta2 = seleccionar_conjunto(conjuntos,resultados,1,2)
        seleccion2 = conjuntos[etiqueta2]
        return seleccion1,seleccion2,etiqueta1,etiqueta2
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
        return seleccion1,seleccion2,etiqueta1,etiqueta2

                
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
"""
    CREACIÓN DE UN CONJUNTO CON VALIDACIONES DE INGRESO DE ELEMENTOS
"""
def crear_conjuntos():
    conjunto = []
    elementos = input("   ⮞ Ingresa los elementos del conjunto (letras A-Z, dígitos 0-9) separados por comas: ").upper()
    #Validación para que no se pueda crear un conjunto vacío
    if "," in elementos or len(elementos)==1:
        elementos = elementos.split(",")
        #Validaciones para elemenos no repetidos y sintaxis de entrada
        for elemento in elementos:
            elemento = elemento.strip()
            if elemento.isalnum() and len(elemento) == 1 and elemento not in conjunto:
                conjunto.append(elemento)
            else:
                print(f" *Elemento inválido o duplicado: {elemento}. Se omitirá.")    
        return conjunto
    else:
        print(" * Elementos ingresados no válidos")
        return None
"""
    CREACIÓN DE CONJUNTO UNIVERSO
"""
def crear_conjunto_universo():
    universo = [chr(i) for i in range(65, 91)]
    universo.extend([str(i) for i in range(10)])
    return universo
"""
    FUNCIÓN COMPLEMENTO DE UN CONJUNTO
"""
def complemento(conjunto, universo):
    conjuntoComplemento = []
    for elemento in universo:
        if elemento not in conjunto:
            conjuntoComplemento.append(elemento)
    return conjuntoComplemento
"""
    FUNCIÓN UNIÓN DE CONJUNTOS
"""
def union(conjunto1, conjunto2):
    conjuntoUnion = conjunto1[:]
    for elemento in conjunto2:
        if elemento not in conjuntoUnion:
            conjuntoUnion.append(elemento)
    return conjuntoUnion
"""
    FUNCIÓN INTERSECCIÓN DE CONJUNTOS
"""
def interseccion(conjunto1, conjunto2):
    conjuntoInterseccion = []
    for elemento in conjunto1:
        if elemento in conjunto2:
            conjuntoInterseccion.append(elemento)
    return conjuntoInterseccion
"""
    FUNCIÓN DIFERENCIA DE CONJUNTOS
"""
def diferencia(conjunto1, conjunto2):
    conjuntoDiferencia = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            conjuntoDiferencia.append(elemento)
    return conjuntoDiferencia
"""
    FUNCIÓN DIFERENCIA SIMÉTRICA DE CONJUNTOS
"""
def diferencia_simetrica(conjunto1, conjunto2):
    conjunto_diferencia_simetrica = []
    for elemento in conjunto1:
        if elemento not in conjunto2:
            conjunto_diferencia_simetrica.append(elemento)
    for elemento in conjunto2:
        if elemento not in conjunto1:
            conjunto_diferencia_simetrica.append(elemento)
    return conjunto_diferencia_simetrica
"""
    MOSTRAR EN FORMATO CONJUNTO EN CONSOLA
"""
def formatear(conjunto):
    formateado = "{" + ", ".join(conjunto) + "}"
    return formateado
"""
    FLUJO PRINCIPAL DEL PROGRAMA
"""
def main():
    universo = crear_conjunto_universo()
    print(universo)
    #Diccionario que almacena los conjuntos contruidos
    conjuntos = {}
    #Diccionario que almacena los resultados de las operaciones anteriores
    resultados = {}
    indice = 0
    repetido = False
    while True:
        opcion = menu_principal()
        if opcion == '1':
            conjunto = crear_conjuntos()
            repetido = comparcion_conjuntos(conjunto,conjuntos)
            if repetido==True:
                print(" * El conjunto ya se ha registrado, vuelva a intentarlo.")
            else:
                if conjunto is not None:
                    #Creación de etiqueta de conjunto de manera dinámica según el abecedario
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
                    #Verificación para operar resultados de conjuntos anteriores
                    if len(resultados) == 0:
                        etiqueta = seleccionar_conjunto(conjuntos,resultados,1,1)
                        seleccion= conjuntos[etiqueta]

                    else:
                        #Verificación para operar los conjuntos (contruidos y resultados)
                        mostrar = opcion_conjuntos()
                        etiqueta = seleccionar_conjunto(conjuntos,resultados,mostrar,1)
                        if(mostrar==1):
                            seleccion = conjuntos[etiqueta]
                        else:
                            seleccion= resultados[etiqueta]
                    clave_nueva = etiqueta + "'"
                    # Realización del complemento con el UNiverso
                    resultado = complemento(seleccion, universo)
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '2':
                    # Opciones para seleccionar los conjuntos a operar
                    selecionado = gestor_operacion_conjuntos(conjuntos,resultados)
                    clave_nueva = selecionado[2] + "U" + selecionado[3]
                    # Realización de la unión
                    resultado = union(selecionado[0], selecionado[1])
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '3':
                    # Opciones para seleccionar los conjuntos a operar
                    selecionado = gestor_operacion_conjuntos(conjuntos,resultados)
                    clave_nueva = selecionado[2] + "∩" + selecionado[3]
                    # Realización de la intersección
                    resultado = interseccion(selecionado[0], selecionado[1])
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '4':
                    # Opciones para seleccionar los conjuntos a operar
                    selecionado = gestor_operacion_conjuntos(conjuntos,resultados)
                    clave_nueva = selecionado[2] + "-" + selecionado[3]
                    # Realización de la diferencia
                    resultado = diferencia(selecionado[0], selecionado[1])
                    resultados[clave_nueva] = resultado
                    print(f"  - {clave_nueva}: {formatear(resultado)}")
                    break
                elif operacion == '5':
                    # Opciones para seleccionar los conjuntos a operar
                    selecionado = gestor_operacion_conjuntos(conjuntos,resultados)
                    clave_nueva = selecionado[2] + "Δ" + selecionado[3]
                    # Realizacion de la diferenccia simétrica
                    resultado = diferencia_simetrica(selecionado[0], selecionado[1])
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
            print("  * Opción no válida, por favor intenta de nuevo.")
"""
    INICIALIZACIÓN DEL PROGRAMA MEDIANTE FUNCIÓN MAIN
"""
main()    