import pygame
import chess
from print_functions.print_figures import print_figures

pygame.init()

# ширина, высота, объявление переменной экрана, ограничитель fps и переменная самой доски
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
fps = 120
board = chess.Board()

font1 = pygame.font.Font(None, 40)

# прописал координаты для удобства, для примера 19 клетка находится на 2 горизонтали
coordinates = {(0, 1, 2, 3, 4, 5, 6, 7): 0,
               (8, 9, 10, 11, 12, 13, 14, 15): 1,
               (16, 17, 18, 19, 20, 21, 22, 23): 2,
               (24, 25, 26, 27, 28, 29, 30, 31): 3,
               (32, 33, 34, 35, 36, 37, 38, 39): 4,
               (40, 41, 42, 43, 44, 45, 46, 47): 5,
               (48, 49, 50, 51, 52, 53, 54, 55): 6,
               (56, 57, 58, 59, 60, 61, 62, 63): 7}

# загрузка изображений для использования
pieces = {'p': pygame.image.load('images/black_pawn.png'),
          'n': pygame.image.load('images/black_knight.png'),
          'b': pygame.image.load('images/black_bishop.png'),
          'r': pygame.image.load('images/black_rook.png'),
          'q': pygame.image.load('images/black_queen.png'),
          'k': pygame.image.load('images/black_king.png'),
          'P': pygame.image.load('images/white_pawn.png'),
          'N': pygame.image.load('images/white_knight.png'),
          'B': pygame.image.load('images/white_bishop.png'),
          'R': pygame.image.load('images/white_rook.png'),
          'Q': pygame.image.load('images/white_queen.png'),
          'K': pygame.image.load('images/white_king.png'),
          }
board_image = pygame.image.load('images/board.png').convert()
# изменю размер изображений фигур
for symbol, piece_image in zip(pieces.keys(), pieces.values()):
    pieces[symbol] = pygame.transform.scale(piece_image, (100, 100))


run = True
while run is True:
    timer.tick(fps)
    screen.fill('dark gray')

    # рисование доски
    screen.blit(board_image, (0, 0))

    print_figures(screen, board, coordinates, pieces)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
