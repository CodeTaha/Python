import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 1")
    
    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Burası Bir Butondur")
    buton.move(15, 40)
    etiket1 = QtWidgets.QLabel(pencere)
    
    etiket2 = QtWidgets.QLabel(pencere)
    
    etiket2.setPixmap(QtGui.QPixmap("Ekran Görüntüsü (67).png"))
    
    etiket2.move(15,75)
    etiket1.setText("Burası Bir Yazıdır")
    etiket1.move(15, 15)
    
    pencere.setGeometry(100, 100, 1200, 700)
    pencere.show()
    
    sys.exit(app.exec())
    
Pencere()