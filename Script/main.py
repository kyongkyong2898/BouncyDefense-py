import sys
import pygame

import var

def main():
    pygame.init()
    var.screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Bouncy Defense')
    
    while True:
        loop()

def loop():
    input_handle()

def input_handle():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

main()
