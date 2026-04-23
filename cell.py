import pygame


class Cell:
    def __init__(self, value, row, col, screen, cell_size = 60):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.cell_size = cell_size
        self.sketched_value = 0
        self.selected = False

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
    
        x = self.col * self.cell_size
        y = self.row * self.cell_size

        # fonts
        font = pygame.font.SysFont(None, 40)
        sketch_font = pygame.font.SysFont(None, 20)

        # draw main value (final number)
        if self.value != 0:
            text = font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + self.cell_size // 2, y + self.cell_size // 2))
            self.screen.blit(text, text_rect)

        # draw sketched value (small top-left number)
        elif self.sketched_value != 0:
            text = sketch_font.render(str(self.sketched_value), True, (128, 128, 128))
            self.screen.blit(text, (x + 5, y + 5))

        # draw selection border
        else:
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (x, y, self.cell_size, self.cell_size),
                1
            )
    def toggle_selected(self):
        self.selected = not self.selected
