import pygame

from game_state_manager import IState

green = (0, 255, 0)


class Game(IState):
    def __init__(self, *args):
        super().__init__(*args)
        self.dragging = False
        self.square_x, self.square_y = 0, 0
        self.offset_x, self.offset_y = 0, 0
        self.square_size = 100

    def update(self):
        if self.dragging:
            self.square_x, self.square_y = pygame.mouse.get_pos()
            self.square_x -= self.offset_x
            self.square_y -= self.offset_y

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, green,
                         (self.square_x, self.square_y,
                          self.square_size, self.square_size))

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.square_x <= event.pos[
                    0] <= self.square_x + self.square_size and self.square_y \
                        <= event.pos[1] <= self.square_y + self.square_size:
                    self.dragging = True
                    self.offset_x = event.pos[0] - self.square_x
                    self.offset_y = event.pos[1] - self.square_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False
