from entidades import Entidad
from excepciones import ReservaNoPermitidaError, ServicioNoDisponibleError

class Reserva(Entidad):
    def __init__(self, identificador, cliente, servicio, duracion, impuesto=0.19, descuento=0.0):
        super().__init__(identificador)
        if cliente is None or servicio is None:
            raise ReservaNoPermitidaError("Se requiere cliente y servicio.")
        if not servicio.disponible:
            raise ServicioNoDisponibleError("El servicio no está disponible.")
        servicio.validar_duracion(duracion)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.costo = servicio.calcular_costo(duracion, impuesto, descuento)
        self.estado = "Pendiente"

    def confirmar(self):
        if self.estado != "Pendiente":
            raise ReservaNoPermitidaError("Solo se confirman reservas pendientes.")
        self.estado = "Confirmada"

    def cancelar(self):
        if self.estado not in ("Pendiente", "Confirmada"):
            raise ReservaNoPermitidaError("No se puede cancelar esta reserva.")
        self.estado = "Cancelada"

    def procesar(self):
        if self.estado != "Confirmada":
            raise ReservaNoPermitidaError("La reserva debe estar confirmada.")
        self.estado = "Procesada"
        return f"Reserva {self.identificador} procesada. Total: ${self.costo:,.2f}"

    def describir(self):
        return f"{self.identificador} | {self.cliente.nombre} | {self.servicio.nombre} | {self.estado} | ${self.costo:,.2f}"
