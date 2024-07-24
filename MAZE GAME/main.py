import pygame
import random

pygame.init()



SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

run = True

PLAYER = pygame.Rect(10,SCREEN_HEIGHT-10,10,10)
GOAL = pygame.Rect(SCREEN_WIDTH-10,0,10,10)

PLAYER_COLOR = [255,255,0]
GOAL_COLOR = [0,255,0]
OBSTACLES_COLOR = [255,0,0]
NO_OF_OBSTACLES = 10
STEP_SIZE = 1
DELAY_TIME = 10 #milliseconds

ALL_OBSTACLE_LOCATIONS = [(x,y) for x in range(0,SCREEN_WIDTH) for y in range(0,SCREEN_HEIGHT)]
OBSTACLES_LOCATIONS_TO_BE_REMOVED = [(x,y) for x in range(0,40) for y in range(SCREEN_HEIGHT-40,SCREEN_HEIGHT)]+[(x,y) for x in range(SCREEN_WIDTH-40,SCREEN_WIDTH) for y in range(0,40)]
POSSIBLE_OBSTACLE_LOCATIONS = [_ for _ in ALL_OBSTACLE_LOCATIONS if _ not in OBSTACLES_LOCATIONS_TO_BE_REMOVED]
 
OBSTACLES = [pygame.Rect(0,0,SCREEN_WIDTH,1),pygame.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,1),pygame.Rect(0,0,1,SCREEN_HEIGHT),pygame.Rect(SCREEN_WIDTH,0,1,SCREEN_HEIGHT)]

for _ in range(NO_OF_OBSTACLES):
    x,y = random.choice(POSSIBLE_OBSTACLE_LOCATIONS)
    OBSTACLES.append(pygame.Rect(x,y,random.randint(10,40),random.randint(10,40)))


def obstacles():

    pygame.draw.rect(screen,OBSTACLES_COLOR,OBSTACLES[0])
    for _ in OBSTACLES[1:]:
        pygame.draw.rect(screen,OBSTACLES_COLOR,_)

def check_collision(last_move):
    for _ in OBSTACLES:
        if(PLAYER.colliderect(_)):
            PLAYER.move_ip(-1*last_move[0],-1*last_move[1])


while(run):
    

    screen.fill((0,0,0))
    
    obstacles()
    pygame.draw.rect(screen,GOAL_COLOR,GOAL)
    pygame.draw.rect(screen,PLAYER_COLOR,PLAYER)
    
    


    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:

        PLAYER.move_ip(-1*STEP_SIZE,0)
        check_collision([-1*STEP_SIZE,0])
        pygame.time.delay(DELAY_TIME)


    if key[pygame.K_d] == True:
        
        PLAYER.move_ip(1*STEP_SIZE,0)
        check_collision([1*STEP_SIZE,0])
        pygame.time.delay(DELAY_TIME)

    if key[pygame.K_s] == True:
        
        PLAYER.move_ip(0,1*STEP_SIZE)
        check_collision([0,1*STEP_SIZE])
        pygame.time.delay(DELAY_TIME)

    if key[pygame.K_w] == True:
        
        PLAYER.move_ip(0,-1*STEP_SIZE)
        check_collision([0,-1*STEP_SIZE])
        pygame.time.delay(DELAY_TIME)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    

    pygame.display.update()

pygame.quit()