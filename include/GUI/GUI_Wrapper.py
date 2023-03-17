from GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import time

from PyQt5.QtCore import QThread


class rootTask(QThread):
    def __init__(self, UI):
        super().__init__()
        self.UI = UI

    def run(self):
        while(True):
            print(self.UI.varInput_1.toPlainText())
            time.sleep(1)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    rT = rootTask(ui)
    rT.start()
    
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()
