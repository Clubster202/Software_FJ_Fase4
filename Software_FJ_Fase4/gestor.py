import logging
from pathlib import Path
from excepciones import ClienteNoEncontradoError, ServicioNoDisponibleError
from reserva import Reserva

def crear_logger():
    carpeta = Path(__file__).resolve().parent / "logs"
    carpeta.mkdir(exist_ok=True)
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        h = logging.FileHandler(carpeta / "eventos.log", encoding="utf-8")
        h.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        logger.addHandler(h)
    return logger

class GestorSistema:
    def __init__(self):
        self.clientes, self.servicios, self.reservas = [], [], []
        self.logger = crear_logger()

    def registrar_cliente(self, cliente):
        if any(x.identificador == cliente.identificador for x in self.clientes):
            raise ValueError("El identificador del cliente ya existe.")
        self.clientes.append(cliente)
        self.logger.info("Cliente registrado: %s", cliente.identificador)
        return cliente

    def registrar_servicio(self, servicio):
        if any(x.identificador == servicio.identificador for x in self.servicios):
            raise ValueError("El identificador del servicio ya existe.")
        self.servicios.append(servicio)
        self.logger.info("Servicio registrado: %s", servicio.identificador)
        return servicio

    def buscar_cliente(self, identificador):
        for c in self.clientes:
            if c.identificador == identificador:
                return c
        raise ClienteNoEncontradoError(f"No existe el cliente {identificador}.")

    def buscar_servicio(self, identificador):
        for s in self.servicios:
            if s.identificador == identificador and s.disponible:
                return s
        raise ServicioNoDisponibleError(f"No existe o no está disponible {identificador}.")

    def crear_reserva(self, id_reserva, id_cliente, id_servicio, duracion,
                      impuesto=0.19, descuento=0.0):
        try:
            cliente = self.buscar_cliente(id_cliente)
            servicio = self.buscar_servicio(id_servicio)
            reserva = Reserva(id_reserva, cliente, servicio, duracion, impuesto, descuento)
            self.reservas.append(reserva)
        except Exception as error:
            self.logger.exception("Error creando reserva %s", id_reserva)
            raise RuntimeError(f"No fue posible crear {id_reserva}.") from error
        else:
            self.logger.info("Reserva creada: %s", id_reserva)
            return reserva
        finally:
            self.logger.info("Finalizó intento de reserva: %s", id_reserva)

    def listar_reservas(self):
        return [r.describir() for r in self.reservas]
