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
        file_index = chess.square_file(square)
        rank_index = chess.square_rank(square)
        rect = pygame.Rect(file_index * 100, 700 - rank_index * 100, 100, 100)
        pygame.draw.rect(screen, square_color, rect)
        piece = board.piece_at(square)
        if piece is not None and square != targeted_square:
            screen_.blit(piece_image_map[str(piece)], rect)
        if choosing_move:
            for legal_move in board.legal_moves:
                if legal_move.from_square == targeted_square:
                    move_to_x = (legal_move.to_square % 8) * 100
                    move_to_y = (7 - legal_move.to_square // 8) * 100
                    pygame.draw.rect(screen, POSSIBLE_MOVE_COLOR, (move_to_x, move_to_y, 100, 100), 3)
            if targeted_piece is not None:
                screen_.blit(piece_image_map[str(targeted_piece)], pygame.Rect(
                    pygame.mouse.get_pos()[0] - 50, pygame.mouse.get_pos()[1] - 50, 100, 100
                ))


def print_promotion_menu(screen_, to_square):
    menu_side = 0 if to_square < 60 else 1
    for square, piece in zip((to_square - 2, to_square - 1, to_square - 9, to_square - 10)
                             if menu_side == 0 else (to_square + 1, to_square + 2, to_square - 6, to_square - 7),
                             ('Q', 'R', 'B', 'N')):
        menu_square_coordinates = (chess.square_rank(square) * 100, -(chess.square_file(square) * 100), 100, 100)
        menu_rectangle = pygame.Rect(menu_square_coordinates[0], menu_square_coordinates[1], 100, 100)
        pygame.draw.rect(screen_, PROMOTION_MENU_COLOR, menu_rectangle)
        screen_.blit(PIECE_IMAGE_MAP[piece], (menu_square_coordinates[0], menu_square_coordinates[1]))


choosing_promotion = True
targeted_piece = None
targeted_square = None
choosing_move = False
run = True
while run is True:
    timer.tick(FRAMES_PER_SECOND)
    screen.fill('dark gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                targeted_square = event.pos[0] // 100 + (7 - event.pos[1] // 100) * 8
                choosing_move = True
                targeted_piece = board.piece_at(targeted_square)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                released_at = event.pos[0] // 100 + (7 - event.pos[1] // 100) * 8
                move = chess.Move(targeted_square, released_at)
                # if chess.square_rank(move.to_square) in (0, 7) and board.piece_at(move.to_square).symbol() == "P":
                #     choosing_promotion = True
                if move in board.legal_moves:
                    board.push(chess.Move(targeted_square, released_at))
            choosing_move = False
            targeted_square = None

        print_promotion_menu(screen, 60)
    # board printing
    print_board(screen, PIECE_IMAGE_MAP)

    pygame.display.flip()
pygame.quit()
