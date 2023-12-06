class CategoriaProducto:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """
                CREATE TABLE IF NOT EXISTS categoria_producto
                (id_categoria_producto INT,
                nombre_categoria VARCHAR(90) NOT NULL,
                descripcion VARCHAR(500),
                PRIMARY KEY (id_categoria_producto)
                )"""
                
            cursor.execute(sql)
        self.conn.commit()
        
    def agregarCategoria(self,datos):
        try:
            with self.conn.cursor() as cursor:
                datos_a_insertar = datos
                consulta = """INSERT INTO categoria_producto (id_categoria_producto, nombre_categoria, descripcion) VALUES (%s, %s, %s)"""
                cursor.execute(consulta, datos_a_insertar)
                self.conn.commit()
                print("Datos insertados correctamente en la tabla 'categoria_producto'")
                cursor.close()
        except Exception as e:
            print(f"Error al insertar datos en la tabla 'categoria_producto': {e}")
            
    def eliminarCategoria(self,categoria):
        with self.conn.cursor() as cursor:
            consulta = """DELETE FROM categoria_producto WHERE nombre_categoria = %s"""
            cursor.execute(consulta, categoria)
            self.conn.commit()
            cursor.close()
            print("Eliminando categoria")
            
    def obtenerDatos(self,id):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nombre_categoria,descripcion from categoria_producto where id_categoria_producto = %s"""
            cursor.execute(consulta,id)
            datos = cursor.fetchone()
        return datos
            
    def modificarCategoria(self, datos):
        with self.conn.cursor() as cursor:
            consulta = """UPDATE categoria_producto SET nombre_categoria = %s, descripcion = %s WHERE id_categoria_producto = %s"""
            cursor.execute(consulta, datos)
            self.conn.commit()
            cursor.close()
        print(datos)
        print("datos modificados")
        return "Modificación exitosa" 
            
            
    def obtenerCategoria(self):
        with self.conn.cursor() as cursor:
            consulta = """SELECT nombre_categoria from categoria_producto"""
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            print(consulta)
            cursor.close()
            return consulta
            
    def obtenerIdsCategoria(self):
        with self.conn.cursor() as cursor:
            consulta = """SELECT id_categoria_producto from categoria_producto"""
            cursor.execute(consulta)
            consulta = cursor.fetchall()
            print(consulta)
            cursor.close()
            return consulta
            
    
            
    # def Cedulas(self,sql):
    #     with self.conn.cursor() as cursor:
    #         consulta = sql
    #         cursor.execute(consulta)
    #         consulta = cursor.fetchall()
    #         print("Obteniendo todas las cedulas'")
    #         print(consulta)
            