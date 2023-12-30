import pygame
import random
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

size = [400, 400]
cell_size = 20
column_count = size[0] // cell_size
row_count = size[1] // cell_size

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

KEY_DIRECTION = {
    pygame.K_UP: 'N',
    pygame.K_DOWN: 'S',
    pygame.K_LEFT: 'W',
    pygame.K_RIGHT: 'E',
}


class Snake:
    def __init__(self):
        self.positions = [(0, 2), (0, 1), (0, 0)]
        self.direction = ''

    def draw(self):
        for position in self.positions:
            self.draw_block(screen, GREEN, position)

    def move(self):
        head_position = self.positions[0]
        y, x = head_position
        if self.direction == 'N':
            self.positions = [(y - 1, x)] + self.positions[:-1]
        elif self.direction == 'S':
            self.positions = [(y + 1, x)] + self.positions[:-1]
        elif self.direction == 'W':
            self.positions = [(y, x - 1)] + self.positions[:-1]
        elif self.direction == 'E':
            self.positions = [(y, x + 1)] + self.positions[:-1]

    def grow(self):
        tail_position = self.positions[-1]
        y, x = tail_position
        if self.direction == 'N':
            self.positions.append((y - 1, x))
        elif self.direction == 'S':
            self.positions.append((y + 1, x))
        elif self.direction == 'W':
            self.positions.append((y, x - 1))
        elif self.direction == 'E':
            self.positions.append((y, x + 1))

    def check_collision(self):
        head_position = self.positions[0]
        y, x = head_position
        if y < 0 or y >= row_count or x < 0 or x >= column_count:
            return True
        return False

    @staticmethod
    def draw_block(screen, color, position):
        block = pygame.Rect((position[1] * 20, position[0] * 20), (20, 20))
        pygame.draw.rect(screen, color, block)


class Apple:
    def __init__(self, position=(5, 5)):
        self.position = position

    def draw(self):
        Snake.draw_block(screen, RED, self.position)


def show_game_over_message():
    root = tk.Tk()
    root.withdraw()  # 창을 표시하지 않도록 설정
    messagebox.showinfo("확인", "게임 오버입니다.")

    # 확인 버튼을 누르면 게임 재시작
    restart_game()


def restart_game():
    global last_moved_time
    last_moved_time = datetime.now()

    # 초기화 코드 추가 (새로운 뱀, 사과 생성 등)
    global snake, apple
    snake = Snake()
    apple = Apple()
    runGame()


def runGame():
    global last_moved_time
    last_moved_time = datetime.now()

    global snake, apple
    snake = Snake()
    apple = Apple()

    global done
    done = False

    while not done:
        clock.tick(10)
        screen.fill(WHITE)

        for column_index in range(column_count):
            for row_index in range(row_count):
                rect = (cell_size * column_index, cell_size * row_index, cell_size, cell_size)
                pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key in KEY_DIRECTION:
                    snake.direction = KEY_DIRECTION[event.key]

        if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
            snake.move()
            last_moved_time = datetime.now()

        if snake.check_collision():
            done = True
            show_game_over_message()

        if snake.positions[0] == apple.position:
            snake.grow()
            apple.position = (random.randint(0, 19), random.randint(0, 19))

        if snake.positions[0] in snake.positions[1:]:
            done = True
            show_game_over_message()

        snake.draw()
        apple.draw()
        pygame.display.update()

    pygame.quit()


runGame()
