import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from bg_pic import BackGroundPicture
from pygame.sprite import Group
from alien import Alien

"""
游戏入口
"""



def run_game():
    """
    初始化游戏并创建一个屏幕对象
    """
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # 飞船
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    bg_pic = BackGroundPicture(screen)
    pygame.display.flip()
    gf.create_fleet(ai_settings, screen, aliens)

    # 背景
    while True:
        # 鼠标和键盘事件
        gf.check_events(ship, ai_settings, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, bg_pic, aliens, bullets)




run_game()