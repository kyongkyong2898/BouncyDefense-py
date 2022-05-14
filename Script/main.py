import sys
import pygame

import asset
import var

import scenetitle
import scenesaveselect
import scenelevelselect
import scenebattle
import scenecollection

def main():
    pygame.init()
    pygame.font.init()
    var.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Bouncy Defense')
    var.clock = pygame.time.Clock()
    
    font_init()

    while True:
        loop()

def loop():
    var.clock.tick(var.FPS)
    input_handle()
    scene_loop()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif var.scene == 'title':
            if event.type == pygame.MOUSEBUTTONUP:
                scenetitle.mouse_up()

        elif var.scene == 'save_select':
            if event.type == pygame.MOUSEBUTTONUP:
                scenesaveselect.mouse_up()

        elif var.scene == 'level_select':
            if event.type == pygame.MOUSEBUTTONUP:
                scenelevelselect.mouse_up()

        elif var.scene == 'battle':
            if event.type == pygame.MOUSEBUTTONUP:
                scenebattle.mouse_up()

            elif event.type == pygame.KEYDOWN:
                scenebattle.key_down()

        elif var.scene == 'collection':
            if event.type == pygame.MOUSEBUTTONUP:
                scenecollection.mouse_up()

def scene_loop():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'save_select':
        scenesaveselect.loop()

    elif var.scene == 'level_select':
        scenelevelselect.loop()

    elif var.scene == 'battle':
        scenebattle.loop()

    elif var.scene == 'collection':
        scenecollection.loop()

def font_init():
    asset.Font.title = pygame.font.SysFont(None, 60)

def image_load():
    asset.Image.Button.level_cleared = pygame.image.load('../Image/Button/LevelCleared.png')
    asset.Image.Button.level_locked = pygame.image.load('../Image/Button/LevelLocked.png')
    asset.Image.Button.level_unlocked = pygame.image.load('../Image/Button/LevelUnlocked.png')

main()
