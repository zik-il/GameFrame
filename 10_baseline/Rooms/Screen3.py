from GameFrame import Level
from Objects import PlayButton
from Objects import QuitButton
from Objects import AnimatedToggleButton
from Objects import AnimatedObject


class Screen3(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        self.set_background_image('bricks.png')

        self.add_room_object(PlayButton(self, 225, 100))
        self.add_room_object(QuitButton(self, 425, 100))
        self.add_room_object(AnimatedToggleButton(self, 425, 300))
        self.add_room_object(AnimatedObject(self, 125, 300))