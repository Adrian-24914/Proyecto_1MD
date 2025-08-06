from operaciones import Conjunto

def crear_conjuntos_ejemplo():
    # Crea los conjuntos del ejercicio
    U = Conjunto(['a','b','c','d','e','f','g','h','i','j','k',1,2,3,4,5], 'U')
    A = Conjunto(['a',1,3,'d','g','h',4,5], 'A')
    B = Conjunto([2,1,4,'e','f','g','k'], 'B')
    C = Conjunto(['b','d','f','h','k',2,4], 'C')
    D = Conjunto([], 'D')
    E = Conjunto({(1,'a'),(2,'b'),(3,'c')}, 'E')
    
    return {'U': U, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E}


def inicializar_conjuntos():
    # Permite al usuario elegir entre conjuntos predefinidos o crear los suyos
    print("¿Como quieres inicializar los conjuntos?")
    print("1. Usar conjuntos predefinidos del ejercicio")
    print("2. Crear mis propios conjuntos")
    print("3. Empezar sin conjuntos (crear desde cero)")
    
    intentos = 0
    max_intentos = 3
    
    for intento in range(max_intentos):
        opcion = input("Selecciona una opcion (1-3): ").strip()
        
        if opcion == '1':
            return crear_conjuntos_ejemplo()
        elif opcion == '2':
            return crear_conjuntos_personalizados()
        elif opcion == '3':
            return {}
        else:
            print("Opcion no valida. Selecciona 1, 2 o 3.")
            if intento < max_intentos - 1:
                print(f"Intentos restantes: {max_intentos - intento - 1}")
    
    print("Demasiados intentos fallidos. Usando conjuntos predefinidos.")
    return crear_conjuntos_ejemplo()


def crear_conjuntos_personalizados():
    # Permite crear conjuntos personalizados al inicio
    conjuntos = {}
    
    print("Creacion de conjuntos personalizados")
    print("Puedes crear hasta 6 conjuntos. Deja vacio para terminar.")
    print("Para parejas ordenadas usa formato: (1,a),(2,b)")
    
    nombres_disponibles = ['U', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'X', 'Y', 'Z']
    
    for i in range(6):
        nombre = input(f"Nombre del conjunto {i+1} (o Enter para terminar): ").upper().strip()
        
        if not nombre:
            break
            
        if nombre in conjuntos:
            print(f"El conjunto {nombre} ya existe")
            continue
        
        if nombre not in nombres_disponibles:
            print("Usa nombres simples como A, B, C, U, X, Y, etc.")
            continue
        
        elementos = solicitar_elementos_con_parejas()
        conjuntos[nombre] = Conjunto(elementos, nombre)
        print(f"Conjunto creado: {conjuntos[nombre]}")
    
    return conjuntos


def solicitar_elementos_con_parejas():
    # Solicita elementos incluyendo soporte para parejas ordenadas
    entrada = input("Elementos: ").strip()
    
    if not entrada:
        return []
    
    # Detectar si contiene parejas ordenadas
    if '(' in entrada and ')' in entrada:
        return parsear_parejas_ordenadas(entrada)
    else:
        return parsear_elementos_simples(entrada)


def parsear_parejas_ordenadas(entrada):
    # Procesa parejas ordenadas como (1,a),(2,b)
    try:
        # Remover espacios y separar por parejas
        entrada = entrada.replace(' ', '')
        parejas_texto = entrada.split('),(')
        
        parejas = []
        for pareja_texto in parejas_texto:
            # Limpiar paréntesis
            pareja_texto = pareja_texto.replace('(', '').replace(')', '')
            elementos = pareja_texto.split(',')
            
            if len(elementos) == 2:
                elem1, elem2 = elementos[0].strip(), elementos[1].strip()
                
                # Convertir a número si es posible
                try:
                    elem1 = int(elem1)
                except ValueError:
                    pass
                
                try:
                    elem2 = int(elem2)
                except ValueError:
                    pass
                
                parejas.append((elem1, elem2))
        
        return parejas
    except:
        print("Error procesando parejas ordenadas. Formato: (1,a),(2,b)")
        return []


def parsear_elementos_simples(entrada):
    # Procesa elementos simples separados por comas
    elementos = []
    for elem in entrada.split(','):
        elem = elem.strip()
        if elem:  # Solo agregar si no está vacío
            try:
                elementos.append(int(elem))
            except ValueError:
                elementos.append(elem)
    return elementos


