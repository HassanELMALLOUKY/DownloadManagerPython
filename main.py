from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QLineEdit

from mainui import Ui_MainWindow
import urllib.request
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
class UI(Ui_MainWindow):
    def Handel_Progress(self, blocknum, blocksize, totalsize):
        pass

         ## colculate the progress
        readed_data = blocknum * blocksize
        if totalsize > 0:
         download_percentage=readed_data*100 / totalsize
         self.progressBar.setValue(download_percentage)
         QApplication.processEvents()

    def Handel_Buttons(self):
        self.pushButton_2.clicked.connect(self.Handel_Browse)

    def Handel_Browse(self):
        save_location = QFileDialog.getSaveFileName(self,caption="Save as",directory=".",filter="All Files(*.*)" )
        #print(save_location)
        self.lineEdit_2.setText("save_location")
    def Download(self):
        print('Start Download')
        download_url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()
        urllib.request.urlretrieve(download_url, save_location, self.Handel_Progress())


