import pygame


class BackGroundPicture():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/sky.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def biltme(self):
        self.screen.blit(self.image, self.rect)