# import sys
# import os
# myDir = os.getcwd()
# sys.path.append(myDir)


class Empleado:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS empleado
                (cedula_empleado INT NOT NULL,
                nombre_empleado VARCHAR(191) NOT NULL,
                telefono INT(12) NOT NULL,
                email VARCHAR(255) NOT NULL,
                apellido VARCHAR(50) NOT NULL,
                direccion VARCHAR(120) NOT NULL,
                fecha_insercion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                PRIMARY KEY (cedula_empleado)
                )"""
            cursor.execute(sql)
        self.conn.commit()
        
        
    def insertarDatos(self,datos): # metodo para insertar datos
        
        try:         # usamos una instruccion try except para que en caso de error, no se nos caiga el programa.
            with self.conn.cursor() as cursor:
                datos_a_insertar = datos
                consulta = """INSERT INTO empleado (cedula_empleado, nombre_empleado, telefono, email, apellido, direccion) VALUES (%s, %s, %s, %s, %s, %s)"""
                cursor.execute(consulta, datos_a_insertar)
                self.conn.commit()
                print("Datos insertados correctamente en la tabla 'empleado'")
        except Exception as e:
            print(f"Error al insertar datos en la tabla 'empleado': {e}")
            
    def Cedulas(self,sql):
        with self.conn.cursor() as cursor:
            consulta = sql
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            print("Obteniendo todas las cedulas'")
            print(consulta)
            return consulta
    
    
    def obtenerCedula(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT cedula_empleado FROM empleado ORDER BY fecha_insercion DESC LIMIT 1")
            ultima_cedula = cursor.fetchone()
            print(ultima_cedula)
        return ultima_cedula[0] if ultima_cedula else None

    def obtenerDatos(self,cedula):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nombre_empleado,telefono,email,apellido,direccion from empleado where cedula_empleado = %s"""
            cursor.execute(consulta,cedula)
            datos = cursor.fetchone()
            print(datos)
        return datos

    def modificarEmpleado(self,datos):
        with self.conn.cursor() as cursor:
            consulta = """UPDATE empleado SET nombre_empleado = %s, telefono = %s,email = %s,apellido = %s,direccion = %s WHERE cedula_empleado = %s"""
            cursor.execute(consulta,datos)
            self.conn.commit()
            cursor.close()
        print(datos)
        print("datos modificados")     
        
    def existeCedula(self,cedula):
        with self.conn.cursor() as cursor:
            consulta = """SELECT cedula_empleado from empleado where cedula_empleado = %s"""
            cursor.execute(consulta,cedula)
            datos = cursor.fetchone()
            print(datos)
        return "El empleado existe!"
            

    def eliminarEmpleado(self,empleado):
        with self.conn.cursor() as cursor:
            consulta = """DELETE FROM empleado WHERE cedula_empleado = %s"""
            cursor.execute(consulta, empleado)
            self.conn.commit()
            cursor.close()
            print("Eliminando Empleado")