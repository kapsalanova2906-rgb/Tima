import datetime  # работа с текущим временем (часы, минуты, секунды)
import os        # работа с путями к файлам

import pygame    # библиотека для графики и игр


# масштабирует точку при изменении размера изображения
def scale_point(point, original_size, new_size):
    original_width, original_height = original_size  # старые размеры
    new_width, new_height = new_size                  # новые размеры
    x, y = point                                     # координаты точки

    # пересчёт координат под новый размер
    scaled_x = round(x * new_width / original_width)
    scaled_y = round(y * new_height / original_height)
    return (scaled_x, scaled_y)


# возвращает точку опоры (центр снизу изображения)
def bottom_center_pivot(size, bottom_offset=0):
    width, height = size
    return (width // 2, height - bottom_offset)  # центр по X, низ по Y


# --- настройки окна и цветов ---
WIDTH, HEIGHT = 900, 700  # размер окна
FPS = 30                  # FPS (кадров в секунду)
BACKGROUND_COLOR = (245, 245, 245)  # цвет фона
TEXT_COLOR = (40, 40, 40)           # цвет текста
ACCENT_COLOR = (220, 60, 60)        # дополнительный цвет (акцент)

# путь к папке с картинками
IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# имена файлов изображений
CLOCK_FACE_FILE = "clock_face.png"
MICKEY_FILE = "mickey.png"
LEFT_HAND_FILE = "left_hand.png"
RIGHT_HAND_FILE = "right_hand.png"

# размеры и позиции элементов
CLOCK_FACE_SIZE = (800, 600)
CLOCK_FACE_CENTER = (WIDTH // 2, HEIGHT // 2 + 20)

MICKEY_SIZE = (350, 350)
MICKEY_CENTER = (WIDTH // 2, HEIGHT // 2)

LEFT_HAND_SIZE = (50, 150)
LEFT_HAND_CENTER = (WIDTH // 2 + 4, HEIGHT // 2 + 5)
LEFT_HAND_PIVOT = bottom_center_pivot(LEFT_HAND_SIZE, bottom_offset=10)

RIGHT_HAND_SIZE = (100, 100)
RIGHT_HAND_CENTER = (WIDTH // 2 - 5, HEIGHT // 2 + 4)
RIGHT_HAND_PIVOT = bottom_center_pivot(RIGHT_HAND_SIZE, bottom_offset=10)

CENTER_DOT_POSITION = (WIDTH // 2, HEIGHT // 2)  # центр часов
TIME_TEXT_POSITION = (WIDTH // 2, HEIGHT - 50)   # позиция текста времени

# fallback (если нет картинок)
FALLBACK_CLOCK_RADIUS = 220
FALLBACK_MICKEY_HEAD_RADIUS = 80
FALLBACK_LEFT_HAND_LENGTH = 180
FALLBACK_RIGHT_HAND_LENGTH = 150


# загрузка изображения
def load_image(file_name):
    path = os.path.join(IMAGES_DIR, file_name)  # полный путь
    if os.path.exists(path):                   # если файл существует
        return pygame.image.load(path).convert_alpha()  # загрузка PNG
    return None  # если файла нет


# изменение размера изображения
def scale_image(image, size):
    if image is None:
        return None
    return pygame.transform.smoothscale(image, size)  # качественное масштабирование


# вращение изображения вокруг центра
def rotate_center(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)  # поворот
    rotated_rect = rotated_image.get_rect(center=center)   # центрируем
    return rotated_image, rotated_rect


# вращение изображения вокруг заданной точки (pivot)
def rotate_around_pivot(image, angle, position, pivot):
    # создаём прямоугольник изображения
    image_rect = image.get_rect(topleft=(position[0] - pivot[0], position[1] - pivot[1]))

    # считаем смещение центра
    offset = pygame.math.Vector2(position) - image_rect.center
    rotated_offset = offset.rotate(-angle)  # вращаем смещение

    rotated_image = pygame.transform.rotate(image, angle)  # поворот картинки

    # новая позиция центра
    rotated_center = (position[0] - rotated_offset.x, position[1] - rotated_offset.y)
    rotated_rect = rotated_image.get_rect(center=rotated_center)

    return rotated_image, rotated_rect


class MickeyClock:
    def __init__(self):
        # загрузка и масштабирование изображений
        self.clock_face = scale_image(load_image(CLOCK_FACE_FILE), CLOCK_FACE_SIZE)
        self.mickey = scale_image(load_image(MICKEY_FILE), MICKEY_SIZE)
        self.left_hand = scale_image(load_image(LEFT_HAND_FILE), LEFT_HAND_SIZE)
        self.right_hand = scale_image(load_image(RIGHT_HAND_FILE), RIGHT_HAND_SIZE)

    # получение углов стрелок
    def get_angles(self):
        now = datetime.datetime.now()  # текущее время
        minutes = now.minute
        seconds = now.second

        # расчёт углов (6 градусов на секунду/минуту)
        minute_angle = -((minutes + seconds / 60) * 6)
        second_angle = -(seconds * 6)

        return minute_angle, second_angle, now

    # рисует фон
    def draw_background(self, screen):
        screen.fill(BACKGROUND_COLOR)

        if self.clock_face:
            face_rect = self.clock_face.get_rect(center=CLOCK_FACE_CENTER)
            screen.blit(self.clock_face, face_rect)
        else:
            # если нет изображения — рисуем круг
            pygame.draw.circle(screen, (230, 230, 230), CLOCK_FACE_CENTER, FALLBACK_CLOCK_RADIUS)
            pygame.draw.circle(screen, TEXT_COLOR, CLOCK_FACE_CENTER, FALLBACK_CLOCK_RADIUS, 4)

    # рисует Микки
    def draw_mickey(self, screen):
        if self.mickey:
            mickey_rect = self.mickey.get_rect(center=MICKEY_CENTER)
            screen.blit(self.mickey, mickey_rect)
        else:
            # fallback — рисуем голову кругами
            pygame.draw.circle(screen, (30, 30, 30), MICKEY_CENTER, FALLBACK_MICKEY_HEAD_RADIUS)
            pygame.draw.circle(screen, (30, 30, 30), (MICKEY_CENTER[0] - 65, MICKEY_CENTER[1] - 70), 35)
            pygame.draw.circle(screen, (30, 30, 30), (MICKEY_CENTER[0] + 65, MICKEY_CENTER[1] - 70), 35)

    # рисует стрелки (руки)
    def draw_hand(self, screen, image, angle, center, pivot, length, width, color):
        if image:
            # если есть картинка — вращаем её
            rotated_image, rotated_rect = rotate_around_pivot(image, angle, center, pivot)
            screen.blit(rotated_image, rotated_rect)
            return

        # иначе рисуем линию
        direction = pygame.math.Vector2(0, -1).rotate(-angle)
        end_x = int(center[0] + length * direction.x)
        end_y = int(center[1] + length * direction.y)
        pygame.draw.line(screen, color, center, (end_x, end_y), width)

    # рисует текст времени
    def draw_time_text(self, screen, now):
        font = pygame.font.SysFont("Arial", 28, bold=True)
        time_text = font.render(f"{now.minute:02d}:{now.second:02d}", True, TEXT_COLOR)
        time_rect = time_text.get_rect(center=TIME_TEXT_POSITION)
        screen.blit(time_text, time_rect)

    # подсказка если нет картинок
    def draw_missing_images_hint(self, screen):
        if all([self.clock_face, self.mickey, self.left_hand, self.right_hand]):
            return

        font = pygame.font.SysFont("Arial", 20)
        hint = font.render("Add PNG images to Practice10/mickeys_clock/images", True, ACCENT_COLOR)
        hint_rect = hint.get_rect(center=(WIDTH // 2, 40))
        screen.blit(hint, hint_rect)

    # главный метод рисования
    def draw(self, screen):
        minute_angle, second_angle, now = self.get_angles()

        self.draw_background(screen)  # фон
        self.draw_mickey(screen)      # микки

        # минутная стрелка
        self.draw_hand(
            screen,
            self.right_hand,
            minute_angle,
            RIGHT_HAND_CENTER,
            RIGHT_HAND_PIVOT,
            FALLBACK_RIGHT_HAND_LENGTH,
            10,
            (40, 40, 40),
        )

        # секундная стрелка
        self.draw_hand(
            screen,
            self.left_hand,
            second_angle,
            LEFT_HAND_CENTER,
            LEFT_HAND_PIVOT,
            FALLBACK_LEFT_HAND_LENGTH,
            6,
            ACCENT_COLOR,
        )

        pygame.draw.circle(screen, TEXT_COLOR, CENTER_DOT_POSITION, 8)  # центр
        self.draw_time_text(screen, now)  # время
        self.draw_missing_images_hint(screen)  # подсказка
