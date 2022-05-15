import pygame
import functionphysics

import var
import const
import asset

class UI():
    title_text = [8, 8]
    back_button = [1160, 40, 80, 80]
    save_data_button = [[160, 160, 960, 160], [160, 320, 960, 160], [160, 480, 960, 160]]
    save_text_1 = [[168, 220], [168, 380], [168, 540]]
    save_text_2 = [[168, 300], [168, 460], [168, 620]]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    var.screen.blit(asset.Font.title.render('Select save file', True, const.Color.black), UI.title_text)
    pygame.draw.rect(var.screen, const.Color.black, UI.back_button, 2)

    for i in range(3):
        pygame.draw.rect(var.screen, const.Color.black, UI.save_data_button[i], 2)
        var.screen.blit(asset.Font.title.render('File ' + str(i + 1), True, const.Color.black), UI.save_text_1[i])

    pygame.display.flip()

def mouse_up():
    mouse = pygame.mouse.get_pos()

    if var.menu == False:
        if var.state == '':
            if functionphysics.point_inside_rect_list(mouse[0], mouse[1], UI.back_button):
                var.scene = 'title'

            for i in range(3):
                if functionphysics.point_inside_rect_list(mouse[0], mouse[1], UI.save_data_button[i]):
                    var.scene = 'level_select'
