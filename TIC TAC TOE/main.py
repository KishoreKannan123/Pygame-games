import pygame
import random
import numpy as np

import time

pygame.init()

#Some unnecessary comment

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = [random.randint(0,256) for _ in range(3)]
GRID_COLOR = [255 - i for i in BACKGROUND_COLOR]
GRID_HEIGHT = 500
GRID_WIDTH = 5
GRID_CENTER_X = 400
GRID_CENTER_Y = 300
CHECK_WIN_COLOR = [128 for i in BACKGROUND_COLOR]

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# X always starts first

GRID_LEFT = pygame.Rect((GRID_CENTER_X-GRID_HEIGHT/6,GRID_CENTER_Y-GRID_HEIGHT/2,GRID_WIDTH,GRID_HEIGHT))
GRID_RIGHT = pygame.Rect((GRID_CENTER_X+GRID_HEIGHT/6,GRID_CENTER_Y-GRID_HEIGHT/2,GRID_WIDTH,GRID_HEIGHT))
GRID_UP = pygame.Rect((GRID_CENTER_X-GRID_HEIGHT/2,GRID_CENTER_Y-GRID_HEIGHT/6,GRID_HEIGHT,GRID_WIDTH))
GRID_DOWN = pygame.Rect((GRID_CENTER_X-GRID_HEIGHT/2,GRID_CENTER_Y+GRID_HEIGHT/6,GRID_HEIGHT,GRID_WIDTH))
CENTER = pygame.Rect((GRID_CENTER_X,GRID_CENTER_Y,10,10))

run = True

class GameLogic():

    def __init__(self,player = -1):
        self.player = player   #-1 for O and +1 for X
        self.matrix = np.zeros((3,3))
        self.positions = [(_,i) for _ in range(3) for i in range(3)]
        self.winner = 0
        self.turn = 'AI' if self.player == 1 else 'HUMAN'
        self.run = True

    def ai_turn(self):
        choice = random.choice(self.positions)
        game.matrix[choice] = self.player
        self.positions.remove(choice)
        self.turn = 'HUMAN'

    def human_turn(self):
        choices = np.array(self.positions)
        choices = (choices - np.ones_like(choices))*GRID_HEIGHT/6 + np.repeat(np.array([[GRID_CENTER_X,GRID_CENTER_Y]]),len(choices),axis = 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = pygame.mouse.get_pos()
                choice_taken = np.argmin(np.linalg.norm(choices-np.repeat(np.array([[x,y]]),len(choices),axis = 0),axis = 1))
                self.matrix[self.positions[choice_taken]] = -1*self.player
                self.positions.remove(self.positions[choice_taken])
                self.turn = 'AI'

    def check_win(self):
        if(3 in np.sum(self.matrix,axis = 0)):
            self.winner = 1
            return True
        elif(-3 in np.sum(self.matrix,axis = 0)):
            self.winner = -1
            return True
        elif(3 in np.sum(self.matrix,axis = 1)):
            self.winner = 1
            return True
        elif(-3 in np.sum(self.matrix,axis = 1)):
            self.winner = -1
            return True
        elif(np.trace(self.matrix) == 3):
            self.winner = 1
            return True
        elif(np.trace(self.matrix) == -3):
            self.winner = -1
            return True
        elif(np.trace(np.fliplr(self.matrix)) == 3):
            self.winner = 1
            return True
        elif(np.trace(np.fliplr(self.matrix)) == -3):
            self.winner = -1
            return True
        else:
            self.winner = 0
            return False
        
    def draw_on_screen(self):

        pygame.draw.rect(screen,GRID_COLOR,GRID_LEFT)
        pygame.draw.rect(screen,GRID_COLOR,GRID_DOWN)
        pygame.draw.rect(screen,GRID_COLOR,GRID_RIGHT)
        pygame.draw.rect(screen,GRID_COLOR,GRID_UP)

        if(self.winner == 1):
            Xcolor = CHECK_WIN_COLOR
            Ocolor = GRID_COLOR
        elif(self.winner == -1):
            Ocolor = CHECK_WIN_COLOR
            Xcolor = GRID_COLOR
        else:
            Ocolor = Xcolor = GRID_COLOR
        drawO(SCREEN_WIDTH-50,GRID_CENTER_Y+self.player*100,color = Ocolor)
        drawX(SCREEN_WIDTH-50,GRID_CENTER_Y-self.player*100,color = Xcolor)

        for _ in range(len(self.matrix)):
            for i in range(len(self.matrix[_])):
                if(self.matrix[_][i] == 1):
                    drawX((_- 1)*GRID_HEIGHT/3 + GRID_CENTER_X,(i- 1)*GRID_HEIGHT/3 + GRID_CENTER_Y)
                elif(self.matrix[_][i] == -1):
                    drawO((_- 1)*GRID_HEIGHT/3 + GRID_CENTER_X,(i- 1)*GRID_HEIGHT/3 + GRID_CENTER_Y)


game = GameLogic(player = 1)

def drawX(x,y,color = GRID_COLOR):
  pygame.draw.lines(screen, color, closed = True, points = [(int(x-GRID_HEIGHT/12),int(y-GRID_HEIGHT/12)),(int(x+GRID_HEIGHT/12),int(y+GRID_HEIGHT/12))],width = 5)
  pygame.draw.lines(screen, color, closed = True, points = [(int(x-GRID_HEIGHT/12),int(y+GRID_HEIGHT/12)),(int(x+GRID_HEIGHT/12),int(y-GRID_HEIGHT/12))],width = 5)

def drawO(x,y,color = GRID_COLOR):
  pygame.draw.circle(screen, color,center = (int(x),int(y)),radius = GRID_HEIGHT/12,width=5)

while(run):
    
    run = game.run
    screen.fill(BACKGROUND_COLOR)
    
    game.draw_on_screen()
    game_status = game.check_win()
    
    if(len(game.positions)!=0 and not game_status):

        if(game.turn == 'AI'):
            game.ai_turn()
        
        elif(game.turn == 'HUMAN'):
            game.human_turn()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
