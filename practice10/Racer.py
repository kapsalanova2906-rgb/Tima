import pygame
import random
import sys
import os

pygame.init()

WIDTH = 400
HEIGHT = 600
FPS = 60

# игровое окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 20)

WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
ORANGE = (255, 140, 0)
RED = (255, 0, 0)

# ПУТИ
BASE_DIR = os.path.dirname(__file__)
IMG_DIR = os.path.join(BASE_DIR, "images")

# ЗАГРУЗКА КАРТИНОК
player_img = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert_alpha()
enemy_img = pygame.image.load(os.path.join(IMG_DIR, "enemy.png")).convert_alpha()
coin_img = pygame.image.load(os.path.join(IMG_DIR, "coin.png")).convert_alpha()
coin_img = pygame.transform.rotate(coin_img, 90)

# дорога
road_path = os.path.join(IMG_DIR, "road.png")
if os.path.exists(road_path):
    road_img = pygame.image.load(road_path).convert()
    road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
else:
    road_img = None

# размеры картинок
player_img = pygame.transform.scale(player_img, (50, 90))
enemy_img = pygame.transform.scale(enemy_img, (50, 90))
coin_img = pygame.transform.scale(coin_img, (30, 30))

# границы дороги
road_left = 80
road_right = WIDTH - 80

# количество монет, после которого увеличивается скорость врагов
N = 5


class Player(pygame.sprite.Sprite):
    # класс игрока
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 100))
        self.speed = 6

    def update(self):
        # движение игрока по клавишам
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # не даём выехать за пределы дороги
        if self.rect.left < road_left:
            self.rect.left = road_left
        if self.rect.right > road_right:
            self.rect.right = road_right


class Enemy(pygame.sprite.Sprite):
    # класс вражеской машины
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        x = random.randint(road_left, road_right - 50)
        self.rect = self.image.get_rect(topleft=(x, -100))
        self.base_speed = random.randint(4, 7)
        self.speed = self.base_speed

    def update(self):
        # движение врага вниз
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        # перенос врага снова наверх
        self.rect.y = -100
        self.rect.x = random.randint(road_left, road_right - 50)
        self.base_speed = random.randint(4, 7)
        self.speed = self.base_speed + speed_bonus


class Coin(pygame.sprite.Sprite):
    # класс монеты
    def __init__(self):
        super().__init__()

        # случайный вес монеты
        self.weight = random.randint(1, 3)

        # копируем исходную картинку монеты
        self.image = coin_img.copy()

        # задаём значение очков в зависимости от веса
        if self.weight == 1:
            self.value = 1
            self.tint = YELLOW
        elif self.weight == 2:
            self.value = 2
            self.tint = ORANGE
        else:
            self.value = 3
            self.tint = RED

        # слегка подкрашиваем монету для различия по весу
        tint_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        tint_surface.fill((*self.tint, 80))
        self.image.blit(tint_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

        # случайная позиция монеты на дороге
        x = random.randint(road_left, road_right - 30)
        self.rect = self.image.get_rect(topleft=(x, -50))
        self.speed = 5

    def update(self):
        # движение монеты вниз
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()


player = Player()
player_group = pygame.sprite.Group(player)

enemy_group = pygame.sprite.Group()
for _ in range(3):
    enemy_group.add(Enemy())

coin_group = pygame.sprite.Group()

coins = 0
score = 0
coin_timer = 0
game_over = False

# бонус к скорости врагов
speed_bonus = 0

while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        # закрытие окна
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # обновляем игрока, врагов и монеты
        player_group.update()
        enemy_group.update()
        coin_group.update()

        # таймер появления новых монет
        coin_timer += 1
        if coin_timer >= 60:
            coin_timer = 0
            coin_group.add(Coin())

        # сбор монет
        collected_coins = pygame.sprite.spritecollide(player, coin_group, True)
        if collected_coins:
            for coin in collected_coins:
                coins += coin.value
                score += coin.value * 10

            # увеличение скорости врагов после каждых N монет
            new_speed_bonus = coins // N
            if new_speed_bonus > speed_bonus:
                speed_bonus = new_speed_bonus
                for enemy in enemy_group:
                    enemy.speed = enemy.base_speed + speed_bonus

        # столкновение с врагом
        if pygame.sprite.spritecollideany(player, enemy_group):
            game_over = True

        # очки за выживание
        score += 1

    # ФОН
    if road_img is not None:
        screen.blit(road_img, (0, 0))
    else:
        screen.fill((50, 50, 50))

    # ОТРИСОВКА
    player_group.draw(screen)
    enemy_group.draw(screen)
    coin_group.draw(screen)

    # ТЕКСТ
    score_text = font.render(f"Score: {score}", True, WHITE)
    coin_text = font.render(f"Coins: {coins}", True, WHITE)
    speed_text = font.render(f"Speed lvl: {speed_bonus}", True, WHITE)

    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (WIDTH - 120, 10))
    screen.blit(speed_text, (10, 35))

    # надпись при проигрыше
    if game_over:
        over = font.render("GAME OVER", True, WHITE)
        screen.blit(over, (WIDTH // 2 - 80, HEIGHT // 2))

    pygame.display.flip()