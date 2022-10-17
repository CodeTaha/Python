import sys
from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    
    v_box = QtWidgets.QVBoxLayout()
    
    v_box.addWidget(okay)
    v_box.addWidget(cancel)
    
    v_box.addStretch()
    
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 Ders 2") 
    pencere.setLayout(v_box)
    pencere.setGeometry(100, 100, 1200, 900)
   
    pencere.show()
    sys.exit(app.exec())
    
Pencere()