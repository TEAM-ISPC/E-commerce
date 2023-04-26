CREATE DATABASE TurnowEcommerce;
USE TurnowEcommerce;

CREATE TABLE IF NOT EXISTS Categoria(
        idCategoria int(11) NOT NULL AUTO_INCREMENT,
        nombre Varchar(50),
        descripcion Varchar(500),
        estado tinyint(1),
        PRIMARY KEY (IdCategoria)
        );

CREATE TABLE IF NOT EXISTS rol(
        idRol int(11) NOT NULL AUTO_INCREMENT,
        nombre Varchar(50),
        descripcion Varchar(500),
        estado tinyint(1),
        PRIMARY KEY (idRol)
        );
        
CREATE TABLE IF NOT EXISTS Usuario (
        idUsuario int(11) NOT NULL AUTO_INCREMENT,
        rolId int(11),
        nombre varchar(100),
        email varchar(50),
        clave varchar(50),
        telefono varchar(50),
        estado tinyint(1),
		PRIMARY KEY(idUsuario),
        FOREIGN KEY (rolId) REFERENCES rol(idRol)
        );