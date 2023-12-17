import pygame
from pygame import Rect, Surface
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, text, foo=lambda: None, *groups):
        super().__init__(*groups)
        self.text = text
        self.on_click = foo
        self.is_active = False
        self.rect = Rect((0, 0, 100, 50))
        self.image = Surface(self.rect.size)
        self.render(self.image)

    def set_size(self, size):
        self.rect.width, self.rect.height = size

    def set_pos(self, pos):
        self.rect.x, self.rect.y = pos

    def update(self, *args):
        if not args:
            return

        if args[0].type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(args[0].pos):
                if not self.is_active:
                    self.is_active = True
                    self.render(self.image)
            else:
                if self.is_active:
                    self.is_active = False
                    self.render(self.image)

        elif (args[0].type == pygame.MOUSEBUTTONDOWN
              and self.rect.collidepoint(args[0].pos)):
            self.on_click()

    def render(self, screen):
        if self.is_active:
            color = (200, 100, 100)
        else:
            color = (100, 200, 100)
        pygame.draw.rect(screen, color, ((0, 0), self.rect.size))
