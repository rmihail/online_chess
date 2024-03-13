import pygame
import chess

pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
fps = 120
board = chess.Board()

run = True
while run is True:
    timer.tick(fps)
    screen.fill('dark gray')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    print(board)

    pygame.display.flip()
pygame.quit()
