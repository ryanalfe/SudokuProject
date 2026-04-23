import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.rows = 9
    self.cols = 9
    self.cells = [[Cell(0, i, j, screen) for j in range(self.cols)] for i in range(self.rows)]
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty
    self.selected_cel = None
    self.board = None
    self.sudoku = None
    self.final_sudoku = None
    self.initial_sudoku = None
    self.generate_board()
    self.cell_is_toggled = False
    self.toggled_cell_pos = None

def generate_board(self):
  self.sudoku = SudokuGenerator(self.difficulty)
