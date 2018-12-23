from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *

import sys
sys.path.insert(0, '../GUI')

from rankgui import Ui_MainWindow

class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listWidget_2.setViewMode(QtWidgets.QListView.IconMode)
        self.ui.listWidget_2.setIconSize(QtCore.QSize(75,75))

        item = QtWidgets.QListWidgetItem()
        icon = QIcon()
        icon.addPixmap(QPixmap("../images/mario.png"), QIcon.Normal, QIcon.Off)
        item.setIcon(icon)

        self.ui.listWidget_2.addItem(item)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())