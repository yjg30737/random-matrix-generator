from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtCore import Qt


class Block(QPixmap):
    def __init__(self, w, h):
        super().__init__(w, h)

        painter = QPainter(self)
        rect = self.rect()
        painter.setBrush(QBrush(Qt.yellow))
        painter.fillRect(rect, painter.brush())
        painter.end()

