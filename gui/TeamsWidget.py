from PySide2.QtWidgets import (QLabel, QVBoxLayout, QWidget)

from api.ApiRequestFactory import ApiRequestFactory


class TeamsWidget(QWidget):
    def __init__(self):
        factory = ApiRequestFactory.get_instance()
        QWidget.__init__(self)

        teams = factory.get_teams()

        self.layout = QVBoxLayout()

        for te in teams:
            team_lb = QLabel(text=te.name)

            self.layout.addWidget(team_lb)

        self.setLayout(self.layout)

