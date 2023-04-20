CREATE DATABASE Turnow;
USE Turnow;

CREATE TABLE IF NOT EXISTS CategoriasTrabajo(
        idCategoria int(11) NOT NULL AUTO_INCREMENT,
        Tipo Varchar(50),
        Descripcion Varchar(500),
        PRIMARY KEY (IdCategoria)
        );
CREATE TABLE IF NOT EXISTS Usuarios (
        idUsuario int(11) NOT NULL AUTO_INCREMENT,
        apellido varchar(50),
        nombre varchar(50),
        email varchar(50),
        password varchar(50),
        telefono varchar(50),
		PRIMARY KEY(idUsuario)
        );
CREATE TABLE IF NOT EXISTS Clientes(
        idCliente int(11) NOT NULL AUTO_INCREMENT,
        direccion varchar(50),
        calificacion INT,
        puntosAcumulados INT,
        usuarioId INT,
        PRIMARY KEY (idCliente),
        FOREIGN KEY (usuarioId) REFERENCES Usuarios(idUsuario)
        );
CREATE TABLE IF NOT EXISTS Emprendedores(
        idEmprendedor int(11) NOT NULL AUTO_INCREMENT,
        nombreEmprendimiento varchar(100),
        diastrabajar varchar(50),
        horarioDiaNormalInicio Time,
        horarioDiaNormalFinal Time,
        horarioDiaEspecialInicio Time,
        horarioDiaEspecialFinal Time,
        tiempoTurno INT,
        descripcion Varchar(500),
        idCategoriasTrabajo INT,
        direccion Varchar(150),
        redSocial1 Varchar(50),
        redSocial2 Varchar(50),
		usuarioId INT,
        PRIMARY KEY (IdEmprendedor),
        FOREIGN KEY (idCategoriasTrabajo) REFERENCES CategoriasTrabajo(idCategoria),
        FOREIGN KEY (usuarioId) REFERENCES Usuarios(idUsuario)
        );
CREATE TABLE IF NOT EXISTS Turnos(
        idTurnos int(11) NOT NULL AUTO_INCREMENT,
        fecha Date,
        horaTurno DateTime,
        clienteId INT,
        trabajo Varchar(50),
        emprendedorId INT,
        comentario Varchar(200),
        PRIMARY KEY (IdTurnos),
        FOREIGN KEY (emprendedorId) REFERENCES Emprendedores(idEmprendedor),
        FOREIGN KEY (clienteId) REFERENCES Clientes(idCliente)
        );  