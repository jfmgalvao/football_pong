from os.path import join

from obj import Obj
from src import ASSETS_PATH
from window import Window


class Game:
    def __init__(self):
        self.tela = Window(1280, 720, 'Football Pong')

        self.bg = Obj(join(ASSETS_PATH, 'field.png'), 0, 0)
        self.tela.add_obj(self.bg.drawing(self.tela.window))

        self.player1 = Obj(join(ASSETS_PATH, 'player1.png'), 50, 300)
        self.tela.add_obj(self.player1.drawing(self.tela.window))

        self.player2 = Obj(join(ASSETS_PATH, 'player2.png'), 1150, 300)
        self.tela.add_obj(self.player2.drawing(self.tela.window))

        self.ball_x = 617
        self.ball_y = 290
        self.ball = Obj(join(ASSETS_PATH, 'ball.png'), self.ball_x, self.ball_y)
        self.tela.add_obj(self.ball.drawing(self.tela.window))


Game().tela.updates()
