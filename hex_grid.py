import pygame
import math

class HexGrid:
        def __init__(self, rows, columns, hex_width, hex_height):
            self.hex_height = hex_height
            self.hex_width = hex_width
            self.rows = rows
            self.columns = columns
            self.potential_highlights = []
            self.highlighted = []
            
        def highlight(self, pos):
            self.highlighted = self.point_at(pos)
            
        def _potentially_close_point(self, pos, i, j):
            center = self._center_point(i, j)
            within_w = (math.fabs(center[0] - pos[0]) < self.hex_width * 0.5)
            within_h = (math.fabs(center[1] - pos[1]) < self.hex_height * 0.5)
            return within_w and within_h

        def dist(self, pos, pos2):
            return math.fabs(pos2[0]-pos[0]) + math.fabs(pos2[1]-pos[1])

        def closest_center(self, pos, potentials):
            idx = -1
            min_dist = self.hex_width + self.hex_height
            min_dist = min_dist * 1000
            for i in range(0, len(potentials)):
                potential = potentials[i]
                this_dist = self.dist(pos, self._center_point(potential[0], potential[1]))
                if(this_dist < min_dist):
                    idx = i
                    min_dist = this_dist
            if idx == -1:
                return []
            else:
                return [potentials[idx]]
                
        def point_at(self, pos):
            self.potential_highlights = [(i, j) for i in range(0, self.rows) for j in range(0, self.columns) if self._potentially_close_point(pos, i, j)]
            centers = self.closest_center(pos, self.potential_highlights)
            return centers
        
        def _center_point(self, row, col):
            if col % 2 == 0:
                return (self.hex_width * (row + 1.0),
                        self.hex_height * (col * 0.75 + 0.5))
            else:
                return (self.hex_width * (row + 0.5),
                        self.hex_height * (col * 0.75 + 0.5))
            
        def _sum_points(self, pt1, pt2):
            return (pt1[0]+pt2[0],pt1[1]+pt2[1])
        
        def get_edge_points(self, row, col):
            offsets = [(0, self.hex_height * 0.5),
                       (self.hex_width * 0.5, self.hex_height * 0.25),
                       (self.hex_width * 0.5, self.hex_height * -0.25),
                       (0, self.hex_height * -0.5),
                       (self.hex_width * -0.5, self.hex_height * -0.25),
                       (self.hex_width * -0.5, self.hex_height * 0.25)]
            center_point = self._center_point(row, col)
            return [self._sum_points(center_point, i) for i in offsets]
            
        def draw_point(self, row, col, surface, color):
            pt = self._center_point(row, col)
            pygame.draw.polygon(surface, color, self.get_edge_points(row, col), 1)
            if (row, col) in self.potential_highlights:
                pygame.draw.polygon(surface, pygame.Color("grey"), self.get_edge_points(row, col))
            if (row, col) in self.highlighted:
                pygame.draw.polygon(surface, color, self.get_edge_points(row, col))

        def draw(self, surface, color):
            for i in range(0, self.rows):
                for j in range(0, self.columns):
                    self.draw_point(i, j, surface, color)
