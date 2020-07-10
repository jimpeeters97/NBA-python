from PySide2.QtWidgets import (QVBoxLayout, QWidget, QTabWidget)

from gui.PlayersWidget import PlayersWidget
from gui.TeamsWidget import TeamsWidget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.tab1 = PlayersWidget()
        self.tab2 = TeamsWidget()

        self.tabs.addTab(self.tab1, "Players")
        self.tabs.addTab(self.tab2, "Teams")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
