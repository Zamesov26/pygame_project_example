import pygame
from pygame.sprite import Group

from game_state_manager import IState
from user_interface import Button


class MainMenu(IState):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.next_button = 0
        self.sprite_buttons = Group()

    def handle_input(self, event):
        self.sprite_buttons.update(event)

    def update(self, *args):
        self.sprite_buttons.update(*args)

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.sprite_buttons.draw(screen)

    def add_item(self, text, foo=lambda: None):
        button = Button(text, foo)
        button.set_pos((0, self.next_button))
        self.sprite_buttons.add(button)
        self.next_button += button.rect.height + 10