def mostrar_menu():
    print("="*50)
    print("CALCULADORA DE OPERACIONES DE CONJUNTOS")
    print("="*50)
    print("1. Ver conjuntos actuales")
    print("2. Union (A ∪ B)")
    print("3. Interseccion (A ∩ B)")
    print("4. Diferencia (A \\ B)")
    print("5. Complemento (¬A)")
    print("6. Producto cartesiano (A × B)")
    print("7. Verificar si es funcion")
    print("8. Operacion con parentesis (A ∪ B) ∩ C")
    print("9. Definir nuevo conjunto")
    print("0. Salir")
    print("="*50)


def mostrar_conjuntos(conjuntos):
    print("Conjuntos disponibles:")
    for nombre, conjunto in conjuntos.items():
        print(f"  {conjunto}")


def solicitar_conjunto(conjuntos, mensaje="Ingresa el nombre del conjunto: "):
    max_intentos = 3
    
    for intento in range(max_intentos):
        nombre = input(mensaje).upper()
        if nombre in conjuntos:
            return nombre
        
        print(f"El conjunto {nombre} no existe. Conjuntos disponibles: {list(conjuntos.keys())}")
        
        if intento < max_intentos - 1:
            print(f"Intentos restantes: {max_intentos - intento - 1}")
    
    # Si no encuentra conjunto válido, retorna el primero disponible
    if conjuntos:
        primer_conjunto = list(conjuntos.keys())[0]
        print(f"Usando conjunto por defecto: {primer_conjunto}")
        return primer_conjunto
    
    return None


def solicitar_elementos():
    # Solicita elementos al usuario y los procesa
    return solicitar_elementos_con_parejas()


def ejecutar_union(conjuntos):
    print("Operacion: Union")
    mostrar_conjuntos(conjuntos)
    
    nombre1 = solicitar_conjunto(conjuntos, "Primer conjunto: ")
    nombre2 = solicitar_conjunto(conjuntos, "Segundo conjunto: ")
    
    resultado = conjuntos[nombre1].union(conjuntos[nombre2])
    
    print(f"{conjuntos[nombre1]}")
    print(f"{conjuntos[nombre2]}")
    print(f"Resultado: {resultado}")


def ejecutar_interseccion(conjuntos):
    print("Operacion: Interseccion")
    mostrar_conjuntos(conjuntos)
    
    nombre1 = solicitar_conjunto(conjuntos, "Primer conjunto: ")
    nombre2 = solicitar_conjunto(conjuntos, "Segundo conjunto: ")
    
    resultado = conjuntos[nombre1].interseccion(conjuntos[nombre2])
    
    print(f"{conjuntos[nombre1]}")
    print(f"{conjuntos[nombre2]}")
    print(f"Resultado: {resultado}")


def ejecutar_diferencia(conjuntos):
    print("Operacion: Diferencia")
    mostrar_conjuntos(conjuntos)
    
    nombre1 = solicitar_conjunto(conjuntos, "Primer conjunto (A): ")
    nombre2 = solicitar_conjunto(conjuntos, "Segundo conjunto (B): ")
    
    resultado = conjuntos[nombre1].diferencia(conjuntos[nombre2])
    
    print(f"{conjuntos[nombre1]}")
    print(f"{conjuntos[nombre2]}")
    print(f"Resultado A \\ B: {resultado}")


def ejecutar_complemento(conjuntos):
    print("Operacion: Complemento")
    mostrar_conjuntos(conjuntos)
    
    if 'U' not in conjuntos or len(conjuntos['U'].elementos) == 0:
        print("Error: Necesitas un conjunto universal U no vacio")
        return
    
    nombre = solicitar_conjunto(conjuntos, "Conjunto para complemento: ")
    
    resultado = conjuntos[nombre].complemento(conjuntos['U'])
    
    print(f"Universo: {conjuntos['U']}")
    print(f"Conjunto: {conjuntos[nombre]}")
    print(f"Complemento: {resultado}")


def ejecutar_producto_cartesiano(conjuntos):
    print("Operacion: Producto Cartesiano")
    mostrar_conjuntos(conjuntos)
    
    nombre1 = solicitar_conjunto(conjuntos, "Primer conjunto: ")
    nombre2 = solicitar_conjunto(conjuntos, "Segundo conjunto: ")
    
    resultado = conjuntos[nombre1].producto_cartesiano(conjuntos[nombre2])
    
    print(f"{conjuntos[nombre1]}")
    print(f"{conjuntos[nombre2]}")
    print(f"Producto cartesiano: {resultado}")
    print(f"Cardinalidad: {len(resultado.elementos)}")


