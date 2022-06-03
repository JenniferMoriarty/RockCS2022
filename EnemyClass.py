import pygame  #attaches pygame module to program
import math
pygame.init()  #initializes pygame

class Enemy:#-----------------------------------------------------------------------------
    def __init__(self, xpos, ypos): #parameterized constructor
        self.xpos = xpos
        self.ypos = ypos
        self.OriginalX = xpos
        self.GoingRight = 1

    def draw(self): #call this in the render section of game loop
        pygame.draw.circle(screen, (0,250,0), (self.xpos, self.ypos), 15)
    
    #movement function: moves enemy back and forth over platform
    #call this in the physics section
    def move(self): 
        if self.GoingRight == 1:
            self.xpos += 2
        if self.GoingRight == -1:
            self.xpos -= 2
        if abs(self.OriginalX - self.xpos) > 40:
            self.GoingRight = self.GoingRight * -1
    
    #circular collision function- uses distance formula
    #call this in the physics section of game loop
    def collide(self, PlayerX, PlayerY):
        if (math.sqrt((self.xpos - (PlayerX+10))**2 + (self.ypos - (PlayerY+10))**2))<15:
            return True
        else:
            return False
        

#end class enemy---------------------------------------------------------------------------

#instantiate an enemy
e1 = Enemy(200, 200)

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

#load an image
image = pygame.image.load("space.jpg") #replace with file of your choice!

#load a font
font = pygame.font.Font("freesansbold.ttf", 50)
#create the text
LostMsg = font.render("Game Over!", False, (250, 0, 250))

WinMsg = font.render("You Win!", False, (250, 0, 250))

#SOUND
jump = pygame.mixer.Sound('jump.wav')
music = pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1) #the argument "-1" means "loop indefinitely"

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
win = True


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
        pygame.mixer.Sound.play(jump)
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
        gameOver = True
        win = False
        
    #win if you touch the top of the screen
    if ypos<0:
        gameOver = True
        win = True
        
    #gravity
    if isOnGround == False:
        vy += gravity #notice this grows over time, aka ACCELERATION
    
    #update player position by adding velocity to position
    xpos += vx 
    ypos += vy
    
    e1.move() #move enemy
    if e1.collide(xpos, ypos) == True: #check for collision b/t enemy and player
        gameOver = True #game over if you hit (you could also reduce health and only stop game when health is below 0)
        win = False
    
    #render section----------------------------------------
    screen.fill(DARK_BLUE) #wipe screen so it doesn't smear
    
    screen.blit(image, (0,0)) #draw loaded image
    
    #first platform
    pygame.draw.rect(screen, PINK, (100, 350, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, PURPLE, (200, 450, 100, 20))
    
    pygame.draw.rect(screen, RED, (xpos, ypos, player_width, player_height)) #draw player
    
    e1.draw() #draw enemy
    
    pygame.display.flip()#draws everything to the screen
    
#END OF GAME LOOP################################################
if win == False:
    screen.blit(LostMsg, (100,100)) #display lost msg
else:
    screen.blit(WinMsg, (100,100)) #display win msg

pygame.display.flip()#draws everything to the screen

pygame.time.delay(5000) #wait before closing window
pygame.quit()

