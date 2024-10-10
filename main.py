import pygame
import time
import random

pygame.init()

width = 600
height = 400
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('My humble snake game')

white = (255, 255, 255)
black = (0, 0, 0)
red = (250, 128, 144)
green = (60, 179, 113)

snake_block = 10
snake_speed = 16

font_style = pygame.font.SysFont('impact', 28)

def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    display.blit(value, [0, 0])

def draw_the_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])


def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_block) / 10) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10) * 10

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            
            display.fill(black)
            message = font_style.render("Game Over! Press Q(quit) or C(Play Again)", True, red)
            message_width = message.get_width()
            display.blit(message, [(width - message_width) / 2, height / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        display.fill(black)

        pygame.draw.rect(display, white, [food_x, food_y, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_the_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        # Snake eating food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
