from PySide2.QtWidgets import (QLabel, QVBoxLayout, QScrollArea, QWidget)
from PySide2.QtCore import (Qt)
from PySide2.QtGui import (QPalette)

from api.ApiRequestFactory import ApiRequestFactory


class PlayersWidget(QWidget):
    def __init__(self):
        factory = ApiRequestFactory.get_instance()
        QWidget.__init__(self)

        page_list = factory.get_players_from_page(1)

        self.layout = QVBoxLayout()

        label_widget = QWidget()
        label_widget.layout = QVBoxLayout()
        for page_obj in page_list[0]:
            for pl in page_obj[1]:
                lb_text = pl.first_name + ' ' + pl.last_name

                if pl.position is not None and (pl.position is not '' or pl.position is not ' '):
                    lb_text = lb_text + ': ' + pl.position

                player_lb = QLabel(text=lb_text)
                label_widget.layout.addWidget(player_lb)

        label_widget.setLayout(label_widget.layout)

        self.scroll_widget = QScrollArea()
        self.scroll_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_widget.setBackgroundRole(QPalette.Light)
        self.scroll_widget.setWidgetResizable(True)

        self.scroll_widget.setWidget(label_widget)
        self.layout.addWidget(self.scroll_widget)

        self.setLayout(self.layout)
