import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.rows = 9
        self.cols = 9
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.cell_size = width // 9
        self.cells = [[Cell(0, i, j, screen) for j in range(self.cols)] for i in range(self.rows)]
        self.selected_cell = None
        self.board = None
        self.sudoku = None
        self.final_sudoku = None
        self.initial_sudoku = None
        self.generate_board()
        self.cell_is_toggled = False
        self.toggled_cell_pos = None
    def generate_board(self):
        if self.difficulty == "easy":
            removed = 30
        elif self.difficulty == "medium":
            removed = 40
        else:
            removed = 50
        self.sudoku = SudokuGenerator(9, removed)
        self.sudoku.fill_values()
        self.final_sudoku = [row[:] for row in self.sudoku.board]
        self.sudoku.remove_cells()
        self.board = self.sudoku.get_board()
        self.initial_sudoku = [row[:] for row in self.board]
        for i in range(self.rows):
            for j in range(self.cols):
                value = self.board[i][j]
                is_original = value != 0

                self.cells[i][j] = Cell(value, i, j, self.screen, is_original)
    def draw(self):
        for i in range(10):
            thickness = 4 if i % 3 == 0 else 1

            pygame.draw.line(self.screen, (0, 0, 0),
                             (i * self.cell_size, 0),
                             (i * self.cell_size, self.height),
                             thickness)

            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, i * self.cell_size),
                             (self.width, i * self.cell_size),
                             thickness)
        for row in self.cells:
            for cell in row:
                cell.draw()
    def select(self, row, col):
        # unselect all
        for r in self.cells:
            for c in r:
                c.selected = False
        self.cells[row][col].selected = True
        self.selected_cell = (row, col)
    def click(self, x, y):
        if x < self.width and y < self.height:
            row = y // self.cell_size
            col = x // self.cell_size
            return (row, col)
        return None
    def clear(self):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.initial_sudoku[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)
    def sketch(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.cells[row][col].value == 0:
                self.cells[row][col].set_sketched_value(value)
    def place_number(self, value):
        if self.selected_cell:
            row, col = self.selected_cell
            if self.initial_sudoku[row][col] == 0:
                self.cells[row][col].set_cell_value(value)
                self.cells[row][col].set_sketched_value(0)
    def reset_to_original(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].set_cell_value(self.initial_sudoku[i][j])
                self.cells[i][j].set_sketched_value(0)
    def is_full(self):
        for row in self.cells:
            for cell in row:
                if cell.value == 0:
                    return False
        return True
    def update_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.board[i][j] = self.cells[i][j].value
    def find_empty(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value == 0:
                    return (i, j)
        return None
    def check_board(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].value != self.final_sudoku[i][j]:
                    return False
        return True
