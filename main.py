from include.pipeutils import text_to_array,get_independent_var,get_dependent_var

def dummy_func(pipe):
    result = pipe
    result[get_dependent_var(pipe)] = result[get_independent_var(pipe)]
    return result



from include.GUI import Ui_MainWindow
from include.GUIGraph import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import Qt
import time

from PyQt5.QtCore import QThread


class rootTask(QThread):
    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while(True):
            self.func(*self.args, **self.kwargs)
            time.sleep(0.1)

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    IG = GUIGraph(ui.graphwidget, width=5, height=4, dpi=100)
    IG.axes.plot([], [])
    IG.setParent(ui.graphwidget)
    
    def loop():
        #Loop functionality here
        
        
        pass
    
    def button_press():
        #Button functionality here
        pipe = {
            'u' : ui.input_u.toPlainText(),
            'v' : ui.input_v.toPlainText(),
            'w' : ui.input_w.toPlainText(),
        }
        pipe = text_to_array(pipe)
        oldpipe = {}
        for key, value in pipe.items():
            oldpipe[key] = value
        pipe = dummy_func(pipe)
        x = pipe[get_independent_var(oldpipe)]
        y = pipe[get_dependent_var(oldpipe)]
        
        IG.axes.cla()
        IG.axes.plot(x, y)
        IG.draw()
        
        
        pass
    
    ui.calcbutton.clicked.connect(button_press)
    
    rT = rootTask(loop)
    rT.start()
    
    
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    main()
