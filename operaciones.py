class Conjunto:


    # Representa un conjunto matemático con operaciones básicas
    
    def __init__(self, elementos=None, nombre=""):
        self.nombre = nombre
        self.elementos = set(elementos) if elementos else set()
    
    def agregar(self, elemento):
        self.elementos.add(elemento)
    
    def remover(self, elemento):
        self.elementos.discard(elemento)
    
    def union(self, otro):
        # Operación A ∪ B
        nombre_resultado = f"({self.nombre} U {otro.nombre})"
        elementos_resultado = self.elementos.union(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)
    
    def interseccion(self, otro):
        # Operación A ∩ B
        nombre_resultado = f"({self.nombre} ∩ {otro.nombre})"
        elementos_resultado = self.elementos.intersection(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)
    
    def diferencia(self, otro):
        # Operación A - B
        nombre_resultado = f"({self.nombre} - {otro.nombre})"
        elementos_resultado = self.elementos.difference(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)
    
    def complemento(self, universal):
        # Operación A^c respecto al conjunto universal
        nombre_resultado = f"¬{self.nombre}"
        elementos_resultado = universal.elementos.difference(self.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)
    
    def producto_cartesiano(self, otro):
        # Operación A × B - retorna lista de tuplas
        resultado = []
        for elemento_a in self.elementos:
            for elemento_b in otro.elementos:
                resultado.append((elemento_a, elemento_b))
        return resultado
    
    def es_vacio(self):
        return len(self.elementos) == 0
    
    def cardinalidad(self):
        return len(self.elementos)
    
    def __str__(self):
        if self.es_vacio():
            return f"{self.nombre}: ∅"
        
        elementos_ordenados = sorted(list(self.elementos), key=lambda x: (str(type(x)), str(x)))
        elementos_str = ', '.join(str(e) for e in elementos_ordenados)
        return f"{self.nombre}: {{{elementos_str}}}"


class VerificadorFuncion:
    # Analiza si una relación es una función matemática
    
    def __init__(self, relacion):
        self.relacion = relacion
        self.dominio = self._extraer_dominio()
        self.rango = self._extraer_rango()
    
    def _extraer_dominio(self):
        return set(pareja[0] for pareja in self.relacion)
    
    def _extraer_rango(self):
        return set(pareja[1] for pareja in self.relacion)
    
    def es_funcion(self):
        # Una relación es función si cada elemento del dominio aparece una sola vez
        if not self.relacion:
            return True
        
        elementos_dominio = [pareja[0] for pareja in self.relacion]
        elementos_unicos = set(elementos_dominio)
        
        return len(elementos_dominio) == len(elementos_unicos)
    
    def elementos_problematicos(self):
        # Retorna elementos que aparecen múltiples veces en el dominio
        if self.es_funcion():
            return []
        
        conteos = {}
        for pareja in self.relacion:
            elemento = pareja[0]
            conteos[elemento] = conteos.get(elemento, 0) + 1
        
        return [elemento for elemento, count in conteos.items() if count > 1]


class CalculadoraConjuntos:
    # Maneja las operaciones entre conjuntos
    
    def __init__(self):
        self.conjuntos = self._inicializar_conjuntos_ejemplo()
    
    def _inicializar_conjuntos_ejemplo(self):
        # Crea los conjuntos del ejercicio
        conjuntos = {}
        conjuntos['U'] = Conjunto(['a','b','c','d','e','f','g','h','i','j','k',1,2,3,4,5], 'U')
        conjuntos['A'] = Conjunto(['a',1,3,'d','g','h',4,5], 'A')
        conjuntos['B'] = Conjunto([2,1,4,'e','f','g','k'], 'B')
        conjuntos['C'] = Conjunto(['b','d','f','h','k',2,4], 'C')
        conjuntos['D'] = Conjunto([], 'D')
        conjuntos['E'] = Conjunto([(1,'a'),(2,'b'),(3,'c')], 'E')
        return conjuntos
    
    def parsear_elementos(self, entrada):
        # Convierte string de entrada a lista de elementos
        if not entrada.strip():
            return []
        
        elementos = [elem.strip() for elem in entrada.split(',')]
        elementos_procesados = []
        
        for elem in elementos:
            try:
                elementos_procesados.append(int(elem))
            except ValueError:
                elementos_procesados.append(elem)
        
        return elementos_procesados
    
    def parsear_parejas_ordenadas(self, entrada):
        # Procesa parejas ordenadas como (1,a),(2,b)
        try:
            parejas_texto = entrada.replace('(', '').replace(')', '')
            elementos = parejas_texto.split(',')
            
            parejas = []
            for i in range(0, len(elementos), 2):
                if i + 1 < len(elementos):
                    elem1 = elementos[i].strip()
                    elem2 = elementos[i + 1].strip()
                    
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
            return []
    
    def obtener_conjunto(self, nombre):
        return self.conjuntos.get(nombre.upper())
    
    def conjunto_existe(self, nombre):
        return nombre.upper() in self.conjuntos
    
    def obtener_nombres_conjuntos(self):
        return list(self.conjuntos.keys())
    
    def definir_conjunto(self, nombre, elementos):
        self.conjuntos[nombre.upper()] = Conjunto(elementos, nombre.upper())
    
    def calcular_union(self, nombre1, nombre2):
        conjunto1 = self.conjuntos[nombre1.upper()]
        conjunto2 = self.conjuntos[nombre2.upper()]
        return conjunto1.union(conjunto2)
    
    def calcular_interseccion(self, nombre1, nombre2):
        conjunto1 = self.conjuntos[nombre1.upper()]
        conjunto2 = self.conjuntos[nombre2.upper()]
        return conjunto1.interseccion(conjunto2)
    
    def calcular_diferencia(self, nombre1, nombre2):
        conjunto1 = self.conjuntos[nombre1.upper()]
        conjunto2 = self.conjuntos[nombre2.upper()]
        return conjunto1.diferencia(conjunto2)
    
    def calcular_complemento(self, nombre):
        conjunto = self.conjuntos[nombre.upper()]
        universal = self.conjuntos['U']
        return conjunto.complemento(universal)
    
    def calcular_producto_cartesiano(self, nombre1, nombre2):
        conjunto1 = self.conjuntos[nombre1.upper()]
        conjunto2 = self.conjuntos[nombre2.upper()]
        return conjunto1.producto_cartesiano(conjunto2)
    
    def verificar_funcion(self, nombre):
        # Retorna (es_funcion, verificador)
        conjunto = self.conjuntos[nombre.upper()]
        
        elementos_validos = all(
            isinstance(elem, tuple) and len(elem) == 2 
            for elem in conjunto.elementos
        )
        
        if not elementos_validos and not conjunto.es_vacio():
            return False, None
        
        verificador = VerificadorFuncion(list(conjunto.elementos))
        return verificador.es_funcion(), verificador
    
    def obtener_todos_conjuntos(self):
        return list(self.conjuntos.values())
