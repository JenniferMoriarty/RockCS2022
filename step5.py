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
isOnGround = False #this variable stops gravity from pulling you down when you're on something solid

#OMG GAME LOOP###################################################
while gameOver == False:
    
    #Input section-----------------------------------------
    clock.tick(60) #FPS (frames per second, aka game speed)
    for event in pygame.event.get(): #event queue
        if event.type == pygame.QUIT: #quit game if x is pressed in top corner
            gameOver = True
      
        if event.type == pygame.KEYDOWN: #key has been pressed down
            if event.key == pygame.K_LEFT: #check if left arrow has been pressed
                keys[0] = True #if so, change list slot value
            if event.key == pygame.K_RIGHT:
                keys[1] = True
            if event.key == pygame.K_UP:
                keys[2] = True

        elif event.type == pygame.KEYUP: #key has been released
            if event.key == pygame.K_LEFT: #check if left arrow has been released
                keys[0] = False #if so, change list slot value
            if event.key == pygame.K_RIGHT:
                keys[1] = False
            if event.key == pygame.K_UP:
                keys[2] = False  
                

    
    #physics update section--------------------------------
    
    #LEFT/RIGHT MOVEMENT
    if keys[0] == True: #check if left has been stored as true in list
        vx = -3 #set velocity
    elif keys[1] == True: #check if right has been stored as true in list
        vx = 3 #set velocity 
    else:
        vx = 0 #otherwise stop!
    
    #UP MOVEMENT
    if keys[2] == True and isOnGround == True: #check if up has been stored as true in list
        vy = -8
        
    #else:
        #vy = 0 
    

    isOnGround = False
    
    #stop falling if on bottom of game screen
    if ypos > 500-20: #adjust "500" to fit the height of your screen
        isOnGround = True
        vy = 0 #stop movement
        ypos = 500-20 #reset feet to bottom of game screen
    
    #gravity
    if isOnGround == False:
        vy += .2 #notice this grows over time, aka ACCELERATION
    
    #update player position by adding velocity to position
    xpos += vx 
    ypos += vy
    
    #render section----------------------------------------
    screen.fill((0,0,50)) #wipe screen so it doesn't smear
    
    pygame.draw.rect(screen, (200,0,0), (xpos, ypos, 20, 20)) #draw player
    
    pygame.display.flip()#draws everything to the screen
    
#END OF GAME LOOP################################################
pygame.quit()

