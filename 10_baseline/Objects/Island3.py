import random
from GameFrame import Globals
from GameFrame import RoomObject


class Island3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        image = self.load_image('island3.png')
        self.set_image(image, 64, 65)

        self.depth = -100

        self.y_speed = 4

    def step(self):
        if self.y >= Globals.SCREEN_HEIGHT:
            self.y = 0 - self.height*2
            self.x = random.randint(0, Globals.SCREEN_WIDTH - self.width)
