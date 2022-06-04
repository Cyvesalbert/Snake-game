import pygame
import random


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
        # self.displayScoreObject = displayScore()
        # self.levelObject = level()

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
                        # self.levelObject.runLevel()
                        pass
                    if width / 2.3 <= mouse[0] <= width / 2.3 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                        # self.displayScoreObject.afficherScore()
                        pass

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

            pygame.display.update() # updates the frames of the game


class playScreen:
    snakeSpeed = 15 #class variable to store speed for the game

    def __init__(self):
        self.snakePosition = [100, 50] # defining snake default position
        self.snakeBody = [[100, 50], [90, 50], [80, 50], [70, 50]] # defining first 4 blocks of snake body
        self.fruitPosition = [random.randrange(1, (width // 10)) * 10, random.randrange(1, (height // 10)) * 10] # fruit position
        self.fruitSpawn = True
        self.direction = 'RIGHT' # setting default snake direction towards right
        self.changeTo = self.direction # variable to store the current direction
        self.score = 0 # initial score

    # method to run the game
    def main(self):
        while True:
            screen.blit(bg1, (0, 0))
            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.changeTo = 'UP'
                    if event.key == pygame.K_DOWN:
                        self.changeTo = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        self.changeTo = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        self.changeTo = 'RIGHT'

                #if mouse is clicked on back button the main menu appear
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width / 1.12 <= mouse1[0] <= width / 1.12 + 140 and height / 150 <= mouse1[1] <= height / 150 + 40:
                        backToMenu = menu()
                        backToMenu.runMenu()

            mouse1 = pygame.mouse.get_pos() # store le coordinates as a tuple

            # if mouse is hovered on back button it changes to lighter shade
            if width / 1.12 <= mouse1[0] <= width / 1.12 + 140 and height / 150 <= mouse1[1] <= height / 150 + 40:
                pygame.draw.rect(screen, colorLight, [width / 1.12, height / 150, 120, 30])


            # If two keys pressed simultaneously we don't want snake to move into two directions simultaneously
            if self.changeTo == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.changeTo == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.changeTo == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.changeTo == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'

            # Moving the snake
            if self.direction == 'UP':
                self.snakePosition[1] -= 10
            if self.direction == 'DOWN':
                self.snakePosition[1] += 10
            if self.direction == 'LEFT':
                self.snakePosition[0] -= 10
            if self.direction == 'RIGHT':
                self.snakePosition[0] += 10

            # Snake body growing mechanism if fruits and snakes collide then scores will be incremented by 10
            self.snakeBody.insert(0, list(self.snakePosition))
            if self.snakePosition[0] == self.fruitPosition[0] and self.snakePosition[1] == self.fruitPosition[1]:
                self.score += 10
                self.fruitSpawn = False
            else:
                self.snakeBody.pop()

            if not self.fruitSpawn:
                self.fruitPosition = [random.randrange(1, (width// 10)) * 10, random.randrange(1, (height // 10)) * 10]

            self.fruitSpawn = True
            #screen.fill(black)

            for pos in self.snakeBody:
                pygame.draw.rect(screen, blue, pygame.Rect(pos[0], pos[1], 10, 10))

            pygame.draw.rect(screen, white, pygame.Rect(self.fruitPosition[0], self.fruitPosition[1], 10, 10))

            # Game Over conditions
            if self.snakePosition[0] < 0 or self.snakePosition[0] > width - 10:
                self.game_over()
                pass
            if self.snakePosition[1] < 0 or self.snakePosition[1] > height - 10:
                self.game_over()

            # Touching the snake body
            for block in self.snakeBody[1:]:
                if self.snakePosition[0] == block[0] and self.snakePosition[1] == block[1]:
                    self.game_over()

            self.show_score() # displaying score countinuously
            screen.blit(back, (width / 1.12, height / 150))

            pygame.display.update() # Refresh game screen

            fps.tick(playScreen.snakeSpeed) # Frame Per Second /Refresh Rate

    # displaying Score function
    def show_score(self):
        scoreSurface = textFont.render('Score : ' + str(self.score), True, white) # create the display surface object score_surface
        scoreRect = scoreSurface.get_rect() # create a rectangular object for the text surface object
        screen.blit(scoreSurface, scoreRect) # displaying text

    # game over function
    def game_over(self):
        with open("scores.txt", 'a') as sco:
            sco.write(" " + str(self.score))

        #creating a text surface on which text will be drawn
        gameOverSurface = textFont.render('Game Over! Your Score is : ' + str(self.score), True, red)
        inputFile = open('scores.txt', 'r')
        bestScoreSurface = textFont.render("The Best Score is : " + str(max([int(num) for num in inputFile.read().split()])), True, red)

        gameOverRect = gameOverSurface.get_rect() # create a rectangular object for the text surface object
        bestScoreRectangle = bestScoreSurface.get_rect() # create a rectangular object for the text surface object

        gameOverRect.midtop = (width / 2, height / 4) # setting position of the text
        bestScoreRectangle.midtop = (width / 2, height / 3) # setting position of the text

        while True:
            screen.blit(bg, (0, 0))
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()

                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if width / 2.1 <= mouse[0] <= width / 2.1 + 140 and height / 1.8 <= mouse[1] <= height / 1.8 + 40:
                        self.replay = playScreen()
                        self.replay.main()
                    if width / 2.3 <= mouse[0] <= width / 2.3 + 140 and height / 1.5 <= mouse[1] <= height / 1.5 + 40:
                        pygame.quit()

            # screen.fill((60, 25, 60)) # fills the screen with a color
            mouse = pygame.mouse.get_pos() # store le coordinates as a tuple

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
            screen.blit(bestScoreSurface, bestScoreRectangle)
            screen.blit(gameOverSurface, gameOverRect)
            screen.blit(replay, (width / 2.2, height / 1.8))
            screen.blit(quit, (width / 2.1, height / 1.5))

            pygame.display.update() # updates the frames of the game
