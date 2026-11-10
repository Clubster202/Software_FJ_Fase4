from entidades import Entidad
from excepciones import DatosInvalidosError

class Cliente(Entidad):
    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatosInvalidosError("El nombre debe tener al menos dos caracteres.")
        self._nombre = valor.strip()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.rsplit("@", 1)[-1]:
            raise DatosInvalidosError("El correo no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 7:
            raise DatosInvalidosError("El teléfono debe tener al menos siete caracteres.")
        self._telefono = valor.strip()

    def describir(self):
        return f"Cliente {self.identificador}: {self.nombre} | {self.correo}"
