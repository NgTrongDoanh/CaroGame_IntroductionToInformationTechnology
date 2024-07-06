import pygame, Define
from Tools import Button

pygame.mixer.init()

class Game_logic():
    def __init__(self, NumberWidthCell, NumberHeightCell, Board, Player1, Player2):
        self.NumberWidthCell = NumberWidthCell
        self.NumberHeightCell = NumberHeightCell
        self.Cell_Size = min(Define.BoardGame.BOARD_WIDTH // self.NumberWidthCell, Define.BoardGame.BOARD_HEIGHT // self.NumberHeightCell)
        self.Board = Board

        self.x0 = (Define.Screen.SCREEN_WIDTH - self.NumberWidthCell*self.Cell_Size)//2
        self.y0 = (Define.Screen.SCREEN_HEIGHT - self.NumberHeightCell*self.Cell_Size)//2
        self.xn = self.x0 + self.NumberWidthCell*self.Cell_Size
        self.yn = self.y0 + self.NumberHeightCell*self.Cell_Size

        self.PlayerX = Player1
        self.PlayerO = Player2

        self.X = Define.get_font_X_O(self.Cell_Size // 4*3).render('X', False, "blue")
        self.O = Define.get_font_X_O(self.Cell_Size // 4*3).render('O', False, "red")

        self.Turn = 1
        self.Turn_Color = "#800000"
        self.not_Turn_Color = "#000000"
        self.last_turn = [-1, -1]

        self.Score = [0, 0]
        self.End = False

    def Draw_Piece(self, SCREEN, row, col):
        if self.Board[row][col] == 1:
            text_Rect = self.X.get_rect(center=(self.x0 + col*self.Cell_Size + self.Cell_Size // 2, self.y0 + row*self.Cell_Size + self.Cell_Size // 2))
            SCREEN.blit(self.X, text_Rect)
        elif self.Board[row][col] == -1:
            text_Rect = self.O.get_rect(center=(self.x0 + col*self.Cell_Size + self.Cell_Size // 2, self.y0 + row*self.Cell_Size + self.Cell_Size // 2))
            SCREEN.blit(self.O, text_Rect)

    def DrawBoard(self, SCREEN):
        for x in range(self.x0 + self.Cell_Size, self.xn, self.Cell_Size):
            pygame.draw.line(SCREEN, (160, 85, 45), (x, self.y0), (x, self.yn - 5), 3)
        for y in range(self.y0 + self.Cell_Size, self.yn, self.Cell_Size):
            pygame.draw.line(SCREEN, (160, 85, 45), (self.x0, y), (self.xn - 5, y), 3)
        
        pygame.draw.rect(SCREEN, (140, 70, 20), ((self.x0, self.y0), (self.Cell_Size*self.NumberWidthCell, self.Cell_Size*self.NumberHeightCell)), width = 7, border_radius = 5)
        
        for row in range(self.NumberHeightCell):
            for col in range(self.NumberWidthCell):
                if self.Board[row][col] == 1:
                    self.Draw_Piece(SCREEN, row, col)
                elif self.Board[row][col] == -1:
                    self.Draw_Piece(SCREEN, row, col)
        pygame.display.update()

        isEnd = self.checkEnd(self.last_turn[0], self.last_turn[1])
        st = isEnd[1]
        end = isEnd[2]
        if isEnd[0] == -1:
            self.Score[1] += 1
            pygame.draw.line(SCREEN, "blue", (self.x0 + st[1]*self.Cell_Size + self.Cell_Size // 2, self.y0 + st[0]*self.Cell_Size + self.Cell_Size // 2), (self.x0 + end[1]*self.Cell_Size + self.Cell_Size // 2, self.y0 + end[0]*self.Cell_Size + self.Cell_Size // 2), 5)
            pygame.display.update()
            pygame.time.delay(2000)
            self.EndMatch(SCREEN)
        elif isEnd[0] == 1:
            self.Score[0] += 1
            pygame.draw.line(SCREEN, "red", (self.x0 + st[1]*self.Cell_Size + self.Cell_Size // 2, self.y0 + st[0]*self.Cell_Size + self.Cell_Size // 2), (self.x0 + end[1]*self.Cell_Size + self.Cell_Size // 2, self.y0 + end[0]*self.Cell_Size + self.Cell_Size // 2), 5)
            pygame.display.update()
            pygame.time.delay(2000)
            self.EndMatch(SCREEN)
        elif isEnd[0] == 0:
            self.Score[0] += 1
            self.Score[1] += 1
            self.EndMatch(SCREEN)
    
    def PrintInfor(self, SCREEN):
        if self.Turn == 1:
            Player1 = Define.get_font(35).render(f"{self.PlayerX}: X", True, self.Turn_Color)
            Rect1 = pygame.Rect(30, 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player1, Rect1)

            Player2 = Define.get_font(25).render(f"{self.PlayerO}: O", True, self.not_Turn_Color)
            Rect2 = pygame.Rect(Define.Screen.SCREEN_WIDTH - 30 - Player2.get_width(), 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player2, Rect2)
        else:
            Player1 = Define.get_font(25).render(f"{self.PlayerX}: X", True, self.not_Turn_Color)
            Rect1 = pygame.Rect(30, 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player1, Rect1)

            Player2 = Define.get_font(35).render(f"{self.PlayerO}: O", True, self.Turn_Color)
            Rect2 = pygame.Rect(Define.Screen.SCREEN_WIDTH - 30 - Player2.get_width(), 30, Player1.get_width(), Player1.get_height())
            SCREEN.blit(Player2, Rect2)
        
        score = Define.get_font(35).render(f"{self.Score[0]} : {self.Score[1]}", False, "brown3")
        score_rect = score.get_rect(center=(640, 50))
        SCREEN.blit(score, score_rect)

    def checkEnd(self, row, col): #return 0(Draw), 1(X win), -1(O win), 2(Nothing)
        st = end = [0, 0]
        if Define.Find_in(0, self.Board):
            # Kiem tra cot
            count = 0
            block = 0
            r = max(row - 1, 0)
            while (r > -1 and self.Board[r][col] == self.Board[row][col]):
                count = count + 1
                r = r - 1
            st = [r+1, col]
            if r == -1 or self.Board[r][col] == - self.Board[row][col]:
                block = block + 1
            r = min(row + 1 , self.NumberHeightCell)
            while ( r < self.NumberHeightCell and self.Board[r][col] == self.Board[row][col]):
                count = count + 1
                r = r + 1
            end = [r-1, col]
            if r == self.NumberHeightCell or self.Board[r][col] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                return [self.Board[row][col], st, end]

            # kiem tra hang
            count = 0
            block = 0
            c = max(col - 1, 0)
            while (c > -1 and self.Board[row][c] == self.Board[row][col]):
                count = count + 1
                c = c - 1
            st = [row, c + 1]
            if c == -1 or self.Board[row][c] == - self.Board[row][col]:
                block = block + 1
            c = min(col + 1 , self.NumberWidthCell)
            while (c < self.NumberWidthCell and self.Board[row][c] == self.Board[row][col]):
                count = count + 1
                c = c + 1
            end = [row, c - 1]
            if c == self.NumberWidthCell or self.Board[row][c] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                return [self.Board[row][col], st, end]

            # Kiem tra duong cheo chinh
            count = 0
            block = 0
            i = 1
            while (row + i < self.NumberHeightCell and col + i < self.NumberWidthCell and self.Board[row + i][col + i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            st = [row + i - 1, col + i - 1]
            if row + i == self.NumberHeightCell or col + i == self.NumberWidthCell or self.Board[row + i][col + i] == - self.Board[row][col]:
                block = block + 1
            i = 1
            while (row - i > -1 and col - i > -1 and self.Board[row - i][col - i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            end = [row - i + 1, col - i + 1]
            if row - i == -1 or col - i == -1 or self.Board[row - i][col - i] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                return [self.Board[row][col], st, end]

            # Kiem tra duong cheo phu
            count = 0
            block = 0
            i = 1
            while (row + i < self.NumberHeightCell and col - i > -1 and self.Board[row + i][col - i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            st = [row + i - 1, col - i + 1]
            if row + i == self.NumberHeightCell or col - i == -1 or self.Board[row + i][col - i] == - self.Board[row][col]:
                block = block + 1
            i = 1
            while (row - i > -1 and col + i < self.NumberWidthCell and self.Board[row - i][col + i] == self.Board[row][col]):
                count = count + 1
                i = i + 1
            end = [row - i + 1, col + i - 1]
            if row - i == -1 or col + i == self.NumberWidthCell or self.Board[row - i][col + i] == - self.Board[row][col]:
                block = block + 1
            if (count > 3 and block < 2):
                return [self.Board[row][col], st, end]
            
            return [2, st, end]
        else:
            return [0, st, end]

    def makeMove(self, row, col):
        if self.Board[row][col] == 0:
            self.Board[row][col] = self.Turn
            self.Turn *= -1
            self.last_turn = (row, col)
            Define.Sound.SOUND_EFFECT.play()

    def checkForInput(self, position):
        if position[0] in range(self.x0, self.xn) and position[1] in range(self.y0, self.yn):
            self.makeMove((position[1] - self.y0) // self.Cell_Size, (position[0] - self.x0) // self.Cell_Size)
        return self.End

    def ContinueGame(self):
        for row in range(self.NumberHeightCell):
            for col in range(self.NumberWidthCell):
                self.Board[row][col] = 0

    def EndGame(self, SCREEN):
        text = ""
        if self.Score[0] > self.Score[1]:
            text = Define.get_font(50).render(f"{self.PlayerX} WIN!", True, (140, 0, 0))
        elif self.Score[0] < self.Score[1]:
            text = Define.get_font(50).render(f"{self.PlayerO} WIN!", True, (140, 0, 0))
        else:
            text = Define.get_font(50).render(f"TWO PLAYER DRAW!", True, (140, 0, 0))

        rect = text.get_rect(center=(640, 270))
        
        Menu_Button = Button(pos=(640, 400), text_input="Menu", font=Define.get_font(35), font_color="black", rect_width=320, rect_height=70)
        
        running = True
        
        while running:
            SCREEN.blit(Define.Popup.BLUR_SURFACE, (0, 0))
            MOUSE_POS = pygame.mouse.get_pos()

            pygame.draw.rect(SCREEN, Define.Popup.POPUP_COLOR, (100, 155, 1080, 300), 5, border_radius=30)

            SCREEN.blit(text, rect)

            Menu_Button.changeSize(MOUSE_POS)
            Menu_Button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Menu_Button.checkForInput(MOUSE_POS):
                        self.End = True
                        running = False
            pygame.display.update()

    def EndMatch(self, SCREEN):
        text = Define.get_font(50).render("CONTINUE OR END GAME?", True, "#b68f40")
        rect = text.get_rect(center=(640, 250))
        
        Continue_Button = Button(pos=(420, 400), text_input="Continue", font=Define.get_font(35), font_color="black", rect_width=320, rect_height=70)
        EndGame_Button = Button(pos=(840, 400), text_input="End Game", font=Define.get_font(35), font_color="black", rect_width=320, rect_height=70)
        
        running = True
        
        while running:
            SCREEN.blit(Define.Popup.BLUR_SURFACE, (0, 0))
            MOUSE_POS = pygame.mouse.get_pos()

            pygame.draw.rect(SCREEN, Define.Popup.POPUP_COLOR, (100, 155, 1080, 300), 5, border_radius=30)

            SCREEN.blit(text, rect)

            for button in [Continue_Button, EndGame_Button]:
                button.changeSize(MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if Continue_Button.checkForInput(MOUSE_POS):
                        running = False
                        self.ContinueGame()
                    if EndGame_Button.checkForInput(MOUSE_POS):
                        self.EndGame(SCREEN)
                        running = False
            pygame.display.update()

    def quit(self):
        if self.End:
            return False
        return True