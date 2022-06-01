import pygame
#from playScreen import playScreen
import time
import random
# import pygame_menu


pygame.init() # initializing the constructor
width = 600
height = 600
pygame.display.set_caption('Snake 1.0')
screen = pygame.display.set_mode((width, height)) # opens up a window
fps = pygame.time.Clock() # FPS (frames per second) controller

bg = pygame.image.load("snakeMenu.png")
bg1 = pygame.image.load("playgroundbackground.jpg")

bg = pygame.transform.scale(bg, (width, height))
bg1 = pygame.transform.scale(bg1, (width, height))

colorLight = (170, 170, 170) # light shade of the button
colorDark = (100, 100, 100) # dark shade of the button
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

titleFont= pygame.font.SysFont('Helvetica', 50)
textFont = pygame.font.SysFont('Roboto',40)

play = textFont.render('Play', True, white)
gameLevel = textFont.render('Level', True, white)
bestScore = textFont.render('Best score', True, white)
titre1 = titleFont.render('Welcome to snake game!', True, white)
quit = textFont.render('Quit', True, white)
replay = textFont.render('Replay', True, white)
easy = textFont.render('Easy', True, white)
medium = textFont.render('Medium', True, white)
dificult = textFont.render('Dificult', True, white)
titre2 = textFont.render('Choose a level below', True, white)
back = textFont.render('back',True, white)