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

board_image = pygame.image.load('images/board.png')
# scale images
for symbol, piece_image in zip(PIECE_IMAGE_MAP.keys(), PIECE_IMAGE_MAP.values()):
    PIECE_IMAGE_MAP[symbol] = pygame.transform.scale(piece_image, (100, 100))
