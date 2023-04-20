from Usuario import *
from sqlService import sqlService

class Cliente(Usuario):    

    def __init__(self, IdUsuario, Apellido, Nombre, Email, Password, Telefono, IDCliente, Direccion, Calificacion, PuntosAcumulados, UsuarioId):
        super().__init__(IdUsuario, Apellido, Nombre, Email, Password, Telefono)
        self._IDCliente = IDCliente
        self._Direccion = Direccion
        self._Calificacion = Calificacion
        self._PuntosAcumulados = PuntosAcumulados
        self._UsuarioId = UsuarioId

    # Getters y Setters

    @property            
    def IDCliente(self): 
        return self._IDCliente
    @IDCliente.setter    
    def IDCliente(self, value):   
        self._IDCliente = value

    @property            
    def Direccion(self): 
        return self._Direccion
    @Direccion.setter    
    def Direccion(self, value):   
        self._Direccion = value 

    @property            
    def Calificacion(self): 
        return self._Calificacion
    @Calificacion.setter    
    def Calificacion(self, value):   
        self._Calificacion = value 
    
    @property            
    def PuntosAcumulados(self): 
        return self._PuntosAcumulados
    @PuntosAcumulados.setter    
    def PuntosAcumulados(self, value):   
        self._PuntosAcumulados = value

    @property            
    def UsuarioId(self): 
        return self._UsuarioId
    @UsuarioId.setter    
    def UsuarioId(self, value):   
        self._UsuarioId = value  

    def __str__(self):
       return str(self.IDCliente) + ' ' + self.Direccion + ' ' + str(self.Calificacion) + ' ' + str(self.PuntosAcumulados) + ' ' + str(self.UsuarioId)

    def guardarCliente(self, cliente):
        Query = "INSERT INTO clientes (idCliente, direccion, calificacion, puntosAcumulados, usuarioId) VALUES (0, '" + cliente.Direccion + "', " + str(cliente.Calificacion) + ", " + str(cliente.PuntosAcumulados) + ", " + str(cliente.UsuarioId) + ");"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó cliente.", "Error al grabar cliente {}")

    def obtenerClientePorId(self, id):           
        Query = "select * from clientes where idCliente =" + str(id)
        Cliente = sqlService.ejecutarSqlR1(self, Query, "Error al obtener cliente {}")
        print(Cliente)
        return Cliente

    def borrarClientePorId(self, id):
        Query = "DELETE FROM clientes WHERE IdCliente =" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró cliente.", "Error al borrar cliente {}")

    def actualizarClientePorId(self, id, cliente):
        Query = "UPDATE clientes SET direccion='" + cliente.Direccion + "', calificacion='" + str(cliente.Calificacion) + "' , puntosAcumulados='" + str(cliente.PuntosAcumulados) + "', usuarioId='" + str(cliente.UsuarioId) + "' WHERE idCliente = " + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó usuario.", "Error al borrar usuario {}")

    def obtenerListaClientes(self):
        Query = "select * from clientes"
        ClienteLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener cliente {}")
        print(ClienteLista)
        return ClienteLista


usuario1 = Usuario(1, "luna", "emanuel", "memonlunagmail.com", "1234", "12344213")
cliente1 = Cliente(usuario1.IdUsuario, usuario1.Apellido, usuario1.Nombre, usuario1.Email, usuario1.Password, usuario1.Telefono, 0, "san m 126456", 2, 123, usuario1.IdUsuario)
# cliente1.guardarCliente(cliente1)
# cliente1.obtenerClientePorId(8)
# cliente1.borrarClientePorId(8)
# cliente1 = Usuario(0, "lunatico", "emanuel", "memonlunagmail.com", "1234", "12344213")
# cliente1.actualizarClientePorId(10, cliente1)
# cliente1.obtenerListaClientes()
# print(cliente1.Direccion)
