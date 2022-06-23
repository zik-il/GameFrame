from GameFrame import RoomObject
from GameFrame import Globals


class PlayButton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        button_image = self.load_image('Play_Button.png')
        self.set_image(button_image, 150, 150)

        self.handle_mouse_events = True

    def clicked(self, button_number):
        Globals.next_level += 1
        Globals.next_level %= len(Globals.levels)
        self.room.running = False
