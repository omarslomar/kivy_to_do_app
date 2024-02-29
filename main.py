from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def clicked():
    print("Who told you to click me?")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1300, 500, 500, 500)
    win.setWindowTitle("To Do List")

    label = QtWidgets.QLabel(win)
    label.setText("Balls")
    label.move(100, 100)

    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()