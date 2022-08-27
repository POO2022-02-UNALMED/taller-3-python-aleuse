class Control:
    def __init__(self):
        pass

    # Método get() para el tv asociado al control
    def getTv(self):
        return self._tv

    # Método set() para el tv asociado al control
    def setTv(self, tv):
        self._tv = tv

    # Método para enlazar el control con el televisor y viceversa
    def enlazar(self, tv):
        self.setTv(tv)
        self._tv.setControl(self)

    # Método para encender el televisor desde el control
    def turnOn(self):
        self._tv.turnOn()

    # Método para apagar el televisor desde el control
    def turnOff(self):
        self._tv.turnOff()

    # Método para aumentar el canal desde el control
    def canalUp(self):
        self._tv.canalUp()

    # Método para disminuir el canal desde el control
    def canalDown(self):
        self._tv.canalDown()

    # Método para aumentar el volumen desde el control
    def volumenUp(self):
        self._tv.volumenUp()

    # Método para disminuir el volumen desde el control
    def volumenDown(self):
        self._tv.volumenDown()

    # Método para asignar el canal desde el control
    def setCanal(self, canal):
        self._tv.setCanal(canal)