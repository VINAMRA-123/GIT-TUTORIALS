# THIS IS THE FRAME OF CREATING PYGAME
# import pygame

# x= pygame.init()
# print(x)    # this is only used for testing that the pygame is working or not
#now creating window 
# gameWindow = pygame.display.set_mode((1000,500))          #double bracket should be there
# pygame.display.set_caption("flappy bird")
#creating specific value
# game_over = False
# exit_game = False
#creating a game loop 
# while not game_over:
#     for event in pygame.event.get():
#          if event.type == pygame.QUIT:
#              exit_game = True
    
#     if event.type == pygame.KEYDOWN:
#         if event.type == KEY_RIGHT:
#             print("you have pressed right key" )

# pygame.quit()
# quit()


# SNAKE GAME

import random
import pygame
pygame.init()

screen_hieght = 1000
screen_width = 500
gameWindow = pygame.display.set_mode((screen_hieght,screen_width))

pygame.display.set_caption("snake game with king kobra")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])



clock = pygame.time.Clock()

def gameloop():
    color = (255,255,255)
    black = (255,0,0)
    red = (0,0,255)
    snake_x = 45
    snake_y = 55
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    init_val = 5
    score = 0
    snk_list = []
    snk_length = 1
    food_y = random.randint(0,screen_hieght/1.25)
    food_x = random.randint(0,screen_width/1.25)
    game_over = False
    exit_game = False
    fps = 30
    
    while not exit_game:
        if game_over:
            gameWindow.fill(color)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameloop()    
                    
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_val
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_val
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_val
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_val
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs( snake_x - food_x)<6 and abs(snake_y - food_y)<6 :
                score +=1
                food_y = random.randint(20,screen_hieght/2)
                food_x = random.randint(20,screen_width/2)
                snk_length +=5

                gameWindow.fill(black)
                text_screen("Score: " + str(score), red, 5, 5)
                pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
            
                if len(snk_list)>snk_length:
                    del snk_list[0]
                    
                if snake_x<0 or snake_x> screen_hieght or snake_y<0 or snake_y>screen_hieght:
                    game_over = True
                    
                if head in snk_list[:-1]:
                    game_over = True

                if len(snk_list)>snk_length:
                    del snk_list[0]

            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snake(gameWindow, color, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
gameloop()

# # source code
# import pygame
# import random

# pygame.init()

# # Colors
# white = (255, 255, 255)
# red = (255, 0, 0)
# black = (0, 0, 0)

# # Creating window
# screen_width = 900
# screen_height = 600
# gameWindow = pygame.display.set_mode((screen_width, screen_height))

# # Game Title
# pygame.display.set_caption("SnakesWithHarry")
# pygame.display.update()
# clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 55)

# def text_screen(text, color, x, y):
#     screen_text = font.render(text, True, color)
#     gameWindow.blit(screen_text, [x,y])


# def plot_snake(gameWindow, color, snk_list, snake_size):
#     for x,y in snk_list:
#         pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

# # Game Loop
# def gameloop():
#     # Game specific variables
#     exit_game = False
#     game_over = False
#     snake_x = 45
#     snake_y = 55
#     velocity_x = 0
#     velocity_y = 0
#     snk_list = []
#     snk_length = 1

#     food_x = random.randint(20, screen_width / 2)
#     food_y = random.randint(20, screen_height / 2)
#     score = 0
#     init_velocity = 5
#     snake_size = 30
#     fps = 60
#     while not exit_game:
#         if game_over:
#             gameWindow.fill(white)
#             text_screen("Game Over! Press Enter To Continue", red, 100, 250)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit_game = True

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RETURN:
#                         gameloop()

#         else:

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     exit_game = True

#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_RIGHT:
#                         velocity_x = init_velocity
#                         velocity_y = 0

#                     if event.key == pygame.K_LEFT:
#                         velocity_x = - init_velocity
#                         velocity_y = 0

#                     if event.key == pygame.K_UP:
#                         velocity_y = - init_velocity
#                         velocity_x = 0

#                     if event.key == pygame.K_DOWN:
#                         velocity_y = init_velocity
#                         velocity_x = 0

#             snake_x = snake_x + velocity_x
#             snake_y = snake_y + velocity_y

#             if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
#                 score +=1
#                 food_x = random.randint(15, screen_width / 1.25)
#                 food_y = random.randint(15, screen_height / 1.25)
#                 snk_length +=5

#             gameWindow.fill(white)
#             text_screen("Score: " + str(score ), red, 5, 5)
#             pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


#             head = []
#             head.append(snake_x)
#             head.append(snake_y)
#             snk_list.append(head)

#             if len(snk_list)>snk_length:
#                 del snk_list[0]

#             if head in snk_list[:-1]:
#                 game_over = True

#             if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
#                 game_over = True
#             plot_snake(gameWindow, black, snk_list, snake_size)
#         pygame.display.update()
#         clock.tick(fps)

#     pygame.quit()
#     quit()
# gameloop()




