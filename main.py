import pygame
import random

pygame.init()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Параметры экрана
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")

# Параметры игры
CELL_SIZE = 20
CELL_COUNT_X = WIDTH // CELL_SIZE
CELL_COUNT_Y = HEIGHT // CELL_SIZE

class Snake:
    def __init__(self):
        self.body = [(5, 5), (4, 5), (3, 5)]
        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        new_head = ((head_x + new_dir_x) % CELL_COUNT_X, (head_y + new_dir_y) % CELL_COUNT_Y)
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        head_x, head_y = self.body[0]
        new_dir_x, new_dir_y = self.direction
        new_head = ((head_x + new_dir_x) % CELL_COUNT_X, (head_y + new_dir_y) % CELL_COUNT_Y)
        self.body = [new_head] + self.body

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

snake = Snake()

food = (random.randint(0, CELL_COUNT_X - 1), random.randint(0, CELL_COUNT_Y - 1))

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != (1, 0):
                snake.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                snake.direction = (1, 0)
            elif event.key == pygame.K_UP and snake.direction != (0, 1):
                snake.direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                snake.direction = (0, 1)

    snake.move()

    if snake.body[0] == food:
        snake.grow()
        food = (random.randint(0, CELL_COUNT_X - 1), random.randint(0, CELL_COUNT_Y - 1))

    if snake.body[0] in snake.body[1:]:
        running = False

    snake.draw(screen)
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
