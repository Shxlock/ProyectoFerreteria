from Models.User import User
import bcrypt

# class User_login():
    
#     def __init__(self, conn):
#         self.conn = conn
#         self.user = User(conn)
#         self.c = self.user.conn.cursor()
#     def Log_In(self,usuario,contraseña):
        
#         self.c.execute('SELECT password, salt FROM user WHERE user=%s', (usuario,))
#         bd = self.c.fetchone()
#         if bd:
#             # contrseña_almacenada = bd[2]
#             # salt_almacenada = bd[3]
#             contraseña_almacenada = bd[0]
#             salt_almacenada = bd[1]
#             contraseña_encriptada = bcrypt.hashpw(contraseña.encode('utf-8'), salt_almacenada.encode('utf-8'))
#             if contraseña_encriptada == contraseña_almacenada:
#                 return True
#         return False


class User_login:
    
    def __init__(self, conn):
        self.conn = conn
        self.user = User(conn)
        self.c = self.user.conn.cursor()
        
    def Log_In(self, usuario, contraseña):
        self.c.execute('SELECT password, salt FROM user WHERE user=%s', (usuario,))
        bd = self.c.fetchone()
        if bd:
            contraseña_almacenada = bd[0]
            salt_almacenada = bd[1]
            # Verifica la contraseña utilizando bcrypt.checkpw
            if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_almacenada.encode('utf-8')):
                return True
        return False

        
        
        
        # self.c.execute('SELECT * FROM user WHERE user=%s AND password=%s AND salt=%s', (usuario,contraseña,salt))  #self.c.execute('SELECT * FROM user WHERE user=%s', (usuario,))
        # existing_user = self.c.fetchone()
        # if existing_user:
        #     return True
        # else:
        #     return False
        
        
        
        
    def agregar(self, usuario, contraseña_encriptada, salt):
        self.c.execute('INSERT INTO user (user, password, salt) VALUES (%s, %s, %s)',
                    (usuario, contraseña_encriptada, salt))
        self.conn.commit()