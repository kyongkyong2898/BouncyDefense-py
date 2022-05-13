import pygame
import functionphysics

import var
import const
import asset

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    pygame.display.flip()