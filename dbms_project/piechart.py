from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtCharts import QChart, QChartView, QPieSeries
from PyQt5 import QtChart
from PyQt5.QtChart import QPieSeries, QChart, QChartView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
import mysql.connector as mc
import traceback


class Window(QMainWindow):
    agent_id = ""
    def __init__(self, x):
        self.agent_id = x
        super().__init__()
        self.setGeometry(980, 20, 461, 371)
        self.setWindowTitle("Agent Report")
        self.setWindowIcon(QIcon('PN.jpg'))
        self.pie_chart()

    def pie_chart(self):

        global no_rent, no_sold, no_reg
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="Yash@2914",
                database="dbms_project"
            )
            print(self.agent_id)
            cursor = mydb.cursor()
            query = "select count(emp_id) from property join seller where mode = 'Rented' and emp_id like '" + str(self.agent_id) + "' and seller.seller_id=property.seller_id"
            query2 = "select count(emp_id) from property join seller where mode = 'Sold' and emp_id like '" + str(self.agent_id) + "' and seller.seller_id=property.seller_id"
            query3 = "select count(emp_id) from seller where emp_id like '" + str(self.agent_id) + "'"
            cursor.execute(query)
            result = cursor.fetchone()
            cursor.execute(query2)
            result1 = cursor.fetchone()
            cursor.execute(query3)
            result2 = cursor.fetchone()
            no_rent = (result[0])
            no_sold = (result1[0])
            no_reg = (result2[0])

        except mc.Error as e:
            traceback.print_exc()

        series = QPieSeries()
        series.append("No. of properties rented", no_rent)
        series.append("No. of properties sold", no_sold)
        series.append("No. of properties registered", no_reg)

        # add slice
        my_slice = series.slices()[2]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle("Agent report")

        chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)
        # chart.legend().setVisible(False)
        # chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)
        chartview = QChartView(chart)

        self.setCentralWidget(chartview)


app = QApplication(sys.argv)
window = Window(5)
window.show()
sys.exit(app.exec())
