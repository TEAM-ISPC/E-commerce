from Usuario import *
from CategoriasTrabajo import *
from sqlService import sqlService

class Emprendedor(Usuario, CategoriasTrabajo):    

    def __init__(self, IdUsuario, Apellido, Nombre, Email, Password, Telefono, IdEmprendedor, NombreEmprendimiento, DiasTrabajar, HorarioDiaNormalInicio, HorarioDiaNormalFinal, HorarioDiaEspecialInicio, HorarioDiaEspecialFinal, TiempoTurno, Descripcion, idCategoriasTrabajo, Direccion, RedSocial1, RedSocial2, UsuarioId):
        super().__init__(IdUsuario, Apellido, Nombre, Email, Password, Telefono)
        self._IdEmprendedor = IdEmprendedor
        self._NombreEmprendimiento = NombreEmprendimiento
        self._DiasTrabajar = DiasTrabajar
        self._HorarioDiaNormalInicio = HorarioDiaNormalInicio
        self._HorarioDiaNormalFinal = HorarioDiaNormalFinal
        self._HorarioDiaEspecialInicio = HorarioDiaEspecialInicio
        self._HorarioDiaEspecialFinal = HorarioDiaEspecialFinal
        self._TiempoTurno = TiempoTurno
        self._Descripcion = Descripcion
        self._idCategoriasTrabajo = idCategoriasTrabajo
        self._Direccion = Direccion
        self._RedSocial1 = RedSocial1
        self._RedSocial2 = RedSocial2
        self._UsuarioId = UsuarioId                 

    @property            
    def IdEmprendedor(self): 
        return self._IdEmprendedor
    @IdEmprendedor.setter
    def IdEmprendedor(self, value):   
        self._IdEmprendedor = value

    @property            
    def NombreEmprendimiento(self): 
        return self._NombreEmprendimiento
    @NombreEmprendimiento.setter
    def NombreEmprendimiento(self, value):   
        self._NombreEmprendimiento = value

    @property            
    def DiasTrabajar(self): 
        return self._DiasTrabajar
    @DiasTrabajar.setter    
    def DiasTrabajar(self, value):
        self._DiasTrabajar = value
    
    @property            
    def HorarioDiaNormalInicio(self): 
        return self._HorarioDiaNormalInicio
    @HorarioDiaNormalInicio.setter    
    def HorarioDiaNormalInicio(self, value):   
        self._HorarioDiaNormalInicio = value
        
    @property            
    def HorarioDiaNormalFinal(self): 
        return self._HorarioDiaNormalFinal
    @HorarioDiaNormalFinal.setter    
    def HorarioDiaNormalFinal(self, value):   
        self._HorarioDiaNormalFinal = value

    @property            
    def HorarioDiaEspecialInicio(self): 
        return self._HorarioDiaEspecialInicio
    @HorarioDiaEspecialInicio.setter    
    def HorarioDiaEspecialInicio(self, value):   
        self._HorarioDiaEspecialInicio = value    

    @property            
    def HorarioDiaEspecialFinal(self): 
        return self._HorarioDiaEspecialFinal
    @HorarioDiaEspecialFinal.setter    
    def HorarioDiaEspecialFinal(self, value):   
        self._HorarioDiaEspecialFinal = value   

    @property            
    def TiempoTurno(self): 
        return self._TiempoTurno
    @TiempoTurno.setter    
    def TiempoTurno(self, value):   
        self._TiempoTurno = value       

    @property            
    def Descripcion(self): 
        return self._Descripcion
    @Descripcion.setter    
    def Descripcion(self, value):   
        self._Descripcion = value        

    @property            
    def idCategoriasTrabajo(self): 
        return self._idCategoriasTrabajo
    @idCategoriasTrabajo.setter    
    def idCategoriasTrabajo(self, value):   
        self._idCategoriasTrabajo = value   
          
    @property            
    def Direccion(self): 
        return self._Direccion
    @Direccion.setter    
    def Direccion(self, value):   
        self._Direccion = value     

    @property            
    def RedSocial1(self): 
        return self._RedSocial1
    @RedSocial1.setter    
    def RedSocial1(self, value):   
        self._RedSocial1 = value        

    @property            
    def RedSocial2(self): 
        return self._RedSocial2
    @RedSocial2.setter    
    def RedSocial2(self, value):   
        self._RedSocial2 = value    

    @property            
    def UsuarioId(self): 
        return self._UsuarioId
    @UsuarioId.setter    
    def UsuarioId(self, value):   
        self._UsuarioId = value    

    def guardarEmprendedor(self, emprendedor):
        print(emprendedor.NombreEmprendimiento)
        Query = "INSERT INTO emprendedores(idEmprendedor, nombreEmprendimiento, DiasTrabajar, HorarioDiaNormalInicio, HorarioDiaNormalFinal, HorarioDiaEspecialInicio, HorarioDiaEspecialFinal, TiempoTurno, Descripcion, idCategoriasTrabajo, Direccion, RedSocial1, RedSocial2, UsuarioId) VALUES (0, '"+ emprendedor.NombreEmprendimiento +"', '"+ emprendedor.DiasTrabajar + "', '"+ emprendedor.HorarioDiaNormalInicio + "', '"+ emprendedor.HorarioDiaNormalFinal + "', '"+ emprendedor.HorarioDiaEspecialInicio + "', '"+ emprendedor.HorarioDiaEspecialFinal + "', "+ str(emprendedor.TiempoTurno) + ", '"+ emprendedor.Descripcion + "', "+ str(emprendedor.idCategoriasTrabajo) + ", '"+ emprendedor.Direccion + "', '"+ emprendedor.RedSocial1 + "', '"+ emprendedor.RedSocial2 + "', "+ str(emprendedor.UsuarioId) + ");"
        print(Query)
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó Emprendedor.", "Error al grabar Emprendedor {}")
        
    def obtenerEmprendedorPorId(self, id):           
        Query = "SELECT * FROM emprendedores WHERE idEmprendedor =" + str(id)
        Cliente = sqlService.ejecutarSqlR1(self, Query, "Error al obtener emprendedor {}")
        print(Cliente)
        return Cliente
    
    def borrarEmprendedorPorId(self, id):
        Query = "DELETE FROM emprendedores WHERE idEmprendedor =" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró emprendedor.", "Error al borrar emprendedor {}")
        
    def actualizarEmprendedorPorId(self, id, emprendedor):
        Query = "UPDATE emprendedores SET nombreEmprendimiento='" + emprendedor.NombreEmprendimiento + "', DiasTrabajar='" + emprendedor.DiasTrabajar + "', HorarioDiaNormalInicio='" + emprendedor.HorarioDiaNormalInicio + "', HorarioDiaNormalFinal='" + emprendedor.HorarioDiaNormalFinal + "', HorarioDiaEspecialInicio='" + emprendedor.HorarioDiaEspecialInicio + "', HorarioDiaEspecialFinal='" + emprendedor.HorarioDiaEspecialFinal + "', TiempoTurno=" + str(emprendedor.TiempoTurno) + ", Descripcion='" + emprendedor.Descripcion + "', idCategoriasTrabajo=" + str(emprendedor.TiempoTurno) + ", Direccion='" + emprendedor.Direccion + "', RedSocial1='" + emprendedor.RedSocial1 + "', RedSocial2='" + emprendedor.RedSocial2 + "', UsuarioId=" + str(emprendedor.UsuarioId) + " WHERE idEmprendedor = " + str(id) + ";"
        print(Query)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó emprendedor.", "Error al borrar emprendedor {}")
        
    def obtenerListaEmprendedores(self):
        Query = "SELECT * FROM emprendedores"
        EmprendedoresLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener cliente {}")
        print(EmprendedoresLista)
        return EmprendedoresLista


