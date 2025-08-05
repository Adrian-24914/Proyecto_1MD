class Conjunto:

    def __init__(self, elementos=None, nombre=""):
        """
        Constructor del conjunto. Si no se pasan elementos, crea un conjunto vacío.
        `nombre` es solo para mostrar el conjunto con un identificador legible.
        """
        self.nombre = nombre
        self.elementos = set(elementos) if elementos else set()

    def __str__(self):
        """
        Representación en texto del conjunto al imprimirlo.
        """
        return f"{self.nombre} = {self.elementos}"

    def agregar(self, elemento):
        """
        Agrega un nuevo elemento al conjunto.
        """
        self.elementos.add(elemento)

    def remover(self, elemento):
        """
        Elimina un elemento del conjunto. Lanza error si no existe.
        """
        self.elementos.remove(elemento)

    def union(self, otro):
        """
        Realiza la unión entre dos conjuntos: A ∪ B
        Devuelve un nuevo objeto Conjunto.
        """
        nombre_resultado = f"({self.nombre} ∪ {otro.nombre})"
        elementos_resultado = self.elementos.union(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)

    def interseccion(self, otro):
        """
        Realiza la intersección entre dos conjuntos: A ∩ B
        Devuelve un nuevo objeto Conjunto.
        """
        nombre_resultado = f"({self.nombre} ∩ {otro.nombre})"
        elementos_resultado = self.elementos.intersection(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)

    def diferencia(self, otro):
        """
        Realiza la diferencia entre dos conjuntos: A \ B
        Devuelve los elementos que están en A pero no en B.
        """
        nombre_resultado = f"({self.nombre} \\ {otro.nombre})"
        elementos_resultado = self.elementos.difference(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)

    def complemento(self, universo):
        """
        Devuelve el complemento de un conjunto respecto al universo.
        Es decir, todos los elementos del universo que no están en el conjunto actual.
        """
        nombre_resultado = f"(¬{self.nombre})"
        elementos_resultado = universo.elementos.difference(self.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)

    def producto_cartesiano(self, otro):
        """
        Calcula el producto cartesiano A × B.
        Devuelve un conjunto de pares ordenados (a, b).
        """
        nombre_resultado = f"({self.nombre} × {otro.nombre})"
        elementos_resultado = {(a, b) for a in self.elementos for b in otro.elementos}
        return Conjunto(elementos_resultado, nombre_resultado)

    def es_funcion(self):
        """
        Verifica si el conjunto actual de pares ordenados representa una función.
        Es función si no se repite ningún primer elemento (dominio).
        """
        if not all(isinstance(x, tuple) and len(x) == 2 for x in self.elementos):
            return False
        dominio = [a for (a, _) in self.elementos]
        return len(dominio) == len(set(dominio))


# Función para combinar operaciones con agrupación de paréntesis
def agrupacion_union_interseccion(conj1, conj2, conj3):
    """
    Aplica la operación: (conj1 ∪ conj2) ∩ conj3
    Sirve para respetar paréntesis en operaciones combinadas.
    """
    return conj1.union(conj2).interseccion(conj3)
