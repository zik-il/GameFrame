import random
from GameFrame import Globals
from GameFrame import RoomObject


class Enemy(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image1 = self.load_image('enemy1.png')
        self.image2 = self.load_image('enemy2.png')
        self.set_image(self.image1, 32, 31)
        self.image_1_set = True

        self.depth = 50

        self.y_speed = 5

        self.set_timer(2, self.update_image)

    def update_image(self):
        if self.image_1_set:
            self.image_1_set = False
            self.set_image(self.image1, 31, 27)
        else:
            self.image_1_set = True
            self.set_image(self.image2, 31, 27)
        self.set_timer(2, self.update_image)
            
    def step(self):
        if self.y >= Globals.SCREEN_HEIGHT:
            self.y = 0 - self.height*2
            self.x = random.randint(0, Globals.SCREEN_WIDTH - self.width)
