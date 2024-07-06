import pygame, Menu, Define, Intro

pygame.init()
pygame.mixer.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(Define.Screen.SCREEN_TITLE)

Define.Sound.BACKGROUND_MUSIC.play(-1)

Intro.intro(SCREEN)

pygame.quit()