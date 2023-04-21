""" 
Comentario -> URL - Mostramos el endpoint a donde va a arrancar este controlador. Cuando ingresamos a esa url, el controlador entra en funcionamiento.
Url = /MostrarTurneroEmprendedor

Comentario -> Describimos la función que va a abarcar el controlador, que va a realizar (por ejemplo, que va a mostrar, que va a guardar, etc.).
En este controlador mostrariamos el turnero al emprendedor con los datos necesarios para su organización. 
El emprendedor puede cancelar turnos, bloquear turnos, cargar turnos (por ingreso de forma presencial)...

Comentario -> Definimos el nombre de los métodos que posee el controlador, que sean bien descriptivos con la función que cumplen.
Posee los siguiente métodos:
    - cargarTurnoPresencial
    - bloquearTurno
    - cancelarTurno

Comentario -> Acá informamos que modulos de "Modelo" utiliza.
Consume datos de los modulos Usuario, Cliente, Turnos.

Comentario -> Espero que les sirva y que sea el correcto. Cualquier cosa me consultan.
""" 