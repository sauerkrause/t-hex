import pygame
import hex_grid
import random

class Grid(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._hex_grid = hex_grid.HexGrid(rows, columns, 50, 50)
        self.objects = {}
        self.selection = []
        for i in range(0, rows):
            for j in range(0, columns):
                self.objects[(i,j)] = random.random()

    def mouse_over(self, pos):
        self._hex_grid.highlight(pos)
        coords = [coord for coord in self._hex_grid.highlighted]
        self.selection = [self.object_at(coord) for coord in coords]
    
    def object_at(self, coord):
        if coord in self.objects:
            return self.objects[coord]
        else:
            return None

    def draw(self, surface):
        self._hex_grid.draw(surface, pygame.Color("white"))

    
