import pygame
import chess

pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
fps = 120
board = chess.Board()

font1 = pygame.font.Font(None, 40)

coordinates = {(0, 1, 2, 3, 4, 5, 6, 7): 0,
               (8, 9, 10, 11, 12, 13, 14, 15): 1,
               (16, 17, 18, 19, 20, 21, 22, 23): 2,
               (24, 25, 26, 27, 28, 29, 30, 31): 3,
               (32, 33, 34, 35, 36, 37, 38, 39): 4,
               (40, 41, 42, 43, 44, 45, 46, 47): 5,
               (48, 49, 50, 51, 52, 53, 54, 55): 6,
               (56, 57, 58, 59, 60, 61, 62, 63): 7}

pieces = {'p': pygame.image.load('images/black_pawn.png').convert(),
          'n': pygame.image.load('images/black_knight.png').convert(),
          'b': pygame.image.load('images/black_bishop.png').convert(),
          'r': pygame.image.load('images/black_rook.png').convert(),
          'q': pygame.image.load('images/black_queen.png').convert(),
          'k': pygame.image.load('images/black_king.png').convert(),
          'P': pygame.image.load('images/white_pawn.png').convert(),
          'N': pygame.image.load('images/white_knight.png').convert(),
          'B': pygame.image.load('images/white_bishop.png').convert(),
          'R': pygame.image.load('images/white_rook.png').convert(),
          'Q': pygame.image.load('images/white_queen.png').convert(),
          'K': pygame.image.load('images/white_king.png').convert(),
          }
board_image = pygame.image.load('images/board.png').convert()

run = True
while run is True:
    timer.tick(fps)
    screen.fill('dark gray')

    screen.blit(board_image, (0, 0))

    f_piece_map = board.piece_map()
    for square in range(64):
        piece = board.piece_at(square)
        if piece is None:
            pass
        else:
            for key in coordinates.keys():
                if square in key:
                    horizontal = coordinates[key]
            screen.blit(pieces[str(piece)], ((square % 8)*100, 700-(square//8)*100))  # тут я напишу свое расположение на доске, сейчас краденное со статьи

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
