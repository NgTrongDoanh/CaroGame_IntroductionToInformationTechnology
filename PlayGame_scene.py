import pygame, Define
from Tools import Button
from BoardGame import Game_logic

def Back_Scene(SCREEN):
    text1 = Define.get_font(50).render("Are you sure you want", True, "#b68f40")
    rect1 = text1.get_rect(center=(640, 200))
    text2 = Define.get_font(50).render("to quit the game?", True, "#b68f40")
    rect2 = text2.get_rect(center=(640, 275))
    
    Continue_Button = Button(pos=(420, 400), text_input="No", font=Define.get_font(35), font_color="black", rect_width=320, rect_height=70)
    EndGame_Button = Button(pos=(840, 400), text_input="Yes", font=Define.get_font(35), font_color="black", rect_width=320, rect_height=70)
    
    running = True
    
    while running:
        SCREEN.blit(Define.Popup.BLUR_SURFACE, (0, 0))
        MOUSE_POS = pygame.mouse.get_pos()

        pygame.draw.rect(SCREEN, Define.Popup.POPUP_COLOR, (100, 155, 1080, 300), 5, border_radius=30)

        SCREEN.blit(text1, rect1)
        SCREEN.blit(text2, rect2)

        for button in [Continue_Button, EndGame_Button]:
            button.changeSize(MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Continue_Button.checkForInput(MOUSE_POS):
                    return True
                    running = False
                if EndGame_Button.checkForInput(MOUSE_POS):
                    return False
                    running = False
        pygame.display.update()

def PlayGame_scene(SCREEN):
    running = True
    p = [[0 for j in range(int(Define.BoardGame.NUMBER_WIDTH_CELL))] for i in range(int(Define.BoardGame.NUMBER_HEIGHT_CELL))]
    Back_Button = Button(pos=(1120, 670), text_input="Back", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)
    Board = Game_logic(int(Define.BoardGame.NUMBER_WIDTH_CELL), int(Define.BoardGame.NUMBER_HEIGHT_CELL), p, Define.BoardGame.PLAYER_X, Define.BoardGame.PLAYER_O)
    while running:
        SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        for button in [Back_Button]:
            button.changeSize(PLAY_MOUSE_POS)
            button.update(SCREEN)
        
        Board.PrintInfor(SCREEN)
        Board.DrawBoard(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.checkForInput(PLAY_MOUSE_POS):
                    running = Back_Scene(SCREEN)
                Board.checkForInput(PLAY_MOUSE_POS)
        pygame.display.update()
        
        if Board.End:
            running = False