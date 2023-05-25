import pygame
import math
from colors import Background, Black
from board import full_board, has_won
from minimax import best_move
pygame.init()
WIDTH = 500
ROWS = 3
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("TicTacToe")
X_IMAGE = pygame.transform.scale(pygame.image.load("Images/x.png"), (150, 150))
O_IMAGE = pygame.transform.scale(pygame.image.load("Images/o.png"), (150, 150))
END_FONT = pygame.font.SysFont('courier', 40)
screen.fill(Background)
turn = 1
grid = [[0] * ROWS for _ in range(ROWS)]
def draw_grid():
    gap = WIDTH // ROWS
    x = 0
    for i in range(ROWS):
        x = i * gap
        pygame.draw.line(screen, Black, (x, 0), (x, WIDTH), 3)
        pygame.draw.line(screen, Black, (0, x), (WIDTH, x), 3)
def on_click(grid):
    global turn, images
    m_x, m_y = pygame.mouse.get_pos()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
             x = (WIDTH // ROWS // 2) * (2 * i + 1)
             y = (WIDTH // ROWS // 2) * (2 * j + 1)
             dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
             if dis < WIDTH // ROWS // 2 and grid[i][j] == 0:
                grid[i][j] = turn
                turn = 2
                if not has_won(grid) or not full_board(grid):
                    move = best_move(grid, turn)
                    grid[move["x"]][move["y"]] = turn
                    turn = 1
def display_message(content):
    pygame.time.delay(500)
    screen.fill(Background)
    end_text = END_FONT.render(content, 1, Black)
    screen.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(3000)
def render():
    screen.fill(Background)
    draw_grid()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
             position = grid[i][j]
             images = [None, X_IMAGE, O_IMAGE]
             if position > 0:
                  IMAGE = images[position]
                  x = (WIDTH // ROWS // 2) * (2 * i + 1)
                  y = (WIDTH // ROWS // 2) * (2 * j + 1)
                  screen.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    pygame.display.update()

running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                on_click(grid)
            
        render()
        if has_won(grid) or full_board(grid):
            if has_won:
                display_message(["O", "X"][turn] + " has won!")

pygame.quit()