def verificar_funcion(conjuntos):
    print("Verificacion de funcion")
    mostrar_conjuntos(conjuntos)
    
    nombre = solicitar_conjunto(conjuntos, "Conjunto a verificar: ")
    conjunto = conjuntos[nombre]
    
    print(f"Conjunto: {conjunto}")
    
    if conjunto.es_funcion():
        print("Resultado: ES una funcion")
        # Extraer dominio y rango
        if conjunto.elementos:
            dominio = {a for (a, b) in conjunto.elementos}
            rango = {b for (a, b) in conjunto.elementos}
            print(f"Dominio: {dominio}")
            print(f"Rango: {rango}")
    else:
        print("Resultado: NO es una funcion")
        print("Razon: Hay elementos repetidos en el dominio o no son pares ordenados")


def ejecutar_operacion_parentesis(conjuntos):
    print("Operacion: (A ∪ B) ∩ C")
    mostrar_conjuntos(conjuntos)
    
    nombre1 = solicitar_conjunto(conjuntos, "Conjunto A: ")
    nombre2 = solicitar_conjunto(conjuntos, "Conjunto B: ")
    nombre3 = solicitar_conjunto(conjuntos, "Conjunto C: ")
    
    resultado = agrupacion_union_interseccion(
        conjuntos[nombre1], 
        conjuntos[nombre2], 
        conjuntos[nombre3]
    )
    
    print(f"{conjuntos[nombre1]}")
    print(f"{conjuntos[nombre2]}")
    print(f"{conjuntos[nombre3]}")
    print(f"Resultado (A ∪ B) ∩ C: {resultado}")


def definir_conjunto(conjuntos):
    print("Definir nuevo conjunto")
    
    nombre = input("Nombre del conjunto: ").upper().strip()
    
    if not nombre:
        print("Nombre no puede estar vacio")
        return
    
    print("Para parejas ordenadas usa formato: (1,a),(2,b)")
    elementos = solicitar_elementos_con_parejas()
    
    conjuntos[nombre] = Conjunto(elementos, nombre)
    print(f"Conjunto {nombre} creado: {conjuntos[nombre]}")


def main():
    print("=== CALCULADORA DE TEORIA DE CONJUNTOS ===")
    
    # Inicializar conjuntos según preferencia del usuario
    conjuntos = inicializar_conjuntos()
    
    if conjuntos:
        print(f"Conjuntos inicializados: {len(conjuntos)}")
        mostrar_conjuntos(conjuntos)
    else:
        print("Empezando sin conjuntos. Usa la opcion 9 para crear conjuntos.")
    
    opciones = {
        '1': lambda: mostrar_conjuntos(conjuntos),
        '2': lambda: ejecutar_union(conjuntos),
        '3': lambda: ejecutar_interseccion(conjuntos),
        '4': lambda: ejecutar_diferencia(conjuntos),
        '5': lambda: ejecutar_complemento(conjuntos),
        '6': lambda: ejecutar_producto_cartesiano(conjuntos),
        '7': lambda: verificar_funcion(conjuntos),
        '8': lambda: ejecutar_operacion_parentesis(conjuntos),
        '9': lambda: definir_conjunto(conjuntos)
    }
    
    continuar = True
    operaciones_realizadas = 0
    
    while continuar and operaciones_realizadas < 25:
        if not conjuntos and operaciones_realizadas > 0:
            print("No tienes conjuntos definidos. Usa la opcion 9 para crear conjuntos.")
        
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        
        if opcion == '0':
            print("Programa terminado")
            continuar = False
        elif opcion == '9':
            # Definir conjunto siempre está disponible
            opciones[opcion]()
            operaciones_realizadas += 1
        elif opcion in opciones:
            if not conjuntos:
                print("Necesitas al menos un conjunto. Usa la opcion 9 para crear conjuntos.")
            else:
                opciones[opcion]()
                operaciones_realizadas += 1
            
            if operaciones_realizadas < 24 and continuar:
                respuesta = input("¿Continuar? (s/n): ").lower()
                continuar = respuesta.startswith('s')
        else:
            print("Opcion no valida")
    
    if operaciones_realizadas >= 25:
        print("Limite de operaciones alcanzado")


main()

