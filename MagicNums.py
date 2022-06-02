import pygame  #attaches pygame module to program
pygame.init()  #initializes pygame

#CONSTANTS
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 500
DARK_BLUE = (0,0,50)
PINK = (200, 0, 100)
PURPLE = (100, 0, 200)
RED = (200, 0, 0)

pygame.display.set_caption("Platformer")  
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH)) 
screen.fill(DARK_BLUE) 

#game variables
gameOver = False #Boolean variable to run game loop
clock = pygame.time.Clock() #set up clock

#player variables
xpos = 100 #xposition of player
ypos = 100 #yposition of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed, slots are 0-3
isOnGround = False #this variable stops gravity from pulling you down when you're on something solid
player_width = 20
player_height = 20
xvel = 3
yvel = 8
gravity = .2

#OMG GAME LOOP###################################################
while gameOver == False:
    
    #Input section-----------------------------------------
    clock.tick(60) #FPS (frames per second, aka game speed)
    for event in pygame.event.get(): #event queue
        if event.type == pygame.QUIT: #quit game if x is pressed in top corner
            gameOver = True
      
        if event.type == pygame.KEYDOWN: #key has been pressed down
            if event.key == pygame.K_LEFT: #check if left arrow has been pressed
                keys[LEFT] = True #if so, change list slot value
            if event.key == pygame.K_RIGHT:
                keys[RIGHT] = True
            if event.key == pygame.K_UP:
                keys[UP] = True

        elif event.type == pygame.KEYUP: #key has been released
            if event.key == pygame.K_LEFT: #check if left arrow has been released
                keys[LEFT] = False #if so, change list slot value
            if event.key == pygame.K_RIGHT:
                keys[RIGHT] = False
            if event.key == pygame.K_UP:
                keys[UP] = False  
                

    
    #physics update section--------------------------------
    
    #LEFT/RIGHT MOVEMENT
    if keys[LEFT] == True: #check if left has been stored as true in list
        vx = -1*xvel #set velocity
    elif keys[RIGHT] == True: #check if right has been stored as true in list
        vx = xvel #set velocity 
    else:
        vx = 0 #otherwise stop!
    
    #UP MOVEMENT
    if keys[UP] == True and isOnGround == True: #check if up has been stored as true in list
        vy = -1*yvel
        
    #else:
        #vy = 0 
    
    isOnGround = False
    
        
    #PLATFORM COLLISION
    if xpos + player_width > 100 and xpos < 200 and ypos + player_height > 350 and ypos + player_height < 370:
        ypos = 350 - player_height
        isOnGround = True
        vy = 0
    elif xpos + player_width > 200 and xpos < 300 and ypos + player_height > 450 and ypos + player_height < 470:
        ypos = 450 - player_height
        isOnGround = True
        vy = 0
    else:
        isOnGround = False
    
    #stop falling if on bottom of game screen
    if ypos > SCREEN_HEIGHT - player_height: #adjust "500" to fit the height of your screen
        isOnGround = True
        vy = 0 #stop movement
        ypos = SCREEN_HEIGHT - player_height #reset feet to bottom of game screen
    
    #gravity
    if isOnGround == False:
        vy += gravity #notice this grows over time, aka ACCELERATION
    
    #update player position by adding velocity to position
    xpos += vx 
    ypos += vy
    
    #render section----------------------------------------
    screen.fill(DARK_BLUE) #wipe screen so it doesn't smear
    
    #first platform
    pygame.draw.rect(screen, PINK, (100, 350, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, PURPLE, (200, 450, 100, 20))
    
    pygame.draw.rect(screen, RED, (xpos, ypos, player_width, player_height)) #draw player
    
    pygame.display.flip()#draws everything to the screen
    
#END OF GAME LOOP################################################
pygame.quit()

