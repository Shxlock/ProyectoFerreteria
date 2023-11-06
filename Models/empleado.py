# import sys
# import os
# myDir = os.getcwd()
# sys.path.append(myDir)

from User import User

class Empleado:
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS empleado
                (cedula_empleado INT(10) NOT NULL,
                nombre_empleado VARCHAR(191) NOT NULL,
                telefono INT(12) NOT NULL,
                email VARCHAR(255) NOT NULL,
                apellido VARCHAR(50) NOT NULL,
                direccion VARCHAR(120) NOT NULL,
                id_user INT,
                FOREIGN KEY (id_user) REFERENCES user(id_user),
                PRIMARY KEY (cedula_empleado)
                )"""

           


            cursor.execute(sql)
        self.conn.commit()