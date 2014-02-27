import pygame
from pygame.locals import *

import grid
import status_window

class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._grid = None
        self._status_window = None
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((840,480), pygame.HWSURFACE)
        self._grid = grid.Grid(10, 10)
        self._status_window = status_window.StatusWindow()
        self._running = True
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        elif event.type == MOUSEMOTION:
            self._grid.mouse_over(event.pos)
            
    def on_loop(self):
        pass

    def on_render(self):
        self._display_surf.fill(pygame.Color("black"))
        self._grid.draw(self._display_surf)
        self._status_window.draw(self._display_surf, self._grid.selected_coords, self._grid.selection)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
