import pygame
import functionphysics

import var
import const
import asset

class UI():
    title_text = [8, 8]

    class Ready():
        rect = [160, 160, 960, 400]
        start_button = [560, 440, 160, 80]
        start_text = [600, 460]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    if var.state == 'ready':
        pygame.draw.rect(var.screen, const.Color.black, UI.Ready.rect, 2)
        pygame.draw.rect(var.screen, const.Color.black, UI.Ready.start_button, 2)

    pygame.display.flip()

def mouse_up():
    pass