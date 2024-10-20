import pygame
import numpy
from entity import Entity2D
from physics.transform import Transform2D

class Square(Entity2D):
    def __init__(self, size, transform : Transform2D = None, color = "white"):
        '''
        Paramaters:
            size: the side length of the square 
            origin: the origin in 2D of the square
        '''
        self.size = size
        if transform is None:
            self.transform = Transform2D()
        else: self.transform = transform

        self.color = color

    def draw(self, camera):
        originScreen = camera.ToScreen(self.transform.position)
        pygame.draw.rect(camera.screen, self.color, pygame.rect.Rect(originScreen[0],originScreen[1],self.size,self.size))