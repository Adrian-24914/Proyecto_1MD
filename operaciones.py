class Conjunto:
    #se va representar los conjuntos matematicos (simples)

    def __init__(self, elementos=None, nombre=""):
        self.nombre = nombre
        self.elementos = set(elementos) if elementos else set()
   

    def agregar(self, elemento):
        self.elementos.add(elemento)

    def remover(self, elemento):
        self.elementos.remove(elemento)

    def union(self, otro):
        #es la operacion de A U B
        nombre_resultado = f"({self.nombre} U {otro.nombre})"
        elementos_resultado = self.elementos.union(otro.elementos)
        return Conjunto(elementos_resultado, nombre_resultado)

    #falta interseccion, diferencia, complemento etc...
