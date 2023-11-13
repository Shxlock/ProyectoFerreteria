import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from Views.mockupLogin import *


if __name__ == "__main__":
    # import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(parent=Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
