from Emprendedor import *

class Producto():
    def __init__(self, IdEmprendedor, idProducto, nombreProducto, descripcionProducto,imagenProducto, precioUnitario, categoriaProducto):
        super().__init__(IdEmprendedor)
        self._idProducto = idProducto
        self._nombreProducto = nombreProducto
        self._descripcionProducto = descripcionProducto
        self._imagenProducto = imagenProducto
        self._precioUnitario = precioUnitario
        self._categoriaProducto = categoriaProducto
        self._emprendedorId = IdEmprendedor


    @property
    def idProducto(self):
        return self._idProducto
    @idProducto.setter
    def idProducto(self, value):
        self._idProducto = value

    @property
    def nombreProducto(self):
        return self._nombreProducto
    @nombreProducto.setter
    def nombreProducto(self, value):
        self._nombreProducto = value

    @property
    def descripcionProducto(self):
        return self._descripcionProducto
    @descripcionProducto.setter
    def descripcionProducto(self, value):
        self._descripcionProducto = value

    @property
    def imagenProducto(self):
        return self._imagenProducto
    @imagenProducto.setter
    def imagenProducto(self, value):
        self._imagenProducto = value

    @property
    def precioUnitario(self):
        return self._precioUnitario
    @precioUnitario.setter
    def precioUnitario(self, value):
        self._precioUnitario = value

    @property
    def categoriaProducto(self):
        return self._categoriaProducto
    @categoriaProducto.setter
    def categoriaProducto(self, value):
        self._categoriaProducto = value

    @property
    def emprendedorId(self):
        return self._emprendedorId
    @emprendedorId.setter
    def emprendedorId(self, IdEmprendedor):
        self._emprendedorId = IdEmprendedor


    def altaProducto(self, IdEmprendedor, Nombre, Descripcion, Imagen, PrecioUnitario, categoriaProducto):
        if self._emprendedorId == IdEmprendedor:
            self._nombreProducto = Nombre
            self._descripcionProducto = Descripcion
            self._imagenProducto = Imagen
            self._precioUnitario = PrecioUnitario
            self._categoriaProducto = categoriaProducto
            print("Producto agregado correctamente")
        else:
            raise Exception("No tiene permiso para dar de alta productos.")

    def modificarProducto(self, IdEmprendedor, nuevaDescripcion, nuevaImagen, nuevoNombre, nuevoPrecioUnitario, nuevaCategoriaProducto):
        if self._emprendedorId == IdEmprendedor:
            self._nombreProducto = nuevoNombre
            self._descripcionProducto = nuevaDescripcion
            self._imagenProducto = nuevaImagen
            self._precioUnitario = nuevoPrecioUnitario
            self._categoriaProducto = nuevaCategoriaProducto
            print("Producto modificado correctamente")
        else:
            raise Exception("No tiene permisos para modificar este producto")

    def bajaProducto(self, IdEmprendedor):
        if self._emprendedorId == IdEmprendedor:
            del self._nombreProducto
            del self._descripcionProducto
            del self._imagenProducto
            del self._precioUnitario
            del self._categoriaProducto
            print("Producto eliminado correctamente")
        else:
            raise Exception("No tiene permisos para eliminar este producto")

