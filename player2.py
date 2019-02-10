#import pygam
import pygame

#declares the color white and black
white = (255,255,255)
black = (0,0,0)

#class for the player 2
class Player2(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        
        #call the parent class constructor (Sprite)
        super().__init__()

        #put in the color for the player, the x and y position, and the width and height
        self.image = pygame.Surface([width, height])
        
        #set the background color to somethign other than the player color, and make it transparent
        self.image.fill(white)
        self.image.set_colorkey(black)
        
        #draw the player
        pygame.draw.rect(self.image, color, [0,0, width, height])

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


        
