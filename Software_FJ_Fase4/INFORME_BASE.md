# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## Introducción
Este proyecto desarrolla una aplicación de consola para Software FJ, empresa que ofrece reservas de salas, alquiler de equipos y asesorías especializadas. La solución utiliza Python y programación orientada a objetos. La información operativa se administra mediante objetos y listas en memoria, sin utilizar bases de datos.

## Objetivo general
Desarrollar un sistema orientado a objetos para administrar clientes, servicios y reservas, incorporando validaciones y manejo controlado de excepciones.

## Objetivos específicos
- Aplicar abstracción, herencia, encapsulación y polimorfismo.
- Gestionar clientes y tres tipos de servicios.
- Crear, confirmar, cancelar y procesar reservas.
- Calcular costos con impuestos y descuentos opcionales.
- Registrar eventos y errores en un archivo de logs.
- Probar el sistema mediante operaciones demostrativas y pruebas automáticas.

## Descripción de la solución
El sistema permite registrar clientes y servicios. Una reserva asocia un cliente con un servicio, registra la duración, calcula el costo y controla el estado de la operación. Los servicios disponibles son reserva de salas, alquiler de equipos y asesorías.

## Diseño de clases
`Entidad` es la clase abstracta general. `Cliente` administra datos personales con propiedades. `Servicio` es la clase abstracta de los servicios. `ReservaSala`, `AlquilerEquipo` y `Asesoria` heredan de Servicio. `Reserva` administra la relación entre cliente y servicio, el costo y el estado. `GestorSistema` coordina las listas y registra eventos.

## Principios de POO
**Abstracción:** clases abstractas `Entidad` y `Servicio`.  
**Herencia:** las clases especializadas reutilizan características de sus clases padre.  
**Encapsulación:** los datos del cliente se validan mediante propiedades.  
**Polimorfismo:** cada servicio implementa su propia validación de duración y cálculo de costo.  
**Sobrecarga:** se simula mediante parámetros opcionales en `calcular_costo` para impuesto y descuento. Python no ofrece sobrecarga tradicional por firma de método.

## Manejo de excepciones
Se definen excepciones personalizadas para datos inválidos, clientes inexistentes, servicios no disponibles y operaciones de reserva no permitidas. El método de creación de reservas utiliza `try/except/else/finally` y encadenamiento de excepciones (`raise ... from error`). Los eventos y errores se almacenan en `logs/eventos.log`.

## Pruebas
La demostración ejecuta doce operaciones que incluyen registros válidos e inválidos, registro de los tres servicios, reservas exitosas y fallidas, confirmación, procesamiento y cancelación. También se incluyen pruebas automáticas en `pruebas.py`.

## Conclusiones
El proyecto aplica los fundamentos de la programación orientada a objetos a un caso práctico de gestión de servicios. La modularidad facilita el mantenimiento, las validaciones y excepciones controlan situaciones incorrectas y el archivo de logs conserva evidencia de eventos. Las pruebas permiten comprobar el comportamiento sin recurrir a una base de datos.

## Referencias
Universidad Nacional Abierta y a Distancia. (s. f.). *Anexo 3 – Problema a desarrollar Fase 4*. Curso Programación, código 213023.

Python Software Foundation. (s. f.). *The Python Tutorial*. https://docs.python.org/3/tutorial/

Python Software Foundation. (s. f.). *Built-in Exceptions*. https://docs.python.org/3/library/exceptions.html

**Antes de entregar:** complete la portada con sus datos, añada capturas reales, incorpore el enlace real de GitHub y verifique las indicaciones del tutor. No declare participación grupal que no haya ocurrido.
