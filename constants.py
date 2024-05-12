"""
File containing settings constants
"""
import pygame

# screen size
WIDTH, HEIGHT = 800, 800
FRAMES_PER_SECOND = 60

# load images
PIECE_IMAGE_MAP = {'p': pygame.image.load('images/black_pawn.png'),
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

# scale images
for symbol, piece_image in zip(PIECE_IMAGE_MAP.keys(), PIECE_IMAGE_MAP.values()):
    PIECE_IMAGE_MAP[symbol] = pygame.transform.scale(piece_image, (100, 100))


BLACK_SQUARE_COLOR = (120, 160, 160)
WHITE_SQUARE_COLOR = (240, 255, 255)
POSSIBLE_MOVE_COLOR = (10, 255, 100)
PROMOTION_MENU_COLOR = (160, 210, 210)
CHECKED_KING_COLOR = (222, 17, 58)
