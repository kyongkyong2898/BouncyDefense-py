import pygame
import functionphysics

import var
import const
import asset

class UI():
    back_button = [1160, 40, 80, 80]

class Arrow_Key_Pressed():
    arrow = {'up' : False, 'left' : False, 'down' : False, 'right' : False}

def loop():
    display()
    camera_move()

def display():
    var.screen.fill(const.Color.white)

    pygame.draw.rect(var.screen, const.Color.black, UI.back_button, 2)

    for i in range(1, 8):
        for j in range(len(const.Level_List.connection[i])):
            temp_coordinate = [const.Level_List.position[i][0] + 40 - var.Level_Select.camera[0], const.Level_List.position[i][1] + 40 - var.Level_Select.camera[1], const.Level_List.position[const.Level_List.connection[i][j]][0] + 40 - var.Level_Select.camera[0], const.Level_List.position[const.Level_List.connection[i][j]][1] + 40 - var.Level_Select.camera[1]]
            pygame.draw.line(var.screen, const.Color.black, temp_coordinate[:2], temp_coordinate[2:], 10)

    for i in range(1, 10):
        if var.Save.level_status[i] == 0:
            var.screen.blit(asset.Image.Button.level_locked, [const.Level_List.position[i][0] - var.Level_Select.camera[0], const.Level_List.position[i][1] - var.Level_Select.camera[1]])
        
        elif var.Save.level_status[i] == 1:
            var.screen.blit(asset.Image.Button.level_unlocked, [const.Level_List.position[i][0] - var.Level_Select.camera[0], const.Level_List.position[i][1] - var.Level_Select.camera[1]])

        elif var.Save.level_status[i] == 2:
            var.screen.blit(asset.Image.Button.level_cleared, [const.Level_List.position[i][0] - var.Level_Select.camera[0], const.Level_List.position[i][1] - var.Level_Select.camera[1]])

    pygame.display.flip()

def camera_move():
    if var.menu == False:
        if var.state == '':
            if Arrow_Key_Pressed.arrow['up'] == True:
                var.Level_Select.camera[1] -= 5

            if Arrow_Key_Pressed.arrow['left'] == True:
                var.Level_Select.camera[0] -= 5

            if Arrow_Key_Pressed.arrow['down'] == True:
                var.Level_Select.camera[1] += 5

            if Arrow_Key_Pressed.arrow['right'] == True:
                var.Level_Select.camera[0] += 5

def mouse_up():
    mouse = pygame.mouse.get_pos()

    if var.menu == False:
        if var.state == '':
            if functionphysics.point_inside_rect_list(mouse[0], mouse[1], UI.back_button):
                var.scene = 'title'
                return

            for i in range(1, 10):
                if functionphysics.point_inside_rect_list(mouse[0], mouse[1], [const.Level_List.position[i][0] - var.Level_Select.camera[0], const.Level_List.position[i][1] - var.Level_Select.camera[1]]  + [80, 80]):
                    var.scene = 'battle'
                    var.state = 'ready'

def key_down(key):
    if var.menu == False:
        if var.state == '':
            if key == pygame.K_w:
                Arrow_Key_Pressed.arrow['up'] = True

            elif key == pygame.K_a:
                Arrow_Key_Pressed.arrow['left'] = True

            elif key == pygame.K_s:
                Arrow_Key_Pressed.arrow['down'] = True

            elif key == pygame.K_d:
                Arrow_Key_Pressed.arrow['right'] = True

def key_up(key):
    if var.menu == False:
        if var.state == '':
            if key == pygame.K_w:
                Arrow_Key_Pressed.arrow['up'] = False

            elif key == pygame.K_a:
                Arrow_Key_Pressed.arrow['left'] = False

            elif key == pygame.K_s:
                Arrow_Key_Pressed.arrow['down'] = False

            elif key == pygame.K_d:
                Arrow_Key_Pressed.arrow['right'] = False