from abc import ABC, abstractmethod
from datetime import datetime

class Entidad(ABC):
    def __init__(self, identificador):
        if not isinstance(identificador, str) or not identificador.strip():
            raise ValueError("El identificador es obligatorio.")
        self._identificador = identificador.strip()
        self._fecha_creacion = datetime.now()

    @property
    def identificador(self):
        return self._identificador

    @abstractmethod
    def describir(self):
        pass
