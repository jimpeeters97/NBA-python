import sys

from PySide2.QtWidgets import (QApplication)

from api.ApiRequestFactory import ApiRequestFactory
from gui.MainWidget import MainWidget

factory = ApiRequestFactory()


def main():
    app = QApplication(sys.argv)

    widget = MainWidget()
    widget.resize(800, 600)
    widget.setWindowTitle("NBA Python")
    widget.show()

    app.exec_()


if __name__ == "__main__":
    main()
