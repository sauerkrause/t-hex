import pygame
import hex_grid
import random
import game_location

class Grid(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self._hex_grid = hex_grid.HexGrid(rows, columns, 50, 50)
        self.locations = {}
        self.selected_coords = ()
        self.selection = []
        for i in range(0, rows):
            for j in range(0, columns):
                r = random.random()
                self.locations[(i,j)] = game_location.GameLocation((i,j))
                if r < 0.75:
                    self.locations[(i,j)].terrain = "Desert"
                elif r < 0.95:
                    self.locations[(i,j)].terrain = "Grassland"
                    self.locations[(i,j)].add_content("farms")
                    self.locations[(i,j)].add_content("peasants")
                else:
                    self.locations[(i,j)].terrain = "Mountains"
                    self.locations[(i,j)].add_content("coal")

    def mouse_over(self, pos):
        self._hex_grid.highlight(pos)
        coords = [coord for coord in self._hex_grid.highlighted]
        self.selected_coords = coords
        self.selection = [self.object_at(coord) for coord in coords]
    
    def object_at(self, coord):
        if coord in self.locations:
            return self.locations[coord]
        else:
            return None

    def draw(self, surface):
        self._hex_grid.draw(surface, pygame.Color("white"))

    
