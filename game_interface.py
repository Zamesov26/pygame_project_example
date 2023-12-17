from game_state_manager import IState
from user_interface import Button


class GameInterface(IState):
    def __init__(self, *args):
        super().__init__(*args)
        self.game = None
        self.button = Button('Выход')
        self.button.rect.left = self.size[0] - 100

    def connect(self, game):
        self.game = game

    def update(self, *args):
        if self.game:
            self.game.update(*args)

    def draw(self, screen):
        if self.game:
            self.game.draw(screen)

        screen.blit(self.button.image, (self.button.rect.x, self.button.rect.y))

    def handle_input(self, event):
        self.button.update(event)
        if self.game:
            self.game.handle_input(event)
