#import pygame
import pygame

#declare the color black and white
black = (0, 0, 0)
white = (255,255,255)

#class for the player 1
class Player1(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        #call the parent class constructor (Sprite)
        super().__init__()

        #put in the color for the player, the x and y position, and the width and height
        self.image = pygame.Surface([width, height])
        
        #set the background color to something other than the players color, and make it transparent
        self.image.fill(white)
        self.image.set_colorkey(black)
        
        #draw the player
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #get the rectangle object
        self.rect = self.image.get_rect()

    #make the player move up
    def moveUp(self, pixels):
        self.rect.y -= pixels

    #make the player move down
    def moveDown(self, pixels):
        self.rect.y += pixels

    #make the player move left
    def moveLeft(self, pixels):
        self.rect.x -=pixels

    #make the player move right
    def moveRight(self, pixels):
        self.rect.x +=pixels


