# Sudoku Game

An interactive Sudoku game developed in Python using Pygame.

The application generates randomized Sudoku boards, provides multiple difficulty levels, and allows users to solve puzzles through a graphical interface using mouse and keyboard controls.

This project was developed collaboratively as a group course project. My contributions included implementation, debugging, and integration work across the game's board management, cell behavior, user interface, and Sudoku generation components.

## Features

- Interactive graphical interface built with Pygame
- Easy, Medium, and Hard difficulty levels
- Random Sudoku board generation
- Mouse-based cell selection
- Keyboard and number-pad input
- Candidate / sketched number entry
- Arrow-key navigation between cells
- Reset, restart, and exit controls
- Automatic board-completion validation
- Win and loss screens

## How It Works

The application is organized into separate components responsible for puzzle generation, board management, individual cells, and the main game loop.

### Puzzle Generation

The Sudoku generator first constructs a completed 9×9 Sudoku grid while enforcing the standard Sudoku constraints:

- Each number may appear only once per row
- Each number may appear only once per column
- Each number may appear only once per 3×3 subgrid

The remaining cells are filled recursively using backtracking. After a completed grid is generated, cells are randomly removed to create the playable puzzle.

The number of removed cells depends on the selected difficulty:

| Difficulty | Cells Removed |
| --- | ---: |
| Easy | 30 |
| Medium | 40 |
| Hard | 50 |

### Game Board

The `Board` class manages the current state of the puzzle, including:

- Generating a new puzzle
- Tracking the original and completed boards
- Selecting cells
- Placing and clearing values
- Storing candidate values
- Resetting the board
- Checking whether the completed puzzle matches the generated solution

### User Interface

The main game loop handles user interaction and transitions between the menu, active game, win, and loss states.

Players can:

- Select cells using the mouse
- Enter candidate values with the keyboard
- Confirm values with Enter
- Clear entries with Backspace or Delete
- Navigate the board with the arrow keys
- Reset the current puzzle
- Restart with a new difficulty
- Exit the application

## Project Structure

```text
SudokuProject/
│
├── sudoku.py
├── sudoku_generator.py
├── board.py
├── cell.py
├── main.sh
└── README.md
