import pygame
import sys
from board import Board

screen_size = (650,600)
button_color = (220,231, 243)
button_text_color = (0,0,0)
background_color = (255,230,225)
grid_color = (50,50,150)
board_margin = 10
board_height = 390
board_width = screen_size[0] - 2 * board_margin - 135
cell_size = board_width // 9 
board_dimensions = (board_width, cell_size * 9)
board_offset_x = board_margin
board_offset_y = board_margin

pygame.init()
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font(None,36)

current_board = None
initial_board = None
in_game = False
win = False
lose = False

def draw_button(text, x, y, w = 150, h=50):
  pygame.draw.rect(screen, button_color, (x,y,w,h))
  text_surf = font.render(text, True, button_text_color)
  text_rect = text_surf.get_rect(center=(x+w/2, y+h/2))
  screen.blit(text_surf, text_rect)
  for i in range(4):
    pygame.draw.rect(screen, (0,0,0),(x,y,w,h),1)
  return pygame.Rect(x,y,w,h)

def handle_mouse_click(pos):
  global current_board, initial_board, in_game, lose
  if not in_game:
    while not in_game:
      if easy_btn.collidepoint(pos):
        current_board = Board(board_width, board_height, screen, 30)
        initial_board = current_board
        current_board.draw()
        in_game = True
      elif medium_btn.collidepoint(pos):
        current_board = Board(board_width, board_height, screen, 40)
        initiall_board = current_board
        current_board.draw()
        in_game = True
      elif hard_btn.collidepoint(pos):
        current_board = Board(board_width, board_height, screen, 50)
        initial_board = current_board
        current_board.draw()
        in_game = True
      else:
        break
  else:
    while in_game:
      if restart_btn.collidepoint(pos):
        current_board = None
        in_game = False
        lose = False
      elif reset_btn.collidepoint(pos):
        current_board.generate_initial_board()
        current_board.draw()
        break
      elif exit_btn.collidepoint(pos):
        pygame.quit()
        sys.exit()
      elif current_board.click(pos[0], pos[1]):
        break
      else:
        break
running = True
while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        handle_mouse_click(pygame.mouse.get_pos())

        if event.type == pygame.KEYUP:
          if current_board.cell_is_toggled:
            pos = pygame.mouse.get_pos()
            self_selected_cell = current_board.select(pos[0], pos[1])
            if event.key == pygame.K_1:
              current_board.sketch(1)
              current_board.draw()
            elif event.key == pygame.K_2:
              current_board.sketch(2)
              current_board.draw()
            elif event.key == pygame.K_3:
              current_board.sketch(3)
              current_board.draw()
            elif event.key == pygame.K_4:
              current_board.sketch(4)
              current_board.draw()
            elif event.key == pygame.K_5:
              current_board.sketch(5)
              current_board.draw()
            elif event.key == pygame.K_6:
              current_board.sketch(6)
              current_board.draw()
            elif event.key == pygame.K_7:
              current_board.sketch(7)
              current_board.draw()
            elif event.key == pygame.K_8:
              current_board.sketch(8)
              current_board.draw()
            elif event.key == pygame.K_9:
              current_board.sketch(9)
              current_board.draw()
            elif event.key == pygame.K_RETURN:
              current_board.place_number(None)
              current_board.draw()
            elif event.key == pygame.K_UP:
               if y > 70:
                 y = y - 40
                 current_board.click(x, y)
            elif event.key == pygame.K_DOWN:
              if y < BOARD_HEIGHT - 40:
                y = y + 40
                current_board.click(x, y)
            elif event.key == pygame.K_RIGHT:
              if x < BOARD_WIDTH - 40:
                x = x + 40
                current_board.click(x, y)
            elif event.key == pygame.K_LEFT:
              if x > 135+40:
                x = x - 40
                current_board.click(x, y)
            elif event.key == pygame.K_BACKSPACE:
              current_board.clear()
              current_board.draw()
  screen.fill(BACKGROUND_COLOR)

  if not in_game:
    welcome_text = font.render("Welcome to Whole Lota Sudoku, Press Play", True, (0, 0, 0))
    welcome_text_rect = welcome_text.get_rect(center=(SCREEN_SIZE[0] // 2, 150))
    screen.blit(welcome_text, welcome_text_rect)
    select_mode_text = font.render("Select game mode:", True, (0, 0, 0))
    select_mode_text_rect = select_mode_text.get_rect(center=(SCREEN_SIZE[0] // 2, 250))
    screen.blit(select_mode_text, select_mode_text_rect)
    easy_btn = draw_button("EASY", SCREEN_SIZE[0] // 2 - 75, 325)
    medium_btn = draw_button("MEDIUM", SCREEN_SIZE[0] // 2 - 75, 400)
    hard_btn = draw_button("HARD", SCREEN_SIZE[0] // 2 - 75, 475)
  else:
    if not win and not lose:
      current_board.draw()
      reset_btn = draw_button("RESET", screen_size[0] //2 - 225, 400, 125)
      restart_btn = draw_button("RESTART", SCREEN_SIZE[0] // 2 - 75, 400, 125)
      exit_btn = draw_button("EXIT", SCREEN_SIZE[0] // 2 + 75, 400, 125)

      if current_board.is_full():
        if current_board.check_board():
          win = True
        else:
          lose = True
    if win:
      current_board = None
      win_screen_text = font.render("Game Won!", True, (0, 0, 0))
      win_screen_text_rect = win_screen_text.get_rect(center=(SCREEN_SIZE[0] // 2, 200))
      screen.blit(win_screen_text, win_screen_text_rect)
      exit_btn = draw_button("EXIT", SCREEN_SIZE[0] // 2 - 75, 300, 150)
    elif lose:
      current_board = None
      lose_screen_text = font.render("Game Over :(", True, (0, 0, 0))
      lose_screen_text_rect = lose_screen_text.get_rect(center=(SCREEN_SIZE[0] // 2, 150))
      screen.blit(lose_screen_text, lose_screen_text_rect)
      restart_btn = draw_button("RESTART", SCREEN_SIZE[0] // 2 - 75, 300, 150)
  pygame.display.flip()
pygame.quit()




              


                           
