import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import mainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = mainWindow.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())