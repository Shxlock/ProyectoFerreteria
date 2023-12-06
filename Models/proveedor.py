class Proveedor:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS proveedor
                (nit_proveedor INT NOT NULL,
                nombre_proveedor VARCHAR(90) NOT NULL,
                telefono_proveedor INT NOT NULL,
                email_proveedor VARCHAR(90) NOT NULL,
                direccion_proveedor VARCHAR(90) NOT NULL,
                ciudad_proveedor VARCHAR(90) NOT NULL,
                PRIMARY KEY (nit_proveedor)
                )"""
            cursor.execute(sql)
        self.conn.commit()
        
    def agregarProveedor(self,datos):
        try:
            with self.conn.cursor() as cursor:
                datos_a_insertar = datos
                consulta = """INSERT INTO proveedor (nit_proveedor, nombre_proveedor, telefono_proveedor,email_proveedor,direccion_proveedor,ciudad_proveedor) VALUES (%s, %s, %s,%s,%s,%s)"""
                cursor.execute(consulta, datos_a_insertar)
                self.conn.commit()
                print("Datos insertados correctamente en la tabla 'proveedor'")
                cursor.close()
        except Exception as e:
            print(f"Error al insertar datos en la tabla 'proveedor': {e}")
        
    def EliminarProveedor(self,proveedor):
        with self.conn.cursor() as cursor:
            consulta = """DELETE FROM proveedor WHERE nombre_proveedor = %s"""
            cursor.execute(consulta, proveedor)
            self.conn.commit()
            cursor.close()
            print("Eliminando Empleado") 
        
    def buscarProveedor(self,nit):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nombre_proveedor,telefono_proveedor,email_proveedor,direccion_proveedor,ciudad_proveedor from proveedor WHERE nit_proveedor = %s"""
            cursor.execute(consulta,nit)
            consulta = cursor.fetchone()
            cursor.close()
            print(consulta)
            return consulta
    
    def modificarProveedor(self,datos):
        with self.conn.cursor() as cursor:
            consulta = """UPDATE proveedor SET nombre_proveedor = %s, telefono_proveedor = %s,email_proveedor = %s,direccion_proveedor = %s,ciudad_proveedor = %s WHERE nit_proveedor = %s"""
            cursor.execute(consulta,datos)
            self.conn.commit()
            cursor.close()
        print(datos)
        print("datos modificados")   
        
        
    def obtenterProveedores(self):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nombre_proveedor from proveedor"""
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            cursor.close()
            print(consulta)
            return consulta
        
    def obtenerIdProveedores(self):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nit_proveedor from proveedor"""
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            cursor.close()
            print(consulta)
            return consulta