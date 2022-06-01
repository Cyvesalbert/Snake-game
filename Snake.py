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


class menu():
    def __init__(self):
        self.playScreenObject = playScreen()
        self.displayScoreObject = displayScore()
        self.levelObject = level()

    def runMenu(self):
        while True:
            screen.blit(bg, (0, 0))
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if width / 2.4 <= mouse[0] <= width / 2.4 + 140 and height / 2.3 <= mouse[1] <= height / 2.3 + 40:
                        self.playScreenObject.main()
                    if width / 2.1 <= mouse[0] <= width / 2.1 + 140 and height / 1.8 <= mouse[1] <= height / 1.8 + 40:
                        self.levelObject.runLevel()
                    if width / 2.3 <= mouse[0] <= width / 2.3 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                        self.displayScoreObject.afficherScore()

            # screen.fill(black) # fills the screen with a color
            mouse = pygame.mouse.get_pos() # store le coordinates as a tuple

            # if mouse is hovered on Start button it changes to lighter shade
            if width / 2.4 <= mouse[0] <= width / 2.4 + 140 and height / 2.3 <= mouse[1] <= height / 2.3 + 40:
                pygame.draw.rect(screen, colorLight, [width / 2.4, height / 2.3, 140, 40])
            else:
                pygame.draw.rect(screen, colorDark, [width / 2.4, height / 2.3, 140, 40])

            # if mouse is hovered on Level button it changes to lighter shade
            if width / 2.1 <= mouse[0] <= width / 2.1 + 140 and height / 1.8 <= mouse[1] <= height / 1.8 + 40:
                pygame.draw.rect(screen, colorLight, [width / 2.4, height / 1.8, 140, 40])
            else:
                pygame.draw.rect(screen, colorDark, [width / 2.4, height / 1.8, 140, 40])

            # if mouse is hovered on BestScore button it changes to lighter shade
            if width / 2.3 <= mouse[0] <= width / 2.3 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                pygame.draw.rect(screen, colorLight, [width / 2.4, height / 1.5, 140, 40])
            else:
                pygame.draw.rect(screen, colorDark, [width / 2.4, height / 1.5, 140, 40])

            # superimposing the text onto our button
            screen.blit(titre1, (width / 7, height / 4))
            screen.blit(play, (width / 2.1, height / 2.3))
            screen.blit(gameLevel, (width / 2.1, height / 1.8))
            screen.blit(bestScore, (width / 2.4, height / 1.5))
            
            # updates the frames of the game
            pygame.display.update()

