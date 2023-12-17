import pygame
from pygame.sprite import Group

from game_state_manager import IState
from game_setting import GameSetting


class UIMenuSetting(IState):
    def __init__(self, setting: GameSetting, *args):
        super().__init__(*args)
        # setting.is_mute.toggle()

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100, 100), (0, 0, 300, 300))

    def handle_input(self, event):
        pass

    def add_item(self):
        pass
