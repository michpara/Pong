#importing modules
import pygame, random, math, sys, os
from player1 import Player1
from player2 import Player2
from ball import Ball
from arena import Arena
from pygame.locals import *

#function for the main game, contains the Start window, Game window and End window
def game():

    #initializes pygame
    pygame.init()

    #initializes pygame.mixer
    pygame.mixer.init()

    
    #defines the colors that will be used in this game
    black = (0,0,0)
    white = (255, 255, 255)

    #sets the height and width for the screen and displays the screen
    size = [512, 256]
    screen = pygame.display.set_mode(size)
    
    #title for our window
    pygame.display.set_caption("Pong")

    #adds sprites into a group
    all_sprites_list = pygame.sprite.Group()

    #defines the color, height, width and position of the player1
    player1 = Player1(white, 5, 28)
    player1.rect.x = 512
    player1.rect.y = 117

    #defines the color, height, width and position of the player2
    player2 = Player2(white, 5, 28)
    player2.rect.x = 0
    player2.rect.y = 117

    #defines the color, height, width and position for the arena
    arena = Arena(white, 1, 256)
    arena.rect.x = 256
    arena.rect.y = 0

    #defines the color, height, width and position of the ball
    ball = Ball(white, 5, 5)
    ball.rect.x = 256
    ball.rect.y = 128

    #keeps track of the balls direction
    ballDirX = -1
    ballDirY = -1

    #checks which directory pygame is looking at when finding sound effects
    os.getcwd()

    #creates a sound effect when the ball hits the wall
    walleffect = pygame.mixer.Sound('wall.wav')

    #creates a sound effect when the ball hits a player
    playereffect = pygame.mixer.Sound('player.wav')

    #creates a sound effect when a player scores
    scoreffect = pygame.mixer.Sound('score.wav')

    #adds player1, player2, ball and arena into sprites
    all_sprites_list.add(player1)
    all_sprites_list.add(player2)
    all_sprites_list.add(ball)
    all_sprites_list.add(arena)

    #initializes the clock (this will be used for the FPS of the game)
    clock = pygame.time.Clock()

    #defines player 1 initial score
    player1score = 0

    #defines player 2 initial score
    player2score = 0

    #checks if the ball collides with the wall
    def checkEdgeCollision(ball, ballDirX, ballDirY):
        
        #if the ball is outside of the top and bottom screen borders
        if ball.rect.top == 0 or ball.rect.bottom == 256:
            
            #change the balls direction (y axis)
            ballDirY = ballDirY *-1
            
            #play the wall sound effect
            walleffect.play()
        
        return ballDirX, ballDirY

    #checks if the ball collides with either of the players
    def checkPlayerCollision(ball, player1, player2, ballDirx):

        #if the ball collides with player 2
        if ballDirX == -1 and ball.rect.left == player2.rect.right and player2.rect.top < ball.rect.top and player1.rect.bottom > ball.rect.bottom:
            
            #play the player sound effect
            playereffect.play()
            
            #change the direction of the ball (x axis)
            return -1
        
        #if the ball collides with player 1
        elif ballDirX == 1 and ball.rect.right == player1.rect.left and player1.rect.top < ball.rect.top and player1.rect.bottom > ball.rect.bottom:
            
            #play the player sound effect
            playereffect.play()
            
            #change the direction of the ball (x axis)
            return -1
        
        #if the ball doesn't collide with either of the players, do nothing.
        else:
            return 1

    #a function that makes the ball move
    def moveBall(ball,ballDirX, ballDirY):

            #changes the position of the balls x axis according to ballDirX
            ball.rect.x += ballDirX

            # hanges the position of the balls y axis according to ballDirY
            ball.rect.y += ballDirY

            #returns ball
            return ball

    #checks if player1 has scored
    def checkScore(ball, player1score):
        if ball.rect.x < 0:

            #player 1 score increases by 1
            player1score+=1

            #plays the score sound effect
            scoreffect.play()

            #resets the ball
            reset()

            #returns player 1 score
            return player1score

        else:
            return player1score

    #checks if player2 has scored
    def checkScore2(ball, player2score):
        if ball.rect.x > 512:

            #player 2 score increases bt 1
            player2score+=1

            #plays the score sound effect
            scoreffect.play()

            #resets the ball
            reset()

            #returns player 2 score
            return player2score
        else:
            return player2score

    #resets the ball
    def reset():
        ball.rect.x = 256
        ball.rect.y = 128
        ballDirX = -1
        ballDirY = -1

    #defines running as False, end as False and start as True (these are all while loops)
    end = False
    running = False
    start = True

    #while loop for start screen
    while start:

        #fills the screen as black
        screen.fill(black)

        #gets the font pong.ttf
        myfont = pygame.font.Font("pong.ttf", 50)
        myfont2 = pygame.font.Font("pong.ttf", 30)

        #creates the "Pong" text in white
        label = myfont.render("Pong", 1, (255,255,255))

        #creates the "Press Enter to Play" text in grey with a white background
        label2 = myfont2.render("Press Enter to Play", 1, (49,79,79),(255,255,255))

        #displays label and label 2 on the screen
        screen.blit(label, (200,100))
        screen.blit(label2, (110,150))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                #if the player presses Enter
                if event.key == pygame.K_RETURN:

                    #play the score effect
                    scoreffect.play()

                    #end the start while loop
                    start = False

                    #start the game while loop
                    running = True

                #if the play presses 'x'
                if event.key == pygame.K_x:

                    #end the start while loop
                    start = False

                    #quit pygame
                    pygame.quit()

                    #exit the system
                    sys.exit()

            #if the player clicks the x button
            if event.type == pygame.QUIT:

                #end the start while loop
                start = False

                #quit pygame
                pygame.quit()

                #exist system
                sys.exit()
        
    #while loop for main game

    running = True
    end = False
    while running:
       
        for event in pygame.event.get():
            
            #if the player closes the window the game quits
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            #if the player clicks the "x" button the game quits
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    running = False
                    pygame.quit()
                    sys.exit()

        #updates the display
        pygame.display.update()

        #defines keys as the pygame functions key.get_pressed()
        keys = pygame.key.get_pressed()
        
        #controls for player 1
        if keys[pygame.K_UP]:
            player1.moveUp(4)
        if keys[pygame.K_DOWN]:
            player1.moveDown(4)
       
        #creates border for player 1
        if player1.rect.right > 512:
            player1.rect.right = 512
        if player1.rect.left < 256:
            player1.rect.left = 256
        if player1.rect.bottom > 256:
            player1.rect.bottom = 256
        if player1.rect.top < 0:
            player1.rect.top = 0

        #controls for player 2
        if keys[ord('w')]:
            player2.moveUp(4)
        if keys[ord('s')]:
            player2.moveDown(4)

        #creates border for player 2
        if player2.rect.right > 256:
            player2.rect.right = 256
        if player2.rect.left < 0:
            player2.rect.left = 0
        if player2.rect.bottom > 256:
            player2.rect.bottom = 256
        if player2.rect.top < 0:
            player2.rect.top = 0
        
        pygame.display.flip()
        
        #updates all sprites
        all_sprites_list.update()

        #colors the screen as black
        screen.fill(black)

        #draws all the sprites onto the screen
        all_sprites_list.draw(screen)

        #60 frames per second
        clock.tick(60)

        #calls the move method, makes the ball move
        ball = moveBall(ball, ballDirX, ballDirY)

        #checks for a collision between the ball and the wall and changes the direction accordingly
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)

        #checks for a collision between the ball and the player and changes the direction accordingly
        ballDirX = ballDirX*checkPlayerCollision(ball, player1,player2, ballDirX)

        #checks if player1 scored and adds the point to player1score if they did
        player1score = checkScore(ball, player1score)

        #checks if player 2 scored and adds the point to player2score if they did
        player2score = checkScore2(ball, player2score)

        #gets the font pong.ttf
        myfont = pygame.font.Font("pong.ttf", 75)
        myfont2 = pygame.font.Font("pong.ttf", 75)

        #gets the text for the score for player 1 and player 2
        label = myfont.render(str(player2score), 1, (255,255,255))
        label2 = myfont2.render(str(player1score), 1,(255,255,255))

        #displays the text on screen
        screen.blit(label, (110,20))
        screen.blit(label2, (370,20))
        
        pygame.display.flip()

        winner = ''
        #if player 1 reaches 10 points
        if player1score == 10:
            
            #starts the game over while loop
            end = True
            winner = 'Player 1 Wins!'

        #if player 2 reaches 10 points
        if player2score == 10:

            #starts the game over while loop
            end = True
            winner= 'Player 2 Wins!'

        #game over while loop
        while end :

            #makes the screen black
            screen.fill(black)

            #gets the font pong.ttf
            myfont = pygame.font.Font("pong.ttf", 50)
            myfont2 = pygame.font.Font("pong.ttf", 20)
            

            #creates the text for the game over screen
            label = myfont.render("GAME OVER", 1, (255,255,255))
            label2 = myfont2.render("Press Enter to Play Play Again", 1,(255,255,255))
            label3 = myfont2.render(winner, 1, (255,255,255))
            
            #displays the text and the screen
            screen.blit(label, (135,100))
            screen.blit(label2, (105,150))
            screen.blit(label3, (180, 200))
            pygame.display.flip()
            
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    
                    #if the play presses return
                    if event.key == pygame.K_RETURN:
                        
                        #restart the game
                        game()

                    #if the user presses x
                    if event.key == pygame.K_x:
                        pygame.quit()
                        
                        #quit the game
                        sys.exit()
            
                #if the user clicks the exit button in the window
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    #quit the game
                    sys.exit()

#restart the game
game()
     
        




