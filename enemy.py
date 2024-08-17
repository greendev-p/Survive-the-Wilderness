# enemy.py
import pygame
import random
from settings import WIDTH, HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.original_image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.original_image, (40, 40))  # Kích thước nhỏ bằng người chơi
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = 2  # Tốc độ di chuyển của quái vật
        self.player = player

    def update(self):
        # Tính toán hướng di chuyển của quái vật về phía người chơi
        dx, dy = self.player.rect.x - self.rect.x, self.player.rect.y - self.rect.y
        distance = (dx**2 + dy**2) ** 0.5
        if distance != 0:
            dx, dy = dx / distance, dy / distance  # Chuẩn hóa hướng

        # Cập nhật vị trí quái vật
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Kiểm tra nếu quái vật ra khỏi màn hình
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT