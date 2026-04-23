import sys
import pygame
from board import Board


SCREEN_WIDTH = 540
SCREEN_HEIGHT = 660
BOARD_SIZE = 540
BACKGROUND_COLOR = (255, 255, 200)
BUTTON_COLOR = (220, 231, 243)
BUTTON_TEXT_COLOR = (0, 0, 0)
TITLE_COLOR = (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")
title_font = pygame.font.Font(None, 48)
text_font = pygame.font.Font(None, 36)


def draw_button(rect, text):
    pygame.draw.rect(screen, BUTTON_COLOR, rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)
    text_surf = text_font.render(text, True, BUTTON_TEXT_COLOR)
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)


def move_selection(board, row_change, col_change):
    if board.selected_cell is None:
        board.select(0, 0)
        return

    row, col = board.selected_cell
    new_row = max(0, min(8, row + row_change))
    new_col = max(0, min(8, col + col_change))
    board.select(new_row, new_col)


def update_game_state(board, current_state):
    if board is not None and board.is_full():
        return "win" if board.check_board() else "lose"
    return current_state


def draw_menu():
    screen.fill(BACKGROUND_COLOR)
    title = title_font.render("Welcome to Whole Lota Sudoku", True, TITLE_COLOR)
    subtitle = text_font.render("Select game mode:", True, TITLE_COLOR)
    screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 120)))
    screen.blit(subtitle, subtitle.get_rect(center=(SCREEN_WIDTH // 2, 180)))
    draw_button(EASY_BUTTON, "EASY")
    draw_button(MEDIUM_BUTTON, "MEDIUM")
    draw_button(HARD_BUTTON, "HARD")


def draw_game(board):
    screen.fill(BACKGROUND_COLOR)
    board.draw()
    draw_button(RESET_BUTTON, "RESET")
    draw_button(RESTART_BUTTON, "RESTART")
    draw_button(EXIT_BUTTON, "EXIT")


def draw_end_screen(message):
    screen.fill(BACKGROUND_COLOR)
    message_surface = title_font.render(message, True, TITLE_COLOR)
    screen.blit(message_surface, message_surface.get_rect(center=(SCREEN_WIDTH // 2, 170)))
    draw_button(END_RESTART_BUTTON, "RESTART")
    draw_button(END_EXIT_BUTTON, "EXIT")


EASY_BUTTON = pygame.Rect(60, 240, 120, 50)
MEDIUM_BUTTON = pygame.Rect(210, 240, 120, 50)
HARD_BUTTON = pygame.Rect(360, 240, 120, 50)

RESET_BUTTON = pygame.Rect(20, 585, 150, 45)
RESTART_BUTTON = pygame.Rect(195, 585, 150, 45)
EXIT_BUTTON = pygame.Rect(370, 585, 150, 45)

END_RESTART_BUTTON = pygame.Rect(110, 280, 140, 50)
END_EXIT_BUTTON = pygame.Rect(290, 280, 140, 50)


current_board = None
game_state = "menu"
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if game_state == "menu":
                if EASY_BUTTON.collidepoint(event.pos):
                    current_board = Board(BOARD_SIZE, BOARD_SIZE, screen, "easy")
                    game_state = "playing"
                elif MEDIUM_BUTTON.collidepoint(event.pos):
                    current_board = Board(BOARD_SIZE, BOARD_SIZE, screen, "medium")
                    game_state = "playing"
                elif HARD_BUTTON.collidepoint(event.pos):
                    current_board = Board(BOARD_SIZE, BOARD_SIZE, screen, "hard")
                    game_state = "playing"

            elif game_state == "playing":
                if RESET_BUTTON.collidepoint(event.pos):
                    current_board.reset_to_original()
                elif RESTART_BUTTON.collidepoint(event.pos):
                    current_board = None
                    game_state = "menu"
                elif EXIT_BUTTON.collidepoint(event.pos):
                    running = False
                else:
                    current_board.click(mouse_x, mouse_y)

            elif game_state in ("win", "lose"):
                if END_RESTART_BUTTON.collidepoint(event.pos):
                    current_board = None
                    game_state = "menu"
                elif END_EXIT_BUTTON.collidepoint(event.pos):
                    running = False

        elif event.type == pygame.KEYDOWN and game_state == "playing" and current_board is not None:
            if event.key in (pygame.K_1, pygame.K_KP1):
                current_board.sketch(1)
            elif event.key in (pygame.K_2, pygame.K_KP2):
                current_board.sketch(2)
            elif event.key in (pygame.K_3, pygame.K_KP3):
                current_board.sketch(3)
            elif event.key in (pygame.K_4, pygame.K_KP4):
                current_board.sketch(4)
            elif event.key in (pygame.K_5, pygame.K_KP5):
                current_board.sketch(5)
            elif event.key in (pygame.K_6, pygame.K_KP6):
                current_board.sketch(6)
            elif event.key in (pygame.K_7, pygame.K_KP7):
                current_board.sketch(7)
            elif event.key in (pygame.K_8, pygame.K_KP8):
                current_board.sketch(8)
            elif event.key in (pygame.K_9, pygame.K_KP9):
                current_board.sketch(9)
            elif event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                current_board.clear()
            elif event.key == pygame.K_RETURN:
                if current_board.selected_cell is not None:
                    row, col = current_board.selected_cell
                    value = current_board.cells[row][col].sketched_value
                    if value != 0:
                        current_board.place_number(value)
            elif event.key == pygame.K_UP:
                move_selection(current_board, -1, 0)
            elif event.key == pygame.K_DOWN:
                move_selection(current_board, 1, 0)
            elif event.key == pygame.K_LEFT:
                move_selection(current_board, 0, -1)
            elif event.key == pygame.K_RIGHT:
                move_selection(current_board, 0, 1)

            game_state = update_game_state(current_board, game_state)

    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game(current_board)
    elif game_state == "win":
        draw_end_screen("Game Won!")
    elif game_state == "lose":
        draw_end_screen("Game Over :(")

    pygame.display.flip()

pygame.quit()
sys.exit()
