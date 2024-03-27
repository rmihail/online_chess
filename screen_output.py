import pygame
import chess
from constants import *

pygame.init()

# ширина, высота, объявление переменной экрана, ограничитель fps и переменная самой доски

screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

board = chess.Board()

font1 = pygame.font.Font(None, 40)


def print_pieces(screen_, piece_image_map):
    for square in chess.SQUARES:
        # проверка, есть ли в клетке фигура
        piece = board.piece_at(square)
        if piece is None:
            pass
        else:
            horizontal = square % 8
            vertical = square // 8
            screen_.blit(piece_image_map[str(piece)], (horizontal*100, 700 - vertical*100))


run = True
while run is True:
    timer.tick(FRAMES_PER_SECOND)
    screen.fill('dark gray')

    # рисование доски
    screen.blit(board_image, (0, 0))

    # display chess pieces on the screen
    print_pieces(screen, PIECE_IMAGE_MAP)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
