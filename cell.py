import pygame


class Cell:
    def __init__(self, value, row, col, screen, is_original=False):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.is_original = is_original
        self.cell_size = 60

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * self.cell_size
        y = self.row * self.cell_size

        font = pygame.font.SysFont(None, 40)
        sketch_font = pygame.font.SysFont(None, 20)

        # draw final number
        if self.value != 0:
            color = (0, 0, 0) if self.is_original else (120, 120, 120)
            text = font.render(str(self.value), True, color)
            text_rect = text.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
            self.screen.blit(text, text_rect)

        # draw sketched value
        elif self.sketched_value != 0:
            text = sketch_font.render(str(self.sketched_value), True, (160, 160, 160))
            self.screen.blit(text, (x + 5, y + 5))

        # draw selected border
        if self.selected:
            pygame.draw.rect(
                self.screen,
                (255, 0, 0),
                (x, y, self.cell_size, self.cell_size),
                3
            )
    def toggle_selected(self):
        self.selected = not self.selected
