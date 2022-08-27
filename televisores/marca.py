class Marca:
    # Constructor
    def __init__(self, nombre):
        self._nombre = nombre

    # Método get()
    def getNombre(self):
        return self._nombre

    # Método set()
    def setNombre(self, nombre):
        self._nombre = nombre