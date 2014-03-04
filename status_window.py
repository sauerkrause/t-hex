import pygame

class StatusWindow(object):
    def __init__(self):
        self.font_height = 24
        self.font = pygame.font.Font(None, self.font_height)

    def draw(self, surface, coords, selection):
        if len(selection) > 0:
            i = 0
            coord_surf = self.font.render(str(coords[0]), True, pygame.color.Color("white"))
            surface.blit(coord_surf, (530, i*self.font_height))
            i = 1
            selected = selection[0]
            terrain = self.font.render(str(selected.terrain), True, pygame.color.Color("white"))
            surface.blit(terrain, (530, i*self.font_height))
            i = 2
            contents = [self.font.render(str(s), True, pygame.color.Color("white")) for s in selected.contents]
            for content in contents:
                surface.blit(content, (530, i*self.font_height))
                i = i + 1
