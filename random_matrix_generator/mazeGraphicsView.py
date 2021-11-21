import random
from PyQt5.QtWidgets import QGraphicsView, QGraphicsRectItem, QGraphicsScene

from random_matrix_generator.block import Block


class RandomMatrixGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        scene = QGraphicsScene()
        self.setScene(scene)

    def generate(self):
        for x in range(20):
            for y in range(20):
                f = random.randint(1, 2)
                self.__addRect(x, y, f)

        item = QGraphicsRectItem(0, 0, 200, 200)
        self.scene().addItem(item)

    def __addRect(self, x, y, f):
        if f == 1:
            w = h = 10
            x *= w
            y *= h
            p = Block(w, h)

            scene = self.scene()

            item = scene.addPixmap(p)
            item.moveBy(x, y)
        else:
            return