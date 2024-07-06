import pygame
from Define import *
from Menu import main_menu

def intro(SCREEN):
    loading_bar_length = Intro.LOADING_BAR_RECT[2]
    logo_image = pygame.image.load(Intro.LOGO_IMAGE)
    logo_image = pygame.transform.scale(logo_image, Intro.LOGO_IMAGE_SIZE)
    SCREEN.blit(logo_image, ((Screen.SCREEN_WIDTH-logo_image.get_width())//2, (Screen.SCREEN_HEIGHT-logo_image.get_height())//2))
    loading_bar_color = Intro.LOADING_BAR_COLOR
    loading_bar_rect = pygame.Rect(Intro.LOADING_BAR_RECT)
    pygame.draw.rect(SCREEN, Intro.LOADING_BAR_BACKGROUND_COLOR, Intro.LOADING_BAR_RECT)
    loading_time = Intro.LOADING_TIME
    start_time = pygame.time.get_ticks()
    
    running = True

    while running:        
        elapsed_time = pygame.time.get_ticks() - start_time
        loading_bar_rect.width = min(1,(elapsed_time / Intro.LOADING_TIME)) * loading_bar_length
        pygame.draw.rect(SCREEN, loading_bar_color, loading_bar_rect)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
        if elapsed_time > loading_time:
            running = False
            main_menu(SCREEN)

        pygame.display.update()