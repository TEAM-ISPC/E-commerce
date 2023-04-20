from sqlService import sqlService

class CategoriasTrabajo():    

    def __init__(self, IdCategorias, Tipo, Descripcion):
        self._IdCategorias = IdCategorias
        self._Tipo = Tipo
        self._Descripcion = Descripcion

    @property            
    def IdCategorias(self): 
        return self._IdCategorias
    @IdCategorias.setter    
    def IdCategorias(self, value):   
        self._IdCategorias = value

    @property            
    def Tipo(self): 
        return self._Tipo
    @Tipo.setter    
    def Tipo(self, value):   
        self._Tipo = value

    @property            
    def Descripcion(self): 
        return self._Descripcion
    @Descripcion.setter    
    def Descripcion(self, value):   
        self._Descripcion = value    

    def guardarCategoria(self, categoria):
        Query = "INSERT INTO categoriastrabajo (idCategoria, Tipo, Descripcion) VALUES (0, '" + categoria.Tipo + "', '" + categoria.Descripcion + "');"
        sqlService.ejecutarSqlCUD(self, Query, "Se grabó categoria.", "Error al grabar categoria {}")

    def obtenerCategoriaPorId(self, id):           
        Query = "select * from categoriastrabajo WHERE idCategoria =" + str(id)
        Categoria = sqlService.ejecutarSqlR1(self, Query, "Error al obtener la categoria {}")
        print(Categoria)
        return Categoria

    def borrarCategoriaPorId(self, id):
        Query = "DELETE FROM categoriastrabajo WHERE IdCategoria=" + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se borró la categoria.", "Error al borrar la categoria {}")

    def actualizarCategoriaPorId(self, id, categoria):
        Query = "UPDATE categoriastrabajo SET Tipo ='" + categoria.Tipo + "', Descripcion ='" + categoria.Descripcion + "' WHERE idCategoria = " + str(id)
        sqlService.ejecutarSqlCUD(self, Query, "Se actualizó la categoria correctamente.", "Error al borrar la categoria {}")

    def obtenerListaCategoria(self):
        Query = "SELECT * FROM categoriastrabajo"
        ClienteLista = sqlService.ejecutarSqlRAll(self, Query, "Error al obtener categoria {}")
        print(ClienteLista)
        return ClienteLista


categoria1 = CategoriasTrabajo(0, "peluqueria", "descripcion de categoria")
# categoria1.guardarCategoria(categoria1)
# categoria1.obtenerCategoriaPorId(4)
# categoria1.borrarCategoriaPorId(2)
# categoria2 = CategoriasTrabajo(0, "barberia", "descripcion de categoria actualizada")
# categoria1.actualizarCategoriaPorId(8, categoria2)
# categoria1.obtenerListaCategoria()
# print(categoria1.Tipo)
