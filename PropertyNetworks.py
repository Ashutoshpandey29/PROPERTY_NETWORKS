from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sys

from PyQt6.QtWidgets import QDialog

from frame1 import Ui_QmainWindow
from frame2 import Agent_MainWindow
from frameagentoffice import Agentoffice_MainWindow
from property_dialog import Property_Dialog
from framebuyer import Buyer_Frame
import mysql.connector as mc
import traceback
# from piechart import Window

class Propertynetworks(QMainWindow, Ui_QmainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.login)# connect


    def userID(self):
        userID = self.LineEdit.text()
        return userID

    def login(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="Yash@2914",
                database="dbms_project"
            )
            cursor = mydb.cursor()
            userID = str(self.LineEdit.text())
            password = self.LineEdit_2.text()
            print(userID)
            print(password)
            query = "Select * from login_details natural join employee where emp_id like'" + userID + "'and password like'" + password + "'"
            # query="select password from login_details where emp_id like '1'"
            cursor.execute(query)
            row = cursor.fetchone()

            if row == None:
                self.label_result.setText("NO USER FOUND!")

            else:
                Name = row[2]
                designation = row[3]
                print(row)
                print(Name)
                self.label_result.setText("VALID!")
                if (designation == "Agent"):
                    self.Agent(Name,userID)
                else:
                    self.Agentoffice(Name)

        except mc.Error as e:
            traceback.print_exc()
            self.label_result.setText("INVALID!")

    def Agent(self, Name, userID):
        # userID = self.LineEdit.text()
        self.agentWindow = QMainWindow()
        self.Ui = Agent_MainWindow(userID)
        self.Ui.setupUi(self.agentWindow)
        self.Ui.label_7.setText("ID: " + userID + " NAME: " + Name)
        self.agentWindow.show()
        self.Ui.toolButton_properties.clicked.connect(self.Ui.property_dialog)
        self.Ui.toolButton_buyer.clicked.connect(self.Ui.buyer_frame)
        self.Ui.toolButton_seller.clicked.connect(self.Ui.seller_frame)


    def Agentoffice(self, Name):
        userID = str(self.LineEdit.text())
        self.agentOfficeWindow = QMainWindow()
        self.ui = Agentoffice_MainWindow()
        self.ui.setupUi(self.agentOfficeWindow)
        self.ui.empname.setText("ID: " + userID + " NAME: " + Name)
        self.agentOfficeWindow.show()
        agent_id = self.ui.lineEdit_agentID.text()
        # self.ui = Agentoffice_MainWindow(self.ui.agent_id)
        # self.agentOfficeWindow.exec()
        self.ui.pushButton.clicked.connect(self.ui.Agentreport)  # connect
        self.ui.toolButton.clicked.connect(self.ui.agent_dialog)
        self.ui.pushButton_4.clicked.connect(self.ui.pychart)








