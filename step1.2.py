import pygame  #attaches pygame module to program
pygame.init()  #initializes pygame
pygame.display.set_caption("Platformer")  # sets the window title
screen = pygame.display.set_mode((500,500))  # creates game screen
screen.fill((0,0,50)) #sets background color of game screen
pygame.display.flip()#draws everything to the screen
