import sys  # нужен для завершения программы (sys.exit)

import pygame  # библиотека для создания игр (окно, графика, события)

from clock import FPS, HEIGHT, WIDTH, MickeyClock  # настройки и класс часов


def main(): 
    pygame.init()  # запуск pygame

    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # создание окна
    pygame.display.set_caption("Mickey's Clock")  # название окна

    clock = pygame.time.Clock()  # контроль FPS
    mickey_clock = MickeyClock()  # создаём объект часов

    running = True
    while running:  # главный цикл программы
        for event in pygame.event.get():  # обработка событий
            if event.type == pygame.QUIT:  # если закрыли окно
                running = False  # выходим из цикла

        mickey_clock.draw(screen)  # рисуем часы
        pygame.display.flip()  # обновляем экран
        clock.tick(FPS)  # ограничиваем FPS

    pygame.quit()  # закрываем pygame
    sys.exit()  # полностью завершаем программу


if __name__ == "__main__":  # если файл запущен напрямую
    main()  # запускаем программу
