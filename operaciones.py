class Conjunto:
    #se va representar los conjuntos matematicos (simples)

    def __init__(self, elementos=None, nombre=""):
        self.nombre = nombre
        self.elementos = set(elementos) if elementos else set()
   

    def agregar(self, elemento):
        self.elementos.add(elemento)
