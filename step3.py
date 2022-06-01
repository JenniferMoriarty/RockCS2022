import pygame  #attaches pygame module to program
pygame.init()  #initializes pygame
pygame.display.set_caption("Platformer")  # sets the window title
screen = pygame.display.set_mode((500,500))  # creates game screen
screen.fill((0,0,50)) #sets background color of game screen

#game variables
gameOver = False #Boolean variable to run game loop
clock = pygame.time.Clock() #set up clock

#player variables
xpos = 100 #xposition of player
ypos = 100 #yposition of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed, slots are 0-3

#OMG GAME LOOP###################################################
while gameOver == False:
    
    #Input section-----------------------------------------
    clock.tick(60) #FPS (frames per second, aka game speed)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #quit game if x is pressed in top corner
            gameOver = True
      
        if event.type == pygame.KEYDOWN: #key has been pressed down
            if event.key == pygame.K_LEFT: #check if left arrow has been pressed
                keys[0] = True #if so, change list slot value

        elif event.type == pygame.KEYUP: #key has been released
            if event.key == pygame.K_LEFT: #check if left arrow has been released
                keys[0] = False #if so, change list slot value

    
    #physics update section--------------------------------
    
    
    #render section----------------------------------------
    
    pygame.draw.rect(screen, (200,0,0), (100,100,20,20)) #draw player
    
    
    pygame.display.flip()#draws everything to the screen
    
#END OF GAME LOOP################################################
pygame.quit()
