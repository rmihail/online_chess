import pygame
import chess
from constants import *

pygame.init()

# ширина, высота, объявление переменной экрана, ограничитель fps и переменная самой доски

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

board = chess.Board()

font1 = pygame.font.Font(None, 40)
BLACK_SQUARE_COLOR = (160, 160, 160)
WHITE_SQUARE_COLOR = (255, 255, 255)


def print_pieces(screen_, piece_image_map):
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            pass
        else:
            horizontal = square % 8
            vertical = square // 8
            screen_.blit(piece_image_map[str(piece)], (horizontal*100, 700 - vertical*100))


def print_board():
    for square in chess.SQUARES:
        vertical_is_even = True if square // 8 % 2 == 0 else False
        if vertical_is_even is True:
            if square % 2 == 0:
                square_color = BLACK_SQUARE_COLOR
            else:
                square_color = WHITE_SQUARE_COLOR
        else:
            if square % 2 == 0:
                square_color = WHITE_SQUARE_COLOR
            else:
                square_color = BLACK_SQUARE_COLOR
        pygame.draw.rect(screen, square_color, squares_rects[square])


squares_rects = {}
for square in chess.SQUARES:
    squares_rects[square] = pygame.Rect(square % 8*100, 700 - square // 8*100, 100, 100)

run = True
while run is True:
    timer.tick(FRAMES_PER_SECOND)
    screen.fill('dark gray')

    # board printing
    print_board()

    # display chess pieces on the screen
    print_pieces(screen, PIECE_IMAGE_MAP)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                targeted_square = event.pos[0] // 100 + (7 - event.pos[1] // 100)*8

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                released_at = event.pos[0] // 100 + (7 - event.pos[1] // 100)*8
                board.push(chess.Move(targeted_square, released_at))

    pygame.display.flip()
pygame.quit()
