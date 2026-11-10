class ErrorSoftwareFJ(Exception):
    """Excepción base del sistema."""

class DatosInvalidosError(ErrorSoftwareFJ):
    pass

class ClienteNoEncontradoError(ErrorSoftwareFJ):
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass

class ReservaNoPermitidaError(ErrorSoftwareFJ):
    pass
