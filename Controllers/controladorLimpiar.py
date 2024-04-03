class ControladorLimpiar():

    def limpiar(self,*args): 
        for arg in args:
            arg.clear()
        print("limpio")