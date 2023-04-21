from sqlService import sqlService

class Turno():    

    def __init__(self, IdTurno, Fecha, HoraTurno, ClienteId, Trabajo, EmprendedorId, Comentario):
        self._IdTurno = IdTurno
        self._Fecha = Fecha
        self._HoraTurno = HoraTurno
        self._ClienteId = ClienteId
        self._Trabajo = Trabajo
        self._EmprendedorId = EmprendedorId
        self._Comentario = Comentario

    @property            
    def IdTurno(self): 
        return self._IdTurno
    @IdTurno.setter    
    def IdTurno(self, value):   
        self._IdTurno = value    

    @property            
    def Fecha(self): 
        return self._Fecha
    @Fecha.setter    
    def Fecha(self, value):   
        self._Fecha = value    
 
    @property            
    def HoraTurno(self): 
        return self._HoraTurno
    @HoraTurno.setter    
    def HoraTurno(self, value):   
        self._HoraTurno = value       

    @property            
    def ClienteId(self): 
        return self._ClienteId
    @ClienteId.setter    
    def ClienteId(self, value):   
        self._ClienteId = value      

    @property            
    def Trabajo(self): 
        return self._Trabajo
    @Trabajo.setter    
    def Trabajo(self, value):   
        self._Trabajo = value   

    @property            
    def EmprendedorId(self): 
        return self._EmprendedorId
    @EmprendedorId.setter    
    def EmprendedorId(self, value):   
        self._EmprendedorId = value             

    @property            
    def Comentario(self): 
        return self._Comentario
    @Comentario.setter    
    def Comentario(self, value):   
        self._Comentario = value   

    def __str__(self):
       return str(self.IdTurno) + ' ' + self.Fecha + ' ' + self.HoraTurno + ' ' + str(self.ClienteId) + ' ' + self.Trabajo + ' ' + str(self.EmprendedorId) + ' ' + self.Comentario

    def guardarTurno(self, turno):
        Query = "INSERT INTO turnos (idTurnos, fecha, horaTurno, clienteId, trabajo, emprendedorId, comentario) VALUES (0, '" + turno.Fecha + "', '" + turno.HoraTurno + "', " + str(turno.ClienteId) + ", '" + turno.Trabajo + "', " + str(turno.EmprendedorId) + ", '" + turno.Comentario + "');"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó Turno.", "Error al grabar Turno {}")

    def obtenerTurnoPorId(self, id):           
        Query = "select * from turnos where idTurnos =" + str(id)
        Turno = sqlService.ejecutarSqlR1(self, Query, "Error al obtener turno {}")
        print(Turno)
        return Turno

    def borrarTurnoPorId(self, id):
        Query = "DELETE FROM turnos WHERE idTurnos =" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró turno.", "Error al borrar turno {}")

    def actualizarTurnoPorId(self, id, turno):
        Query = "UPDATE turnos SET fecha='" + turno.Fecha + "', horaTurno='" + turno.HoraTurno + "' , clienteId='" + str(turno.ClienteId) + "', trabajo='" + turno.Trabajo + "', emprendedorId='" + str(turno.EmprendedorId) + "', comentario='" + turno.Comentario +"' WHERE idTurnos = " + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó usuario.", "Error al borrar usuario {}")

    def obtenerListaTurnos(self):
        Query = "select * from turnos"
        TurnosLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener turnos {}")
        print(TurnosLista)
        return TurnosLista

    def obtenerListaTurnosConDatos(self):
        Query = "SELECT T.idTurnos, T.fecha, T.horaTurno, U.apellido AS apellidoCliente, U.nombre AS nombreCliente, T.trabajo, E.nombreEmprendimiento FROM Turnos AS T JOIN usuarios AS U ON T.clienteId = U.idUsuario JOIN emprendedores AS E ON T.emprendedorId = E.idEmprendedor;"
        TurnosLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener turnos {}")
        print(TurnosLista)
        return TurnosLista

# turno1 = Turno(0, "2022-10-10", "2022-10-10 10:30", 2, "Tatoo grande", 3, "el mejor tatuaje")
# turno1.guardarTurno(turno1)
# turno1.obtenerTurnoPorId(2)
# turno1.borrarUsuarioPorId(2)
# turno2 = Turno(0, "2021-10-20", "2021-10-20 10:30", 2, "Tatoo peqyelo", 3, "el mejor tatooo")
# turno1.actualizarTurnoPorId(1, turno2)
# turno1.obtenerListaTurnos()
# turno1.obtenerListaTurnosConDatos()