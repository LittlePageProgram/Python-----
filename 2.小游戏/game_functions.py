import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        new_bullet = Bullet(ship.rect.centerx, ship.rect.centery, ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship, ai_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, ai_settings, screen, bullets)


def update_screen(ai_settings, screen, ship, bg_pic, aliens, bullets):
    """更新屏幕图像，切换新屏幕"""
    # 重绘
    screen.fill(ai_settings.bg_color)
    bg_pic.biltme()

    for alien in aliens:
        alien.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet(bullets)

    ship.biltme()
    # 屏幕可见
    pygame.display.flip()

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    print(number_aliens_x)
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)