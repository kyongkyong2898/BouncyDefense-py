import sys
import pygame

import asset
import var

import scenetitle
import scenesaveselect

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

def scene_loop():
    if var.scene == 'title':
        scenetitle.loop()

    elif var.scene == 'save_select':
        scenesaveselect.loop()

def font_init():
    asset.Font.title = pygame.font.SysFont(None, 60)

main()
