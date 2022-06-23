import pygame
from menu import *
from GameFrame import Globals

class game():
    def __init__(self):
        #pygame.init()
        #self.running, self.playing = True, False
        self.Click = False
        self.RIGHT_KEY, self.LEFT_KEY, self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = Globals.SCREEN_WIDTH, Globals.SCREEN_HEIGHT
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        #self.font_name = 'FreeSans.ttf'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu
        self.curr_menu.display_menu()

    # def game_loop(self):
    #     while Globals.playing:
    #         self.check_events()
    #         if self.START_KEY:
    #             Globals.playing= False
    #         self.display.fill(self.BLACK)
    #         self.draw_text('Thanks for Playing', 20, self.DISPLAY_W/2, self.DISPLAY_H/2)
    #         self.window.blit(self.display, (0,0))
    #         pygame.display.update()
    #         self.reset_keys()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Globals.running, Globals.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = True
                if event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.LEFT_KEY = False
                elif event.key == pygame.K_RIGHT:
                    self.RIGHT_KEY = False
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.Click = True

    def reset_keys(self):
        #self.RIGHT_KEY, self.LEFT_KEY = False, False 
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
        return text_rect





