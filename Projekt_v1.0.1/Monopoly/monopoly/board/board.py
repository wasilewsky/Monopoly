from ..field import *
from ..image import *


class Board:
    def __init__(self):
        self.s = None
        self._build_board()


    def _build_board(self):
        self.s = Start(10, 10, image.POLESTART)


    def draw(self, screen):
        self.s.draw(screen)
