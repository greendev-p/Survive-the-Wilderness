# tree.py
import pygame
import random
from settings import WIDTH, HEIGHT, TREE_COLOR # type: ignore

class Tree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("assets/tree.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (50, 50))  
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
