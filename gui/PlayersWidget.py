from PySide2.QtWidgets import (QLabel, QVBoxLayout, QWidget)

from api.ApiRequestFactory import ApiRequestFactory


class PlayersWidget(QWidget):
    def __init__(self):
        factory = ApiRequestFactory.get_instance()
        QWidget.__init__(self)

        players = factory.get_players()

        self.layout = QVBoxLayout()

        for pl in players:
            player_lb = QLabel(text=pl.first_name)

            self.layout.addWidget(player_lb)

        self.setLayout(self.layout)
