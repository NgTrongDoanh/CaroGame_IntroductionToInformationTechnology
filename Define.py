import pygame, time
pygame.mixer.init()

class Screen:
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    SCREEN_TITLE = "Nhom 01 - Do An Game Caro"
    BACKGROUND = pygame.image.load("Assets/Background.png")

class Font:
    FONT_FILE_PATH = "FontText/KongText.ttf"
    FONT_COLOR = (0, 0, 0)
    FONT_X_O = "FontText/DeathBlood.otf"

class Popup:
    POPUP_COLOR = ("#c8c8c8")
    
    BLUR_SURFACE = pygame.Surface((Screen.SCREEN_WIDTH, Screen.SCREEN_HEIGHT), pygame.SRCALPHA)
    BLUR_SURFACE.fill((0, 0, 0, 100))

class BoardGame:
    BOARD_WIDTH = 1080
    BOARD_HEIGHT = 520
    NUMBER_WIDTH_CELL = "09"
    NUMBER_HEIGHT_CELL = "09"
    PLAYER_X = "Player 1"
    PLAYER_O = "Player 2"

class Sound:
    BACKGROUND_MUSIC = pygame.mixer.Sound("Assets/MusicBackground.mp3")
    BACKGROUND_MUSIC.set_volume(1)
    
    SOUND_EFFECT = pygame.mixer.Sound("Assets/WriteEffect.wav")
    SOUND_EFFECT.set_volume(100)


class Intro:
    def calculate_rect_size(ratioPostitionX,ratioPositionY,ratioWidth,ratioHeight):
        _width = Screen.SCREEN_WIDTH*ratioWidth
        _height = Screen.SCREEN_HEIGHT*ratioHeight
        _postionX = Screen.SCREEN_WIDTH* ratioPostitionX - _width//2
        _postionY = Screen.SCREEN_HEIGHT*ratioPositionY - _height//2
        return (_postionX,_postionY,_width,_height)
        
    LOGO_RECT = calculate_rect_size(1/2,1/2,1/3,1/3)
    LOGO_IMAGE = 'Assets/logo_caro.jpg'
    LOGO_IMAGE_SIZE = (400,400)
    LOGO_BACKGROUND_COLOR = (255,255,255)
    LOGO_BORDER_COLOR = (0,0,0)

    LOADING_BAR_RECT = calculate_rect_size(1/2,0.9,1/2,1/20)
    LOADING_BAR_COLOR = (0, 128, 0)
    LOADING_BAR_BACKGROUND_COLOR = (128, 128, 128)
    LOADING_TIME = 5000

def get_font(size):
    return pygame.font.Font(Font.FONT_FILE_PATH, size)

def get_font_X_O(size):
    return pygame.font.Font(Font.FONT_X_O, size)


def Find_in(a, p):
    for row in p:
        if a in row:
            return True
    return False