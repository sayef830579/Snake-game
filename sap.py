
import pygame
import random
import sys

pygame.init()

WIDTH = 600
HEIGHT = 400
SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game 🐍")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)

BLACK = (20, 20, 20)
GREEN = (0, 255, 100)
RED = (255, 50, 50)
WHITE = (255, 255, 255)

snake = [(100, 100), (80, 100), (60, 100)]
direction = (SIZE, 0)

food = (
    random.randrange(0, WIDTH, SIZE),
    random.randrange(0, HEIGHT, SIZE)
)

score = 0
game_over = False

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, SIZE):
                direction = (0, -SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -SIZE):
                direction = (0, SIZE)
            elif event.key == pygame.K_LEFT and direction != (SIZE, 0):
                direction = (-SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-SIZE, 0):
                direction = (SIZE, 0)

            if game_over and event.key == pygame.K_SPACE:
                snake = [(100, 100), (80, 100), (60, 100)]
                direction = (SIZE, 0)
                score = 0
                game_over = False

    if not game_over:
        head = (
            snake[0][0] + direction[0],
            snake[0][1] + direction[1]
        )

        snake.insert(0, head)

        if head == food:
            score += 10
            while True:
                food = (
                    random.randrange(0, WIDTH, SIZE),
                    random.randrange(0, HEIGHT, SIZE)
                )
                if food not in snake:
                    break
        else:
            snake.pop()

        if (head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT or
            head in snake[1:]):
            game_over = True

    screen.fill(BLACK)

    for part in snake:
        pygame.draw.rect(
            screen, GREEN,
            (part[0], part[1], SIZE - 2, SIZE - 2)
        )

    pygame.draw.rect(
        screen, RED,
        (food[0], food[1], SIZE - 2, SIZE - 2)
    )

    score_text = font.render(
        f"Score: {score}", True, WHITE
    )
    screen.blit(score_text, (10, 10))

    if game_over:
        text = font.render("GAME OVER!", True, RED)
        restart = font.render(
            "Press SPACE to Restart", True, WHITE
        )

        screen.blit(text, (200, 150))
        screen.blit(restart, (145, 200))

    pygame.display.update()
    clock.tick(10)

pygame.quit()
sys.exit()
