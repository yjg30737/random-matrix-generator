import random
from PyQt5.QtWidgets import QGraphicsView, QGraphicsRectItem, QGraphicsScene

from random_matrix_generator.block import Block


class RandomMatrixGraphicsView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.__h_dot_cnt = 20
        self.__v_dot_cnt = 20
        self.__dot_size = 10
        self.__border_flag = False
        self.__initUi()

    def __initUi(self):
        scene = QGraphicsScene()
        self.setScene(scene)

    def setHDotCount(self, cnt: int):
        self.__h_dot_cnt = cnt

    def setVDotCount(self, cnt: int):
        self.__v_dot_cnt = cnt
        
    def setDotSize(self, size: int):
        self.__dot_size = size
        
    def setBorder(self, f: bool):
        self.__border_flag = f
                
    def generate(self):
        for x in range(self.__h_dot_cnt):
            for y in range(self.__v_dot_cnt):
                f = random.randint(1, 2)
                self.__addRect(x, y, f)
        
        if self.__border_flag:
            item = QGraphicsRectItem(0, 0, self.__dot_size*self.__h_dot_cnt, 
                                           self.__dot_size*self.__v_dot_cnt)
            self.scene().addItem(item)

    def __addRect(self, x, y, f):
        if f == 1:
            w = h = self.__dot_size
            x *= w
            y *= h
            p = Block(w, h)

            scene = self.scene()

            item = scene.addPixmap(p)
            item.moveBy(x, y)
        else:
            return