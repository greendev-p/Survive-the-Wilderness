# player.py
import pygame
from settings import WIDTH, HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Tải hình ảnh và thay đổi kích thước nó
        self.original_image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (40, 40))  # Kích thước nhỏ hơn
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3.5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
