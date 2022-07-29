import pygame


class Window:
    def __init__(self, x, y, title):
        pygame.init()

        self.window = pygame.display.set_mode([x, y])
        pygame.display.set_caption(title)

        self.loop = True

        self.list_obj = []

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_move_up = True
                if event.key == pygame.K_s:
                    player1_move_down = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1_move_up = False
                if event.key == pygame.K_s:
                    player1_move_down = False

    def add_obj(self, item):
        self.list_obj.append(item)

    def updates(self):

        while self.loop:
            self.events()
            pygame.display.update()
