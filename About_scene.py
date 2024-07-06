import pygame, Define
from Tools import Button

def About_scene(SCREEN):
    running = True
    
    text = Define.get_font(100).render("GROUP 1", True, "#000000")
    rect = text.get_rect(center=(640, 100))
    
    Back_Button = Button(pos=(1120, 670), text_input="Back", font=Define.get_font(35), font_color="black", rect_width=200, rect_height=70)

    TrongDoanh = Define.get_font(35).render("Nguyen Trong Doanh - 23120004", True, "#000000")
    TrongDoanh_Rect = pygame.Rect(100, 200, TrongDoanh.get_width(), TrongDoanh.get_height())
    
    GiaHuy = Define.get_font(35).render("Thai Gia Huy - 23120008", True, "#000000")
    GiaHuy_Rect = pygame.Rect(100, 300, GiaHuy.get_width(), GiaHuy.get_height())

    PhanDai = Define.get_font(35).render("Phan Trong Dai - 23120026", True, "#000000")
    PhanDai_Rect = pygame.Rect(100, 400, PhanDai.get_width(), PhanDai.get_height())

    LeKhanh = Define.get_font(35).render("Nguyen Le Khanh - 23120052", True, "#000000")
    LeKhanh_Rect = pygame.Rect(100, 500, LeKhanh.get_width(), LeKhanh.get_height())

    while running:
        SCREEN.blit(Define.Screen.BACKGROUND, (0, 0))
        SCREEN.blit(text, rect)
        
        SCREEN.blit(TrongDoanh, TrongDoanh_Rect)
        SCREEN.blit(PhanDai, PhanDai_Rect)
        SCREEN.blit(GiaHuy, GiaHuy_Rect)
        SCREEN.blit(LeKhanh, LeKhanh_Rect)

        PLAY_MOUSE_POS = pygame.mouse.get_pos()
                
        Back_Button.changeSize(PLAY_MOUSE_POS)
        Back_Button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.checkForInput(PLAY_MOUSE_POS):
                    running = False
        pygame.display.update()
        
