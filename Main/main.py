import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from Views.mockupLogin import *


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    login_controller = LogInController()
    usuario_existe = UsuarioExistenteError()
    ui = Ui_Dialog(parent=Dialog, login_controller=login_controller, usuario_existe=usuario_existe)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
    
    