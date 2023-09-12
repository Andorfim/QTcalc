# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtCore

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form_ui import Ui_Widget
from PySide6 import QtWidgets 

class Widget(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)    
        self.ui.label.setText(QCoreApplication.translate("Widget", u"0", None))

        


    # Продолжает функциональность при нажатии дальнейших кнопок
    
    # def proceed(self):

        

        
        # self.ui.label.setText(QCoreApplication.translate("Widget", u"0", None))
        # self.ui.text_edit.append()
    
    

    # def check(self):
    # if ui.pushButton_7.setCheckable == True:


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
