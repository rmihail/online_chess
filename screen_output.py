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
board_text = font1.render(str(board), 1, (180, 180, 180))

run = True
while run is True:
    timer.tick(fps)
    screen.fill('dark gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(board_text, (10, 50))

    pygame.display.flip()
pygame.quit()
