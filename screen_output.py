import pygame
import chess
from constants import *

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()

board = chess.Board()


def print_board(screen_, piece_image_map):
    for square in chess.SQUARES:
        square_color = BLACK_SQUARE_COLOR if (square % 8 + square // 8) % 2 == 0 else WHITE_SQUARE_COLOR
        horizontal = square % 8
        vertical = square // 8
        rect = pygame.Rect(horizontal*100, 700 - vertical*100, 100, 100)
        pygame.draw.rect(screen, square_color, rect)
        piece = board.piece_at(square)
        if piece is not None:
            screen_.blit(piece_image_map[str(piece)], rect)


run = True
while run is True:
    timer.tick(FRAMES_PER_SECOND)
    screen.fill('dark gray')

    # board printing
    print_board(screen, PIECE_IMAGE_MAP)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                targeted_square = event.pos[0] // 100 + (7 - event.pos[1] // 100)*8

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                released_at = event.pos[0] // 100 + (7 - event.pos[1] // 100)*8
                if chess.Move(targeted_square, released_at) in board.legal_moves:
                    board.push(chess.Move(targeted_square, released_at))

    pygame.display.flip()
pygame.quit()
