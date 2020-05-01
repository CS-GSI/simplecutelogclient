import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from scc import scc

class MainWindow(QtWidgets.QMainWindow):    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = scc()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(
            self, 'Confirm Close', 'Are you sure you want to close?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            self.ui.close()
            event.accept()
        else:
            event.ignore()


def main():
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = scc()
    #ui.setupUi(MainWindow)
    window = MainWindow()
    window.show()
    #MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
