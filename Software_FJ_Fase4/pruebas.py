import unittest
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from gestor import GestorSistema
from excepciones import DatosInvalidosError, ReservaNoPermitidaError

class PruebasSoftwareFJ(unittest.TestCase):
    def setUp(self):
        self.g = GestorSistema()
        self.g.registrar_cliente(Cliente("C100","María López","maria@example.com","3001234567"))
        self.g.registrar_servicio(ReservaSala("S100","Sala principal",40000))

    def test_cliente_valido(self):
        self.assertEqual(self.g.clientes[0].nombre, "María López")

    def test_correo_invalido(self):
        with self.assertRaises(DatosInvalidosError):
            Cliente("C101","Pedro Ruiz","correo","3001234567")

    def test_duracion_invalida(self):
        with self.assertRaises(DatosInvalidosError):
            self.g.servicios[0].calcular_costo(0)

    def test_descuento_impuesto(self):
        self.assertEqual(self.g.servicios[0].calcular_costo(2,0.19,0.10),85680.0)

    def test_procesar_confirmada(self):
        r = self.g.crear_reserva("R100","C100","S100",2)
        r.confirmar()
        self.assertIn("procesada", r.procesar())

    def test_no_procesar_pendiente(self):
        r = self.g.crear_reserva("R101","C100","S100",1)
        with self.assertRaises(ReservaNoPermitidaError):
            r.procesar()

    def test_servicios_especializados(self):
        equipo = AlquilerEquipo("S101","Portátil",70000)
        asesoria = Asesoria("S102","Asesoría",90000)
        self.assertGreater(equipo.calcular_costo(1),0)
        self.assertGreater(asesoria.calcular_costo(1),0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
