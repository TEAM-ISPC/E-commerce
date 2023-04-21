--Tabla CategoriasTrabajo
insert into CategoriasTrabajo(idCategoria, tipo, descripcion) value (1,'peluqueria', 'Establecimiento en el que se peina, se corta, se arregla y se cuida el cabello');
insert into CategoriasTrabajo(idCategoria, tipo, descripcion) value (2,'panaderia', 'Establecimiento en el que se hacen especialidades de panificacion');
insert into CategoriasTrabajo(idCategoria, tipo, descripcion) value (3,'verduleria', 'Establecimiento en el que venden todo tipo de verduras');
select * from CategoriasTrabajo;
select idCategoria, tipo from categoriastrabajo;
delete from categoriastrabajo where idCategoria = 1;
update categoriastrabajo set idCategoria = 4 where idCategoria=2;


-- Tabla Usuario
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "Campos", "Emanuel", "email@com.com", 1234, "351241214");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "rojas", "marcos", "marcos@com.com", 'marcos2k', "3523092919");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "cardelli", "yohana", "yohana@com.com", 'yoha2020', "353412231");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "garelli", "mauricio", "mauricio@com.com",'mauri2k', "351231235");
INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, "salas", "santiago", "santiago@com.com", 'dog2022', "355421313");
SELECT * FROM usuarios;
SELECT idUsuario, nombre FROM usuarios;
SELECT * FROM usuarios where nombre = 'yohana';
DELETE FROM usuarios where idUsuario = 5;
UPDATE usuarios set apellido = 'Campito' where idUsuario = 1;
select * from usuarios inner join clientes on usuarios.idUsuario=clientes.usuarioId;
--Tabla Clientes
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados,usuarioId) VALUES ('igualdad 5886', 10 , 330);
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados,usuarioId) VALUES ('colon 1290', 3 , 120, 3);
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados,usuarioId) VALUES ('marcelo t alvear 493', 1 , 20);
INSERT INTO Clientes (idCliente, direccion, calificacion, puntosAcumulados,usuarioId) VALUES ('calazan 1233', 34 , 12330);
SELECT * 
FROM clientes
inner join usuarios on clientes.usuarioId=usuarios.idUsuario;
-- Tabla emprendedores
INSERT INTO emprendedores (idEmprendedor, nombreEmprendimiento, DiasTrabajar, HorarioDiaNormalInicio, HorarioDiaNormalFinal, HorarioDiaEspecialInicio, HorarioDiaEspecialFinal, TiempoTurno, Descripcion, idCategoriasTrabajo, Direccion, RedSocial1, RedSocial2, UsuarioId) VALUES (0, "Bruno Luna Tatoo", "5", "08:00:00", "16:00:00", "8:00:00", "12:00:00", 1, "descripcion del turno", 1 , "centro 456", "Facebook.com/peluqueria", "instagram.com/peluqueria", 1);
-- Tabla turnos (Join de tres tablas para turnero)
SELECT T.idTurnos, T.fecha, T.horaTurno, U.apellido AS apellidoCliente, U.nombre AS nombreCliente, T.trabajo, E.nombreEmprendimiento FROM Turnos AS T JOIN usuarios AS U ON T.clienteId = U.idUsuario JOIN emprendedores AS E ON T.emprendedorId = E.idEmprendedor;