usuario1 = Usuario(1, "Rios", "Agustin", "agustin@correo.com", "1234", "12344213")
categoria1 = CategoriasTrabajo(1, "peluqueria", "descripcion de categoria")
emprendedor1 = Emprendedor(usuario1.IdUsuario, usuario1.Apellido, usuario1.Nombre, usuario1.Email, usuario1.Password, usuario1.Telefono, 0, "Luna Tatoo", "5", "08:00:00", "16:00:00", "8:00:00", "12:00:00", 1, "descripcion del turno", categoria1.IdCategorias , "centro 456", "Facebook.com/peluqueria", "instagram.com/peluqueria", usuario1.IdUsuario)
emprendedor1.guardarEmprendedor(emprendedor1)
# emprendedor1.obtenerEmprendedorPorId(9)
# emprendedor1.borrarEmprendedorPorId(9)DiasTrabajar
# emprendedor1 = Usuario(1, "Rios", "Agustin", "agustin@correo.com", "1234", "12344213")
# emprendedor1 = Emprendedor(usuario1.IdUsuario, usuario1.Apellido, usuario1.Nombre, usuario1.Email, usuario1.Password, usuario1.Telefono, 0, "5", "08:30:00", "16:30:00", "8:00:00", "12:00:00", 1, "descripcion del turno", categoria1.IdCategorias , "centro 456", "Facebook.com/peluqueria", "instagram.com/peluqueria", usuario1.IdUsuario)
# emprendedor1.actualizarEmprendedorPorId(15, emprendedor1)
# emprendedor1.obtenerListaEmprendedores()


 