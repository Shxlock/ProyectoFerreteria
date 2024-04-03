from Models.empleado import Empleado

class User:
    def __init__(self,conn):
        self.conn = conn          # creamos una instancia de la coneccion que recibimos como parametro
        self.empleado = Empleado(conn)  # instancia del modelo Empleado (user tiene como foranea la primaria de Empleado), por eso la importamos e instanciamos
        with self.conn.cursor() as cursor:           # renombramos self.conn.cursor simplemente como cursor (es como un alias q usabamos en base de datos)
            sql = """CREATE TABLE IF NOT EXISTS user       
                (user_id INT NOT NULL AUTO_INCREMENT,
                user VARCHAR(191) NOT NULL,
                password VARCHAR(191) NOT NULL,
                salt VARCHAR(255) NOT NULL,
                rol VARCHAR(50) NOT NULL,
                cedula_usuario INT NOT NULL,
                PRIMARY KEY (user_id),
                FOREIGN KEY (cedula_usuario) REFERENCES empleado(cedula_empleado) ON DELETE CASCADE
                )""" # empezamos la consulta con 'CREATE TABLE IF NOT EXISTS' lo cual nos ayuda a no crear nuevamente la tabla, esta linea se encarga de que si la tabla ya existe omite todo el proceso de la creacion
            cursor.execute(sql)
        self.conn.commit()
        
    def agregar(self, usuario, contraseña_encriptada, salt, rol,cedula): # metodo para agregar un nuevo usuario
        with self.conn.cursor() as cursor:
            cursor.execute('INSERT INTO user (user, password, salt,rol, cedula_usuario) VALUES (%s, %s, %s,%s,%s)', # '%s' nos ayuda a decirle a la consulta q aun no sabemos los valores para esas columnas, por lo que seran variables
                    (usuario, contraseña_encriptada, salt,rol,cedula))
            self.conn.commit()
            cursor.close()
        return "Usuario Agregado!" # retornamos un mensaje para saber que si se agrego el usuario
        
    def eliminarUsuario(self,empleado):         # metodo para eliminar un usuario
        with self.conn.cursor() as cursor:
            consulta = """DELETE FROM user WHERE cedula_usuario = %s"""
            cursor.execute(consulta, empleado)
            self.conn.commit()         # eliminamos el user
            self.empleado.eliminarEmpleado(empleado)  # eliminamos al empleado que tenga la cedula que le estamos pasando como parametro
            cursor.close()
        
    