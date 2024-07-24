import pygame

pygame.init()

#There are 3 elements :
#Window
#Game loop
#Event handler

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #creates a window


player = pygame.Rect((300,250,50,50))    #first 2 are coordinates,next 2 are the height and width

#Game loop
run = True
while(run):

    screen.fill((0,0,0))   #to clear the traces made by the player

    pygame.draw.rect(screen,(255,255,0),player)   #the second argument is color , in this case it is red
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1,0)    #move in place (subtract coordinates from position)
    if key[pygame.K_d] == True:
        player.move_ip(1,0)
    if key[pygame.K_w] == True:
        player.move_ip(0,-1)
    if key[pygame.K_s] == True:
        player.move_ip(0,1)

    for event in pygame.event.get():  #Iterating through all the events that pygame picks up
        if event.type == pygame.QUIT:   #Checks for the clicking the close button on the top right corner of the window (The x button)
            run = False

    pygame.display.update()
pygame.quit()