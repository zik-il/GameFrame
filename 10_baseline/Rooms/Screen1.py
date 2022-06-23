import random
from GameFrame import Level, Globals, TextObject
from Objects import Banner, Plane, Island1, Island2, Island3, Enemy


class Screen1(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # - Set Background image - #
        self.set_background_image('ocean.png')
        #self.set_background_scroll(10)

        self.add_room_object(Plane(self, 468, Globals.SCREEN_HEIGHT - 60))

        # self.add_room_object(Island1(self, random.randint(65, Globals.SCREEN_WIDTH - 130), -100))
        # self.add_room_object(Island2(self, random.randint(65, Globals.SCREEN_WIDTH - 130), -300))
        # self.add_room_object(Island3(self, random.randint(65, Globals.SCREEN_WIDTH - 130), -500))

        # - Add Banner for game info (lives) 800x56 - #
        self.add_room_object(Banner(self, 0, Globals.SCREEN_HEIGHT - 56))

        # - Add Text - #
        self.score_text = TextObject(self, 20, Globals.SCREEN_HEIGHT - 56, 'Lives: %i' % Globals.LIVES)
        self.score_text.depth = 200
        self.score_text.font = 'Arial'
        self.score_text.colour = (255, 255, 255)
        self.score_text.update_text()
        self.add_room_object(self.score_text)

        # Load Sounds
        self.fire_bullet_sound = self.load_sound("fire_bullet.wav")
        self.explosion_sound = self.load_sound("explosion.wav")

        # - Add first Enemy plane after 5 Seconds - #
        self.set_timer(150, self.add_enemy)


    def update_score(self, value):
        Globals.LIVES += value
        if Globals.LIVES == 0:
            self.running = False
            self.quitting = True

        self.score_text.text = 'Lives: %i' % Globals.LIVES
        self.score_text.update_text()

    def add_enemy(self):
        self.add_room_object(Enemy(self, random.randint(0, Globals.SCREEN_WIDTH), -100))
        # - Add new enemy every 2 seconds until max of 10 - #
        Globals.total_count += 1
        if Globals.total_count < 10:
            self.set_timer(60, self.add_enemy)

    def reset_game(self):
        Globals.LIVES = 3