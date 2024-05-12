import pygame
import chess
from stockfish import Stockfish
from constants import *

STOCKFISH_PARAMETERS = {
    "Debug Log File": "",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Threads": 1,
    "Ponder": "false",
    "Hash": 16,
    "MultiPV": 1,
    "Skill Level": 20,
    "Move Overhead": 10,
    "Minimum Thinking Time": 20,
    "Slow Mover": 100,
    "UCI_Chess960": "false",
    "UCI_LimitStrength": "false",
    "UCI_Elo": 1350
}
stockfish = Stockfish(path="C:/Users/User/PycharmProjects/online_chess/stockfish/stockfish-windows-x86-64-avx2.exe",
                      depth=18, parameters=STOCKFISH_PARAMETERS)
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
    file_index = chess.square_file(to_square)
    rank_index = chess.square_rank(to_square) + 1
    for piece_type in (chess.QUEEN, chess.ROOK, chess.BISHOP, chess.KNIGHT):
        rank_index -= 1

        rect = pygame.Rect(file_index * 100, 700 - rank_index * 100, 100, 100)
        pygame.draw.rect(screen, PROMOTION_MENU_COLOR, rect)

        piece = chess.Piece(piece_type, board.turn)
        screen_.blit(PIECE_IMAGE_MAP[piece.symbol()], rect)

        choosing_promotion[chess.square(file_index, rank_index)] = piece_type


choosing_promotion = {}
released_at = None
targeted_piece = None
targeted_square = None
choosing_move = False
run = True
while run is True:
    timer.tick(FRAMES_PER_SECOND)
    # screen.fill('dark gray')

    if board.turn is False:  # True - white to move
        stockfish.set_fen_position(board.fen())
        board.push(chess.Move.from_uci(stockfish.get_best_move()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not choosing_promotion:
                targeted_square = event.pos[0] // 100 + (7 - event.pos[1] // 100) * 8
                choosing_move = True
                targeted_piece = board.piece_at(targeted_square)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                released_at_ = event.pos[0] // 100 + (7 - event.pos[1] // 100) * 8
                promotion = choosing_promotion.get(released_at_)
                if choosing_promotion and not promotion:
                    choosing_promotion = {}
                    targeted_piece = None
                    targeted_square = None
                    continue
                if not choosing_promotion and chess.square_rank(released_at_) in (0, 7) and board.piece_at(targeted_square) is not None \
                        and board.piece_at(targeted_square).symbol() in ('P', 'p') \
                        and chess.Move(targeted_square, released_at_, promotion=chess.QUEEN) in board.legal_moves:  # проверка на возможность хода в эту клетку с превращением
                    print_promotion_menu(screen, released_at_)
                    released_at = released_at_
                else:
                    if promotion := choosing_promotion.get(released_at_):
                        choosing_promotion = {}
                    move = chess.Move(targeted_square, released_at or released_at_, promotion=promotion)
                    if move in board.legal_moves:
                        board.push(move)
                    choosing_move = False
                    targeted_square = None
                    released_at = None
                    choosing_promotion = {}

    # board printing
    if not choosing_promotion:
        print_board(screen, PIECE_IMAGE_MAP)

    pygame.display.flip()
pygame.quit()
