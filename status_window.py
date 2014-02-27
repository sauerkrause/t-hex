import pygame

class StatusWindow(object):
    def __init__(self):
        self.font_height = 24
        self.font = pygame.font.Font(None, self.font_height)

    def draw(self, surface, coords, selection):
        if len(selection) > 0:
            i = 1
            coord_surf = self.font.render(str(coords[0]), True, pygame.color.Color("white"))
            surface.blit(coord_surf, (530, 0))
            selected = selection[0]
            stati = [self.font.render(str(s), True, pygame.color.Color("white")) for s in selected]
            for status in stati:
                surface.blit(status, (530, i*self.font_height))
                i = i + 1
