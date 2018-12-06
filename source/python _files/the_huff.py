import pygame

class Huff():

    def __init__(self, screen):
        """Initialize the image and set its starting position."""
        self.screen = screen
        #load the image and get it's rect.
        self.image = pygame.image.load('source\images\jhuffff.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        # Start each new image at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at it's current location."""
        self.screen.blit(self.image, self.rect)
