import pygame, Define
from Tools import Button
from Setting_scene import Setting_scene
from PlayGame_scene import PlayGame_scene
from About_scene import About_scene

def main_menu(SCREEN):
    Menu_text = Define.get_font(100).render("MAIN MENU", True, "#000000")
    Menu_rect = Menu_text.get_rect(center=(640, 100))

    PlayGame_Button = Button(pos=(640, 250), text_input="Play Game", font=Define.get_font(35), font_color="black", rect_width=400, rect_height=70)
    Setting_Button = Button(pos=(640, 350), text_input="Setting", font=Define.get_font(35),font_color="black", rect_width=400, rect_height=70)
    Help_Button = Button(pos=(640, 450), text_input="About", font=Define.get_font(35), font_color="black", rect_width=400, rect_height=70)
    Quit_Button = Button(pos=(640, 550), text_input="QUIT", font=Define.get_font(35),font_color="black", rect_width=400, rect_height=70)
    
    running = True
    
    while running:        
        SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(Menu_text, Menu_rect)

        for button in [PlayGame_Button, Setting_Button, Help_Button, Quit_Button]:
            button.changeSize(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PlayGame_Button.checkForInput(MENU_MOUSE_POS):
                    PlayGame_scene(SCREEN)
                if Setting_Button.checkForInput(MENU_MOUSE_POS):
                    Setting_scene(SCREEN)
                if Help_Button.checkForInput(MENU_MOUSE_POS):
                    About_scene(SCREEN)
                if Quit_Button.checkForInput(MENU_MOUSE_POS):
                    running = False

        pygame.display.update()
