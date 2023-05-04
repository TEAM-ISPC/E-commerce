from Producto import Producto

class Pedido():
    def __init__(self, idPedido, fechaPedido, fechaEntrega, direccion, total):
        super().__init__(idProducto, precioUnitario)
        self._idPedido= idPedido
        self._fechaPedido = fechaPedido
        self._fechaEntrega = fechaEntrega
        self._direccion = direccion
        self._total = total
        self._productos = []

    @property
    def idPedido(self):
        return self._idPedido
    @idPedido.setter
    def idPedido(self, value):
        self._idPedido = value

    @property
    def fechaPedido(self):
        return self._fechaPedido
    @fechaPedido.setter
    def fechaPedido(self, value):
        self._fechaPedido = value

    @property
    def fechaEntrega(self):
        return self._fechaEntrega
    @fechaEntrega.setter
    def fechaEntrega(self, value):
        self._fechaEntrega = value

    @property
    def direccion(self):
        return self._direccion
    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        self._total = value

    def añadirProducto(self, idProducto, nombreProducto, descripcionProducto, imagenProducto, precioUnitario):
        for producto in self._productos:
            if producto.idProducto == idProducto:
                producto.aumentarCantidad()
                return

        producto = Producto(idProducto, nombreProducto, descripcionProducto, imagenProducto, precioUnitario)
        self._productos.append(producto)

    def eliminarProducto(self):
        for producto in self._productos:
            if producto.idProducto == idProducto:
                self._productos.remove(producto)
                break

    def vaciarPedido(self):
        self._productos = []

    def visualizarPedido(self):
        for producto in self._productos:
            print(producto.nombreProducto, producto.precioUnitario, producto.imagenProducto, producto.cantidad)

    def totalPedido(self):
        total = 0
        for producto in self._productos:
            total += producto.precioUnitario * producto.cantidad
        return total
