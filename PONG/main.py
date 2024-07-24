import pygame
import random

pygame.init()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 100)

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
BOARD_COLOR = [255,255,255]
PLAYER_COLOR = [128,128,128]
BALL_COLOR = [255,255,0]
BALL_RADIUS = 10
TIME_DELAY = 10 #milliseconds
PLAYER_SPEED = 5

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

PLAYER_1 = pygame.Rect(SCREEN_WIDTH/2-350,int(SCREEN_HEIGHT*0.4),5,int(0.2*SCREEN_HEIGHT))
PLAYER_2 = pygame.Rect(SCREEN_WIDTH/2+350,int(SCREEN_HEIGHT*0.4),5,int(0.2*SCREEN_HEIGHT))
BALL_OBJECT = pygame.Rect(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,BALL_RADIUS,BALL_RADIUS)
UPPER_BOUNDARY = pygame.Rect(0,0,SCREEN_WIDTH,2)
LOWER_BOUNDARY = pygame.Rect(0,SCREEN_HEIGHT,SCREEN_WIDTH,2)
LEFT_BOUNDARY  = pygame.Rect(-20,0,22,SCREEN_HEIGHT)
RIGHT_BOUNDARY  = pygame.Rect(SCREEN_WIDTH,0,22,SCREEN_HEIGHT)
velocities = [_ for _ in [[x,y] for x in range(-4,5) for y in range(-4,5)] if _ not in ([[0,i] for i in range(-4,5)]+[[j,0] for j in range(-4,5)])]

class Game():

    def __init__(self):
        self.ball_velocity = random.choice(velocities)
        self.player1_score = 0
        self.player2_score = 0
        # self.ball_pos = [SCREEN_WIDTH/2,SCREEN_HEIGHT/2]

    def draw_on_screen(self):
        pygame.draw.rect(screen,BOARD_COLOR,pygame.Rect(SCREEN_WIDTH/2-2,0,5,SCREEN_HEIGHT))
        pygame.draw.rect(screen,BOARD_COLOR,PLAYER_1)
        pygame.draw.rect(screen,BOARD_COLOR,PLAYER_2)
        pygame.draw.rect(screen,BOARD_COLOR,UPPER_BOUNDARY)
        pygame.draw.rect(screen,BOARD_COLOR,LOWER_BOUNDARY)

    def check_bounce(self):
        if(BALL_OBJECT.colliderect(UPPER_BOUNDARY) or BALL_OBJECT.colliderect(LOWER_BOUNDARY)):
            self.ball_velocity[1] = -1*self.ball_velocity[1]
        
        elif(BALL_OBJECT.collidelist([PLAYER_1,PLAYER_2])!=-1):
            self.ball_velocity[0] = -1*(self.ball_velocity[0])*(abs(self.ball_velocity[0])+1)/(abs(self.ball_velocity[0]))
    
            

    

game = Game()

run = True

while(run):

    screen.fill((0,0,0))

    game.draw_on_screen()
    # game.ball_pos[0]+=game.ball_velocity[0]
    # game.ball_pos[1]+=game.ball_velocity[1]
    
    game.check_bounce()
    BALL_OBJECT.x = BALL_OBJECT.x + (game.ball_velocity[0])
    BALL_OBJECT.y = BALL_OBJECT.y + (game.ball_velocity[1])

    if(BALL_OBJECT.x>SCREEN_WIDTH):
        game.player1_score+=1
        BALL_OBJECT.x,BALL_OBJECT.y = SCREEN_WIDTH/2,SCREEN_HEIGHT/2
        game.ball_velocity = random.choice(velocities)

    elif(BALL_OBJECT.x<0):
        game.player2_score+=1
        BALL_OBJECT.x,BALL_OBJECT.y = SCREEN_WIDTH/2,SCREEN_HEIGHT/2
        game.ball_velocity = random.choice(velocities)

    Player1_surface = my_font.render(str(game.player1_score), False, (128,128,128))
    Player2_surface = my_font.render(str(game.player2_score), False, (128,128,128))

    screen.blit(Player1_surface, (SCREEN_WIDTH*1/4-25,SCREEN_HEIGHT/2-60))
    screen.blit(Player2_surface, (SCREEN_WIDTH*3/4-25,SCREEN_HEIGHT/2-60))


    pygame.draw.circle(screen,BALL_COLOR,center=(BALL_OBJECT.x,BALL_OBJECT.y),radius=BALL_RADIUS)
    pygame.time.delay(TIME_DELAY)
    
    key = pygame.key.get_pressed()
    if(key[pygame.K_w] == True):
        if(not PLAYER_1.colliderect(UPPER_BOUNDARY)):
            PLAYER_1.move_ip(0,-1*PLAYER_SPEED)
    elif(key[pygame.K_s] == True):
        if(not PLAYER_1.colliderect(LOWER_BOUNDARY)):
            PLAYER_1.move_ip(0,1*PLAYER_SPEED)

    if(key[pygame.K_UP] == True):
        if(not PLAYER_2.colliderect(UPPER_BOUNDARY)):
            PLAYER_2.move_ip(0,-1*PLAYER_SPEED)
    elif(key[pygame.K_DOWN] == True):
        if(not PLAYER_2.colliderect(LOWER_BOUNDARY)):
            PLAYER_2.move_ip(0,1*PLAYER_SPEED)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()