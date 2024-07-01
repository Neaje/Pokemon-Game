import pygame
import random
import os
import sys

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jeu d'évitement")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

BACKGROUND_IMG = resource_path('assets/images/background.png')
GAME_OVER_IMG = resource_path('assets/images/game_over.png')
PLAYER_IMGS = [resource_path(f'assets/images/player{i}.png') for i in range(1, 4)]
OBSTACLE_IMGS = [resource_path(f'assets/images/obstacle{i}.png') for i in range(1, 3)]

def load_and_scale_image(path, size):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, size)

background = pygame.image.load(BACKGROUND_IMG)
game_over_img = pygame.image.load(GAME_OVER_IMG)
player_imgs = [load_and_scale_image(img, (90, 90)) for img in PLAYER_IMGS]
obstacle_imgs = [load_and_scale_image(img, (50, 50)) for img in OBSTACLE_IMGS]


player_img = random.choice(player_imgs)
player_width = player_img.get_width()
player_height = player_img.get_height()

player_speed = 5

initial_obstacle_interval = 1500  # ms

score = 0
max_score = 0  
difficulty_increase_interval = 2000  # ms
max_speed = 15
min_obstacle_interval = 200

font = pygame.font.Font(None, 36)

def game_over():
    global score, max_score
    over = True
    if score > max_score:
        max_score = score  

    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    over = False
                    game_loop()

        screen.fill(WHITE)
        game_over_x = (screen_width - game_over_img.get_width()) // 2
        game_over_y = (screen_height - game_over_img.get_height()) // 2
        screen.blit(game_over_img, (game_over_x, game_over_y))
        pygame.display.flip()

def game_loop():
    global score, initial_obstacle_interval, player_img, player_width, player_height
    player_img = random.choice(player_imgs)  
    player_img = pygame.transform.scale(player_img, (90, 90))  
    player_width = player_img.get_width()
    player_height = player_img.get_height()
    player_x = screen_width // 2
    player_y = screen_height - player_height - 10
    obstacles = []
    last_obstacle_time = pygame.time.get_ticks()
    last_difficulty_increase_time = pygame.time.get_ticks()
    player_speed_current = player_speed
    obstacle_interval = initial_obstacle_interval
    score = 0
    start_time = pygame.time.get_ticks()
    running = True
    difficulty_capped = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed_current
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed_current

        current_time = pygame.time.get_ticks()
        if current_time - last_obstacle_time > obstacle_interval:
            obstacle_x = random.randint(0, screen_width - 50)
            obstacle_y = -50
            obstacle_img = random.choice(obstacle_imgs)
            obstacles.append([obstacle_x, obstacle_y, obstacle_img])
            last_obstacle_time = current_time

        for obstacle in obstacles:
            obstacle[1] += player_speed_current
            if obstacle[1] > screen_height:
                obstacles.remove(obstacle)

        for obstacle in obstacles:
            if (player_x < obstacle[0] < player_x + player_width or player_x < obstacle[0] + 25 < player_x + player_width) and \
               (player_y < obstacle[1] < player_y + player_height or player_y < obstacle[1] + 25 < player_y + player_height):
                running = False
                game_over()

        if current_time - last_difficulty_increase_time > difficulty_increase_interval:
            if player_speed_current < max_speed:
                player_speed_current += 1
            if obstacle_interval > min_obstacle_interval:
                obstacle_interval -= 100
            else:
                difficulty_capped = True
            last_difficulty_increase_time = current_time

        score = (current_time - start_time) // 1000

        screen.blit(background, (0, 0))
        screen.blit(player_img, (player_x, player_y))
        for obstacle in obstacles:
            screen.blit(obstacle[2], (obstacle[0], obstacle[1]))

        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if max_score > 0:
            max_score_text = font.render(f"Max Score: {max_score}", True, BLACK)
            screen.blit(max_score_text, (10, 50))

        pygame.display.flip()
        pygame.time.delay(30)

    pygame.quit()

game_loop()
