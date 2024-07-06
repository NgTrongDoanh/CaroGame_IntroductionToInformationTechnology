import pygame
class Button:
    def __init__(self, pos, text_input, font, font_color, rect_width, rect_height):
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.font_color = font_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.font_color)
        self.buttom_color = (140, 70, 20)
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect = pygame.Rect(self.x - rect_width // 2, self.y - rect_height // 2, rect_width, rect_height)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
    
    def update(self, screen):
        pygame.draw.rect(screen, self.buttom_color, self.rect, border_radius = 30)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeSize(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.rect = pygame.Rect(self.x - (self.rect_width + 100)//2, self.y - (self.rect_height + 15) // 2, self.rect_width + 100, self.rect_height + 15)
        else:
            self.rect = pygame.Rect(self.x - self.rect_width // 2, self.y - self.rect_height // 2, self.rect_width, self.rect_height)


class Box():
    def __init__(self, pos, font, font_type, rect_width, rect_height, text_default):
        self.x = pos[0]
        self.y = pos[1]
        self.font = font
        self.font_color = (50, 50, 50)
        self.font_type = font_type
        self.text_length = 2 if font_type == "number" else 12
        self.text_input = str(text_default)
        self.box_color = (255, 255, 255)
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.rect = pygame.Rect(self.x - rect_width // 2, self.y - rect_height // 2, rect_width, rect_height)
        self.text = self.font.render(self.text_input, False, self.font_color)
        self.text_rect = pygame.Rect(self.x - rect_width // 2 + 25, self.y - self.text.get_height() // 2, rect_width, rect_height)
        self.active = False

    def update(self, screen):
        pygame.draw.rect(screen, self.box_color, self.rect)
        self.text = self.font.render(self.text_input, False, self.font_color)
        screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self,screen, position):
        if self.active:
            self.box_color = (225, 225, 225)
        else:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
                self.box_color = (225, 225, 225)
            else:
                self.box_color = (255, 255, 255)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(self.rect.left, self.rect.right) and event.pos[1] in range(self.rect.top, self.rect.bottom):
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text_input = self.text_input[:-1]
                else:
                    if len(self.text_input) < self.text_length:
                        self.text_input += event.unicode
    
class Panel():
    def __init__(self, pos, length, sound):
        self.pos_line = pos
        self.length = length
        self.sound = sound
        self.volume_default = self.sound.get_volume()
        self.volume = self.sound.get_volume()
        self.rect = pygame.Rect(self.pos_line[0] - 25 + self.length*self.volume, self.pos_line[1] - 18, 50, 36)
        self.active = False
    def update(self, SCREEN):
        pygame.draw.line(SCREEN, "white", self.pos_line, (self.pos_line[0]+self.length, self.pos_line[1]), 5)
        pygame.draw.rect(SCREEN, "white", self.rect, border_radius = 20)
        self.sound.set_volume(self.volume)

    def handle_event(self, event):
        offset_x = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                offset_x = event.pos[0] - self.rect.x

        elif event.type == pygame.MOUSEBUTTONUP:
            self.active = False

        elif event.type == pygame.MOUSEMOTION and self.active:
            if event.pos[0] - offset_x + 25 > self.pos_line[0] + self.length:
                self.rect.x = self.pos_line[0] + self.length - 25
            elif event.pos[0] - offset_x + 25 < self.pos_line[0]:
                self.rect.x = self.pos_line[0] - 25
            else:
                self.rect.x = event.pos[0] - offset_x

        self.volume = (self.rect.x + 25 - self.pos_line[0])/self.length

    def quit(self, isSave):
        if not isSave:
            self.sound.set_volume(self.volume_default)
            
        

