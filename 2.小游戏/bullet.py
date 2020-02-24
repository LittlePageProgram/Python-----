import pygame
from pygame.sprite import  Sprite


class Bullet(Sprite):
    """子弹"""

    def __init__(self, x, y, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(x, y, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self, bullets):
        self.y -= self.speed_factor
        self.rect.y = self.y

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

    def draw_bullet(self, bullets):
        self.update(bullets)
        pygame.draw.rect(self.screen, self.color, self.rect)