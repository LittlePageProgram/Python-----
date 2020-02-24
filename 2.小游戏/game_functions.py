import sys
import pygame


def check_events(ship):
    """响应案件和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False


def update_screen(ai_settings, screen, ship, bg_pic):
    """更新屏幕图像，切换新屏幕"""
    # 重绘
    screen.fill(ai_settings.bg_color)
    bg_pic.biltme()
    ship.biltme()
    # 屏幕可见
    pygame.display.flip()