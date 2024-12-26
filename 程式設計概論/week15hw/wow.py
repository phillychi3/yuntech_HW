import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("hw15")


class Snake:
    def __init__(self, x, y, color):
        self.positions = [(x, y)]
        self.direction = [1, 0]
        self.color = color
        self.score = 0
        self.grow_flag = False

    def move(self):
        current = self.positions[0]
        x = current[0] + self.direction[0]
        y = current[1] + self.direction[1]

        if x >= GRID_WIDTH:
            x = 0
        elif x < 0:
            x = GRID_WIDTH - 1
        if y >= GRID_HEIGHT:
            y = 0
        elif y < 0:
            y = GRID_HEIGHT - 1

        self.positions.insert(0, (x, y))
        if not self.grow_flag:
            self.positions.pop()
        self.grow_flag = False

    def grow(self):
        self.score += 1
        self.grow_flag = True

    def check_collision(self, other_snake):
        head = self.positions[0]
        if head in self.positions[1:]:
            return True
        if head in other_snake.positions:
            return True
        return False


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        x = random.randint(0, GRID_WIDTH - 1)
        y = random.randint(0, GRID_HEIGHT - 1)
        self.position = (x, y)


def main():
    clock = pygame.time.Clock()

    snake1 = Snake(5, GRID_HEIGHT // 2, GREEN)
    snake2 = Snake(GRID_WIDTH - 6, GRID_HEIGHT // 2, BLUE)

    food = Food()

    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and snake1.direction != [0, 1]:
                    snake1.direction = [0, -1]
                elif event.key == pygame.K_s and snake1.direction != [0, -1]:
                    snake1.direction = [0, 1]
                elif event.key == pygame.K_a and snake1.direction != [1, 0]:
                    snake1.direction = [-1, 0]
                elif event.key == pygame.K_d and snake1.direction != [-1, 0]:
                    snake1.direction = [1, 0]

                elif event.key == pygame.K_UP and snake2.direction != [0, 1]:
                    snake2.direction = [0, -1]
                elif event.key == pygame.K_DOWN and snake2.direction != [0, -1]:
                    snake2.direction = [0, 1]
                elif event.key == pygame.K_LEFT and snake2.direction != [1, 0]:
                    snake2.direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and snake2.direction != [-1, 0]:
                    snake2.direction = [1, 0]

        snake1.move()
        snake2.move()

        if snake1.positions[0] == food.position:
            snake1.grow()
            food.spawn()
        if snake2.positions[0] == food.position:
            snake2.grow()
            food.spawn()

        if snake1.check_collision(snake2) or snake2.check_collision(snake1):
            running = False

        screen.fill(BLACK)

        pygame.draw.rect(
            screen,
            RED,
            (
                food.position[0] * GRID_SIZE,
                food.position[1] * GRID_SIZE,
                GRID_SIZE - 1,
                GRID_SIZE - 1,
            ),
        )

        for pos in snake1.positions:
            pygame.draw.rect(
                screen,
                snake1.color,
                (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1),
            )

        for pos in snake2.positions:
            pygame.draw.rect(
                screen,
                snake2.color,
                (pos[0] * GRID_SIZE, pos[1] * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1),
            )

        score_text = font.render(
            f"green: {snake1.score}  blue: {snake2.score}", True, WHITE
        )
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
