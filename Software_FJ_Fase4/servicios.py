from abc import abstractmethod
from entidades import Entidad
from excepciones import DatosInvalidosError

class Servicio(Entidad):
    def __init__(self, identificador, nombre, tarifa_base):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")
        if not isinstance(tarifa_base, (int, float)) or isinstance(tarifa_base, bool) or tarifa_base <= 0:
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")
        self.nombre = nombre.strip()
        self.tarifa_base = float(tarifa_base)
        self.disponible = True

    @abstractmethod
    def validar_duracion(self, duracion):
        pass

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0.19, descuento=0.0):
        pass

    def _total(self, duracion, impuesto, descuento):
        if not isinstance(impuesto, (int, float)) or not 0 <= impuesto <= 1:
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 1.")
        if not isinstance(descuento, (int, float)) or not 0 <= descuento <= 1:
            raise DatosInvalidosError("El descuento debe estar entre 0 y 1.")
        return round(self.tarifa_base * duracion * (1 + impuesto) * (1 - descuento), 2)

    def describir(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.identificador} - {self.nombre} | ${self.tarifa_base:,.2f} | {estado}"

class ReservaSala(Servicio):
    def validar_duracion(self, duracion):
        if not isinstance(duracion, int) or isinstance(duracion, bool) or not 1 <= duracion <= 12:
            raise DatosInvalidosError("La sala se reserva entre 1 y 12 horas.")
    def calcular_costo(self, duracion, impuesto=0.19, descuento=0.0):
        self.validar_duracion(duracion)
        return self._total(duracion, impuesto, descuento)

class AlquilerEquipo(Servicio):
    def validar_duracion(self, duracion):
        if not isinstance(duracion, int) or isinstance(duracion, bool) or not 1 <= duracion <= 30:
            raise DatosInvalidosError("El alquiler debe ser de 1 a 30 días.")
    def calcular_costo(self, duracion, impuesto=0.19, descuento=0.0):
        self.validar_duracion(duracion)
        return self._total(duracion, impuesto, descuento)

class Asesoria(Servicio):
    def validar_duracion(self, duracion):
        if not isinstance(duracion, int) or isinstance(duracion, bool) or not 1 <= duracion <= 8:
            raise DatosInvalidosError("La asesoría debe durar entre 1 y 8 horas.")
    def calcular_costo(self, duracion, impuesto=0.19, descuento=0.0):
        self.validar_duracion(duracion)
        return self._total(duracion, impuesto, descuento)
