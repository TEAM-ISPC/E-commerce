CREATE DATABASE TurnowEcommerce;
USE TurnowEcommerce;

CREATE TABLE IF NOT EXISTS Categoria(
        idCategoria int(11) NOT NULL AUTO_INCREMENT,
        nombre Varchar(50),
        descripcion Varchar(500),
        estado tinyint(1),
        PRIMARY KEY (IdCategoria)
        );
	
CREATE TABLE IF NOT EXISTS Articulo(
        idArticulo int(11) NOT NULL AUTO_INCREMENT,
        idCategoria int(11),
        codigo varchar(50),
        nombre varchar(100),
        stock int(11),
        imagen varchar(20),
        estado tinyint(1),
        PRIMARY KEY (idArticulo), 
        FOREIGN KEY(idCategoria) REFERENCES Categoria(idCategoria)
        );

CREATE TABLE IF NOT EXISTS Persona(
        idPersona int(11) NOT NULL AUTO_INCREMENT,
        tipo_Persona varchar(20),
        nombre varchar(100),
        tipo_documento varchar(20),
        num_documento varchar(20),
        direccion varchar(50),
        telefono varchar(20)
        email varchar(50)
        PRIMARY KEY (idPersona)
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

CREATE TABLE IF NOT EXISTS Ingreso (
        idIngreso int(11) NOT NULL AUTO_INCREMENT,
        proveedorId int(11),
        usuarioId int(11),
        tipo_comprobante varchar(20),
        serie_comprobante varchar(7),
        num_comprobate varchar(10),
        fehca datetime,
        total int(11),
        estado tinyint(1),
	PRIMARY KEY(idIngreso),
        FOREIGN KEY (proveedorId) REFERENCES Persona(idPersona)
        FOREIGN KEY (usuarioId) REFERENCES Usuario(idUsuario)
        );

CREATE TABLE IF NOT EXISTS Detalle_Ingreso (
        idDetalleIngreso int(11) NOT NULL AUTO_INCREMENT,
        ingresoId int(11),
        articuloId int(11),
        cantidad int(11),
        precio int(11),
	PRIMARY KEY(idDetalleIngreso),
        FOREIGN KEY (ingresoId) REFERENCES Ingreso(idIngreso)
        FOREIGN KEY (articuloId) REFERENCES Articulo(idArticulo)
        );

CREATE TABLE IF NOT EXISTS Venta (
        idVenta int(11) NOT NULL AUTO_INCREMENT,
        clienteId int(11),
        usuarioId int(11),
        tipo_comprobante varchar(20),
        serie_comprobante varchar(7),
        num_comprobate varchar(10),
        fehca datetime,
        impuesto int(11),
        total int(11),
        estado tinyint(1),
	PRIMARY KEY(idVenta),
        FOREIGN KEY (clienteId) REFERENCES Ingreso(idPersona)
        FOREIGN KEY (usuarioId) REFERENCES Articulo(idUsuario)
        );

