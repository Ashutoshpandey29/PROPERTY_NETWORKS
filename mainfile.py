import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PropertyNetworks import Propertynetworks

app = QApplication(sys.argv)

property = Propertynetworks()
 
sys.exit(app.exec_())
