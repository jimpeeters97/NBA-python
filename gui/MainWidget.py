import sys

from PySide2.QtCore import (Slot)
from PySide2.QtWidgets import (QApplication, QPushButton, QVBoxLayout, QWidget)

from gui.PlayersWidget import PlayersWidget
from gui.TeamsWidget import TeamsWidget


class MainWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.players_button = QPushButton("Players")
        self.teams_button = QPushButton("Teams")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.players_button)
        self.layout.addWidget(self.teams_button)

        self.setLayout(self.layout)

        self.players_button.clicked.connect(self.show_players)
        self.teams_button.clicked.connect(self.show_teams)

    @Slot()
    def show_players(self):
        player_widget = PlayersWidget()
        player_widget.resize(800, 600)
        player_widget.show()

        player_app = QApplication(sys.argv)
        player_app.exec_()

        return player_widget

    @Slot()
    def show_teams(self):
        team_widget = TeamsWidget()
        team_widget.resize(800, 600)
        team_widget.show()

        team_app = QApplication(sys.argv)
        team_app.exec_()

        return team_widget
