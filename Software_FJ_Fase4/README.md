# Software FJ – Fase 4

**Ejercicio 1:** Sistema Integral de Gestión de Clientes, Servicios y Reservas  
**Lenguaje:** Python 3.14.3 | **Editor:** Visual Studio Code  
**Dependencias externas:** Ninguna. **Base de datos:** No utiliza.

## Ejecución
1. Descomprima el ZIP.
2. Abra la carpeta `Software_FJ_Fase4` en Visual Studio Code (File > Open Folder).
3. Abra Terminal > New Terminal.
4. Ejecute `python main.py` o `py main.py`.
5. Seleccione `1` para ejecutar las 12 operaciones demostrativas.

## Pruebas automáticas
Ejecute `python -m unittest pruebas.py -v`.

## Archivos
- `entidades.py`: clase abstracta Entidad.
- `excepciones.py`: excepciones personalizadas.
- `cliente.py`: Cliente y validación encapsulada.
- `servicios.py`: Servicio abstracto y tres servicios concretos.
- `reserva.py`: estados, confirmación, cancelación y procesamiento.
- `gestor.py`: listas, búsquedas, creación de reservas y logs.
- `demo.py`: doce operaciones demostrativas.
- `main.py`: menú de ejecución.
- `pruebas.py`: pruebas automáticas.
- `logs/eventos.log`: historial de eventos y errores.
- `INFORME_BASE.md`: borrador para elaborar el informe.

## Conceptos de POO
Abstracción: `Entidad` y `Servicio`. Herencia: `Cliente`, `Servicio`, `Reserva` y las clases concretas de servicio. Encapsulación: propiedades de `Cliente`. Polimorfismo: cada servicio implementa sus propios métodos de validación y cálculo. Sobrecarga simulada: `calcular_costo` admite parámetros opcionales de impuesto y descuento; Python no realiza sobrecarga tradicional por firma.

## Excepciones
Se incluyen `try/except`, `try/except/else/finally`, excepciones personalizadas y encadenamiento mediante `raise ... from error`. Los eventos y errores se guardan en `logs/eventos.log`.

## Alcance
Clientes, servicios y reservas se guardan en listas mientras la aplicación está abierta. Al cerrar el programa se pierden esos datos; el archivo de logs sí conserva el registro de eventos y errores.

## Evidencias
Capture: estructura de archivos, ejecución de las 12 operaciones, archivo `eventos.log`, pruebas automáticas y repositorio GitHub.
