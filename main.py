import time
import pygame
import sys

from dice import Dice

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600 # Высота и ширина
BACKGROUND_COLOR = (255, 255, 255) # Цвет фона устанавливаем белый

# Настройки окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")

# Создание кубика
dice = Dice()

# Загрузка изображений
dice_images = [pygame.image.load(f'./images/dice_{i}.png') for i in range(1, 13)]

# Загрузка звука
roll_sound = pygame.mixer.Sound('./sounds/roll_sound (mp3cut.net).wav')


def draw_dice(image):
    # Рисуем кубик в центре окна
    screen.fill(BACKGROUND_COLOR)
    image_rect = image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(image, image_rect)
    pygame.display.flip()


def main():
    clock = pygame.time.Clock()

    index = 0 # Индекс картинки
    result = None
    run = True # Работа с флагом

    while run:

        # Создание смены картинок до пробела
        screen.fill(BACKGROUND_COLOR) # Цвет фона устанавливаем в переменную
        screen.blit(dice_images[index], (WIDTH // 2 - 324 // 2, HEIGHT // 2 - 340 // 2)) # Высота и ширина делится на 2 и отнимается высота и ширина картинки, что бы определить центр
        index += 1 # Увеличиваем индекс для смены цикла

        # Если индекс больше или равен 11, то индекс становится 0
        if index > 11:
            index = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                value = dice.roll()[0]  # Ролл при нажатии пробела
                draw_dice(dice_images[value - 1])  # Отображаем текущее значение
                roll_sound.play()  # Играем звуковой эффект
                result = value # Результат по значению 1-12
                run = False # Становится False, что бы цикл прервался
                screen.blit(dice_images[value - 1], (WIDTH // 2 - 324 // 2, HEIGHT // 2 - 340 // 2))
                time.sleep(5) # Таймер на 5 сек

        pygame.display.update() # Обновление экрана, для смены картинок

        clock.tick(10)  # Ограничение до 10 кадров в секунду

    return result # Возвращаем результат по значению 1-12

if __name__ == "__main__":
    res = main()
    print(res)