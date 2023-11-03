from controladorLogin import *

class Roles():
    
    def __init__(self):
        self.controlador_login = LogInController()
        self.conn = connection()
        self.modelo_user = User(self.conn)
        self.modelo_user_login = User_login(self.conn)
        
        