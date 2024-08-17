# main.py
import pygame
import sys
from settings import WIDTH, HEIGHT, FPS, BLACK
from player import Player
from enemy import Enemy
from tree import Tree

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survive the Wilderness")

# Định nghĩa màu sắc
WHITE = (255, 255, 255)  # Màu trắng
BLACK = (0, 0, 0)        # Màu đen
YELLOW = (255, 255, 0)   # Màu vàng (ban ngày)
DARK_BLUE = (0, 0, 139)  # Màu xanh đậm (ban đêm)

# Định nghĩa kích thước và vị trí của thanh trạng thái
status_bar_width = 200  # Chiều rộng của thanh trạng thái
status_bar_height = 20  # Chiều cao của thanh trạng thái
status_bar_x = (WIDTH - status_bar_width) // 2  # Vị trí x để căn giữa thanh trạng thái trên màn hình
status_bar_y = 10  # Vị trí y, đặt thanh trạng thái cách trên cùng 10 pixel


clock = pygame.time.Clock()
#thêm khái niệm cho ngày và đêm
day_time = True
time_counter = 0
day_length = 10000


# Tải hình ảnh cỏ để làm nền
grass_image = pygame.image.load("assets/grass.png").convert()

# Khởi tạo các đối tượng
player = Player()
enemies = pygame.sprite.Group()
trees = pygame.sprite.Group()

for _ in range(50):
    tree = Tree()
    trees.add(tree)

for _ in range(2):  # Giảm số lượng quái vật
    enemy = Enemy(player)
    enemies.add(enemy)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)
all_sprites.add(trees)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    # Khi thời gian chuyển từ ngày sang đêm
if not day_time and time_counter == 0:
    # Sinh ra quái vật khi đêm xuống
    for _ in range(2):  # Số lượng quái vật tùy theo bạn muốn
        enemy = Enemy(player)
        enemies.add(enemy)
    all_sprites.add(enemies)

# Khi thời gian chuyển từ đêm sang ngày
if day_time and time_counter == 0:
    # Xóa quái vật khi ngày lên
    enemies.empty()

            
    all_sprites.update()
      

    # Vẽ hình ảnh cỏ làm nền, lặp lại để phủ kín toàn bộ màn hình
    for x in range(0, WIDTH, grass_image.get_width()):
        for y in range(0, HEIGHT, grass_image.get_height()):
            screen.blit(grass_image, (x, y))
            
    # Vẽ thanh trạng thái ngày và đêm
    pygame.draw.rect(screen, WHITE, (status_bar_x, status_bar_y, status_bar_width, status_bar_height), 2)  # Khung viền
    filled_width = (time_counter / day_length) * status_bar_width
    if day_time:
        bar_color = YELLOW  # Sử dụng màu vàng cho ban ngày
    else:
        bar_color = DARK_BLUE  # Sử dụng màu xanh đậm cho ban đêm
    new_varnew_var = pygame.draw.rect(screen, bar_color, (status_bar_x, status_bar_y, filled_width, status_bar_height))
    


    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
