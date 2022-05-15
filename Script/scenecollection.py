import pygame
import functionphysics

import var
import const
import asset

class UI():
    title_text = [8, 8]
    back_button = [1160, 40, 80, 80]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.title.render('Collection', False, const.Color.black), UI.back_button)
    pygame.draw.rect(var.screen, const.Color.black, UI.back_button, 2)

    pygame.display.flip()