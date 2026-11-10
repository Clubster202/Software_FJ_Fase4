from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from gestor import GestorSistema

def ejecutar_demo():
    g = GestorSistema()
    print("\\n=== SOFTWARE FJ: DEMOSTRACIÓN DE 12 OPERACIONES ===")

    def prueba(n, nombre, accion):
        try:
            resultado = accion()
            print(f"[{n:02}] {nombre}: CORRECTO")
            if resultado is not None:
                print("     ", resultado)
        except Exception as e:
            g.logger.exception("Operación %s: %s", n, nombre)
            print(f"[{n:02}] {nombre}: ERROR CONTROLADO -> {e}")

    prueba(1, "Registrar cliente Laura", lambda: g.registrar_cliente(Cliente("C001","Laura Gómez","laura@email.com","3001234567")))
    prueba(2, "Registrar cliente Andrés", lambda: g.registrar_cliente(Cliente("C002","Andrés Pérez","andres@email.com","3017654321")))
    prueba(3, "Rechazar cliente inválido", lambda: g.registrar_cliente(Cliente("C003","A","correo","123")))
    prueba(4, "Registrar sala", lambda: g.registrar_servicio(ReservaSala("S001","Sala de reuniones",50000)))
    prueba(5, "Registrar alquiler de equipo", lambda: g.registrar_servicio(AlquilerEquipo("S002","Portátil",80000)))
    prueba(6, "Registrar asesoría", lambda: g.registrar_servicio(Asesoria("S003","Asesoría tecnológica",100000)))

    def reserva_confirmada():
        r = g.crear_reserva("R001","C001","S001",2)
        r.confirmar()
        return r.describir()
    prueba(7, "Crear y confirmar reserva", reserva_confirmada)
    prueba(8, "Reserva con cliente inexistente", lambda: g.crear_reserva("R002","C999","S002",1))
    prueba(9, "Reserva con duración inválida", lambda: g.crear_reserva("R003","C002","S002",0))
    prueba(10, "Procesar reserva confirmada", lambda: g.reservas[0].procesar())

    def reserva_cancelada():
        r = g.crear_reserva("R004","C002","S003",1)
        r.cancelar()
        return r.describir()
    prueba(11, "Crear y cancelar reserva", reserva_cancelada)
    prueba(12, "Intentar procesar reserva cancelada", lambda: g.reservas[-1].procesar())

    print("\\n--- RESUMEN ---")
    for r in g.listar_reservas():
        print(r)
    print("\\nRevise logs/eventos.log para ver los eventos y errores.")
