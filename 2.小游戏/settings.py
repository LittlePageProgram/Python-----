import pygame

class Settings():
    """
    存储设置类
    """
    def __init__(self):
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        self.ship_spped_factor = 10
        self.bullet_speed_factor = 20
        self.bullet_color = (255, 255, 0)
        self.bullet_width = 5
        self.bullet_height = 25