import pygame  #attaches pygame module to program
pygame.init()  #initializes pygame
pygame.display.set_caption("my game")  # sets the window title
screen = pygame.display.set_mode((200,200))  # creates game screen
screen.fill((0,250,0)) #sets background color of game screen
pygame.display.flip()#draws everything to the screen
