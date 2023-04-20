import mysql.connector

class sqlService:
    def ejecutarSqlCUD(self, SqlQuery, msjExito, msjError):
        try:
            connection = mysql.connector.connect(host='localhost', port = 3308, database='turnow', user='root', password='')
            print(SqlQuery)
            cursor = connection.cursor(buffered=True)
            cursor.execute(SqlQuery)
            connection.commit()
            print(cursor.rowcount, msjExito)
            cursor.close()

        except mysql.connector.Error as error:
            print(msjError.format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("Conexion cerrada")

    def ejecutarSqlR1(self, SqlQuery, msjError):
        try:
            connection = mysql.connector.connect(host='localhost', port = 3308, database='turnow', user='root', password='')
            # print(SqlQuery)
            cursor = connection.cursor(buffered=True)
            cursor.execute(SqlQuery)
            row=cursor.fetchall()
            cursor.close()

        except mysql.connector.Error as error:
            print(msjError.format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("Conexion cerrada")
            return row

    def ejecutarSqlRAll(self, SqlQuery, msjError):
        Lista = []
        try:
            connection = mysql.connector.connect(host='localhost', port = 3308, database='turnow', user='root', password='')
            cursor = connection.cursor()
            cursor.execute(SqlQuery)
            rows=cursor.fetchall()
            for row in rows:
                print(row)
                Lista.append(row)
            cursor.close()

        except mysql.connector.Error as error:
            print(msjError.format(error))

        finally:
            if connection.is_connected():
                connection.close()
                print("Conexion cerrada")
            return Lista