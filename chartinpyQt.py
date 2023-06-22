import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Create a vertical box layout
        vbox = QVBoxLayout(central_widget)

        # Create a figure and axis object
        fig = Figure()
        ax = fig.add_subplot(111)

        # Create the initial pie chart
        labels = ['Apples', 'Bananas', 'Oranges', 'Peaches']
        sizes = [20, 30, 25, 15]
        pie_chart = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        # Create the canvas to display the plot
        canvas = FigureCanvas(fig)
        vbox.addWidget(canvas)

        # Define the update function for the animation
        def update(frame):
            # Generate new data
            new_sizes = [random.randint(0, 50) for i in range(4)]

            # Update the sizes of the pie slices
            for i, slice in enumerate(pie_chart[0]):
                slice.set_sizes([new_sizes[i]])

            # Return the updated artists
            return pie_chart

        # Create the animation object
        animation = FuncAnimation(fig, update, frames=10, interval=1000)

        # Show the PyQt window
        self.setGeometry(100, 100, 640, 480)
        self.setWindowTitle('Animated Pie Chart')
        self.show()

        # Start the animation loop
        canvas.draw()
        animation._start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
