import pygame
import functionphysics

import var
import const
import asset

class UI():
    title_text = [8, 8]

    start_button = [160, 160, 960, 80]
    start_text = [168, 180]
    arena_button = [160, 240, 960, 80]
    arena_text = [168, 260]
    collection_button = [160, 320, 960, 80]
    collection_text = [168, 340]

    version_text = [8, 660]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)
    var.screen.blit(asset.Font.title.render('Bouncy Defense', True, const.Color.black), UI.title_text)
    
    pygame.draw.rect(var.screen, const.Color.black, UI.start_button, 2)
    var.screen.blit(asset.Font.title.render('Start Game', True, const.Color.black), UI.start_text)
    pygame.draw.rect(var.screen, const.Color.black, UI.arena_button, 2)
    var.screen.blit(asset.Font.title.render('Arena', True, const.Color.black), UI.arena_text)
    pygame.draw.rect(var.screen, const.Color.black, UI.collection_button, 2)
    var.screen.blit(asset.Font.title.render('Collection', True, const.Color.black), UI.collection_text)

    var.screen.blit(asset.Font.title.render('V0.0.1', True, const.Color.black), UI.version_text)
    pygame.display.flip()

def mouse_up():
    mouse = pygame.mouse.get_pos()

    if var.menu == False:
        if var.state == '':
            if functionphysics.point_inside_rect_list(mouse[0], mouse[1], UI.start_button):
                var.scene = 'save_select'

            elif functionphysics.point_inside_rect_list(mouse[0], mouse[1], UI.collection_button):
                var.scene = 'collection'