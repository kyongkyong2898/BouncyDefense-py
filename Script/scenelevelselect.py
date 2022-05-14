import pygame
import functionphysics

import var
import const
import asset

class UI():
    back_button = [1160, 40, 80, 80]

def loop():
    display()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.back_button, 2)

    for i in range(1, 8):
        for j in range(len(const.Level_List.connection[i])):
            temp_coordinate = [const.Level_List.position[i][0] + 40, const.Level_List.position[i][1] + 40, const.Level_List.position[const.Level_List.connection[i][j]][0] + 40, const.Level_List.position[const.Level_List.connection[i][j]][1] + 40]
            pygame.draw.line(var.screen, const.Color.black, temp_coordinate[:2], temp_coordinate[2:], 10)

    for i in range(1, 10):
        if var.Save.level_status[i] == 0:
            var.screen.blit(asset.Image.Button.level_locked, const.Level_List.position[i])
        
        elif var.Save.level_status[i] == 1:
            var.screen.blit(asset.Image.Button.level_unlocked, const.Level_List.position[i])

        elif var.Save.level_status[i] == 2:
            var.screen.blit(asset.Image.Button.level_cleared, const.Level_List.position[i])

    pygame.display.flip()

def mouse_up():
    pass