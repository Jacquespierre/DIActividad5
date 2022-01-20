import sys
import var
import events
import clients
from ventana import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.Salir.clicked.connect(events.Eventos.Salir)
        var.sexo=(var.ui.radioButtonFem, var.ui.radioButtonMas)
        for i in var.sexo:
            i.toggled.connect(clients.Clientes.selSexo)
        '''
        Eventos cada de texto
        '''
        var.ui.CampoDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.Aceptar.clicked.connect(clients.Clientes.validarDNI)
        var.ui.grupoSexo.buttonClicked.connect(clients.Clientes.selSexo)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
