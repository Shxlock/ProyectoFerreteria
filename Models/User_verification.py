from Models.User import User


class User_verification():
    
    def __init__(self, conn):
        self.conn = conn
        self.user = User(conn)
        self.c = self.user.conn.cursor()
    def verificar(self,usuario):
        self.c.execute('SELECT * FROM user WHERE user=%s', (usuario,))  #self.c.execute('SELECT * FROM user WHERE user=%s', (usuario,))
        existing_user = self.c.fetchone()
        if existing_user:
            return True
            
    def getData(self,usuario):
        return self.c.execute('SELECT salt FROM user WHERE user=%s', (usuario,))
    
    def agregar(self, usuario, contraseña_encriptada, salt, rol):
        self.c.execute('INSERT INTO user (user, password, salt,rol) VALUES (%s, %s, %s,%s)',
                    (usuario, contraseña_encriptada, salt,rol))
        self.conn.commit()