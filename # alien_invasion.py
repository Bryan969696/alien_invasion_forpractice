# alien_invasion.py
import sys
import pygame
# 创建用户窗口及响应用户输入
class AlienInvasion:
# 管理游戏资源和行为的类
    def __init__(self):
        # 初始化游戏并创建游戏资源
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()