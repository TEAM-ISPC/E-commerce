from sqlService import sqlService

class Usuario():    

    def __init__(self, IdUsuario, Apellido, Nombre, Email, Password, Telefono):
        self._IdUsuario = IdUsuario
        self._Apellido = Apellido
        self._Nombre = Nombre
        self._Email = Email
        self._Password = Password
        self._Telefono = Telefono

    # Getters y Setters

    @property            
    def IdUsuario(self): 
        return self._IdUsuario
    @IdUsuario.setter    
    def IdUsuario(self, value):   
        self._IdUsuario = value

    @property            
    def Apellido(self): 
        return self._Apellido
    @Apellido.setter    
    def Apellido(self, value):   
        self._Apellido = value 

    @property            
    def Nombre(self): 
        return self._Nombre
    @Nombre.setter    
    def Nombre(self, value):   
        self._Nombre = value 
    
    @property            
    def Email(self): 
        return self._Email
    @Email.setter    
    def Email(self, value):   
        self._Email = value

    @property            
    def Password(self): 
        return self._Email
    @Password.setter    
    def Password(self, value):   
        self._Password = value  

    @property            
    def Telefono(self): 
        return self._Telefono
    @Telefono.setter    
    def Telefono(self, value):   
        self._Telefono = value 

    def __str__(self):
       return str(self.IdUsuario) + ' ' + self.Apellido + ' ' + self.Nombre + ' ' + self.Email + ' ' + self.Password + ' ' + self.Telefono

    def guardarUsuario(self, usuario):
        Query = "INSERT INTO usuarios (idUsuario, apellido, nombre, email, password, telefono) VALUES (0, '" + usuario.Apellido + "', '" + usuario.Nombre + "', '" + usuario.Email + "', '" + usuario.Password + "', '" + usuario.Telefono + "');"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó usuario.", "Error al grabar usuario {}")

    def obtenerUsuarioPorId(self, id):           
        Query = "select * from Usuarios where idUsuario =" + str(id)
        Usuario = sqlService.ejecutarSqlR1(self, Query, "Error al obtener usuario {}")
        print(Usuario)
        return Usuario

    def borrarUsuarioPorId(self, id):
        Query = "DELETE FROM Usuarios WHERE IdUsuario =" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró usuario.", "Error al borrar usuario {}")

    def actualizarUsuarioPorId(self, id, usuario):
        Query = "UPDATE Usuarios SET apellido='" + usuario.Apellido + "', nombre='" + usuario.Nombre + "' , email='" + usuario.Email + "', password='" + usuario.Password + "', telefono='" + usuario.Telefono + "' WHERE idUsuario = " + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó usuario.", "Error al borrar usuario {}")

    def obtenerListaUsuarios(self):
        Query = "select * from Usuarios"
        UsuarioLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener usuario {}")
        print(UsuarioLista)
        return UsuarioLista


# usuario1 = Usuario(0, "luna", "emanuel", "memonlunagmail.com", "1234", "12344213")
# usuario1.guardarUsuario(usuario1)
# usuario1.obtenerUsuarioPorId(2)
# usuario1.borrarUsuarioPorId(2)
# usuario2 = Usuario(0, "lunatico", "emanuel", "memonlunagmail.com", "1234", "12344213")
# usuario1.actualizarUsuarioPorId(1, usuario2)
# usuario1.obtenerListaUsuarios()