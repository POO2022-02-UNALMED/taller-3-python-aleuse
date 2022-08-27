class TV:
    _numTV = 0

    # Constructor
    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        TV._numTV += 1

    # Método get() para el canal
    def getCanal(self):
        return self._canal

    # Método set() para el canal
    def setCanal(self, canal):
        if self.getEstado():
            if 1 <= canal < 120:
                self._canal = canal

    # Método get() para el precio
    def getPrecio(self):
        return self._precio

    # Método set() para el precio
    def setPrecio(self, precio):
        self._precio = precio

    # Método get() para el volumen
    def getVolumen(self):
        return self._volumen

    # Método set() para el volumen
    def setVolumen(self, volumen):
        if self.getEstado():
            self._volumen = volumen

    # Método get() para el número de televisores
    def getNumTV(self):
        return TV._numTV

    # Método set() para el número de televisores
    def setNumTV(self, numTV):
        TV._numTV = numTV

    # Método get() para la marca
    def getMarca(self):
        return self._marca

    # Método set() para la marca
    def setMarca(self, marca):
        self._marca = marca

    # Método get() para el control
    def getControl(self):
        return self._marca

    # Método set() para el control
    def setControl(self, control):
        self._control = control

    # Método get() para el estado
    def getEstado(self):
        return self._estado

    # Método set() para el estado
    def setEstado(self, estado):
        self._estado = estado

    # Método turnOn() para cambiar el estado del TV a encendido
    def turnOn(self):
        self.setEstado(True)

    # Método turnOff() para cambiar el estado del TV a apagado
    def turnOff(self):
        self.setEstado(False)

    # Método canalUp() para aumentar el canal
    def canalUp(self):
        if self.getEstado():
            if 1 <= self.getCanal() < 120:
                self.setCanal(self.getCanal() + 1)

    # Método canalDown() para disminuir el canal
    def canalDown(self):
        if self.getEstado():
            if 1 < self.getCanal() <= 120:
                self.setCanal(self.getCanal() - 1)

    # Método volumenUp() para aumentar el volumen
    def volumenUp(self):
        if self.getEstado():
            if 0 <= self.getVolumen() < 7:
                self.setVolumen(self.getVolumen() + 1)

    # Método volumenDown() para disminuir el volumen
    def volumenDown(self):
        if self.getEstado():
            if 0 < self.getVolumen() <= 7:
                self.setVolumen(self.getVolumen() - 1)