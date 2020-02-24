import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))

ball = pygame.image.load('./1.jpg')

ball_rect = ball.get_rect()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(ball, ball_rect)

