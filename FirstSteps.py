import pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)
def main(winstyle=0):
    pygame.init()
    winstyle=0
    bestdepth = pygame.display.mode_ok(SCREENRECT.size,winstyle,32)
    screen = pygame.display.set_mode(SCREENRECT.size,winstyle,bestdepth)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
        keystate = pygame.key.get_pressed()
main()
pygame.quit()
quit()