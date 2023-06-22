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
    no_rent = 0
    no_sold = 0
    no_reg = 0

    def __init__(self, x, y, z):

        super().__init__()
        self.no_rent = x
        self.no_sold = y
        self.no_reg = z
        self.setGeometry(980, 20, 461, 371)
        self.setWindowTitle("Agent Report")
        self.setWindowIcon(QIcon('PN.jpg'))
        self.pie_chart()

    def pie_chart(self):
        series = QPieSeries()

        print(self.no_sold)
        print(self.no_rent)
        print(self.no_reg)
        # self.no_reg=3
        # self.no_rent=4
        # self.no_sold=5
        series.append("No. of properties rented", self.no_rent)
        series.append("No. of properties sold", self.no_sold)
        series.append("No. of properties registered", self.no_reg)

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
        print("test")




def run_chart(no_rent,no_sold,no_reg):
# def run_chart():
    # print(no_sold)
    # print(no_rent)
    # print(no_reg)
    app = QApplication(sys.argv)
    print("1")
    window = Window(no_rent,no_sold,no_reg)
    # window = Window(1,2,3)
    # print("2")
    window.exec()
    window.show()
    print("3")
    sys.exit(app.exec_())
    print("4")

# run_chart()
