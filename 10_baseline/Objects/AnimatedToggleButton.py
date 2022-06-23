from GameFrame import RoomObject
from GameFrame import Globals


class AnimatedToggleButton(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        self.state = "up"
        #button_image = self.load_image('Play_Button.png')
        #self.set_image(button_image, 150, 150)
        
        self.image1 = self.load_image('plane1_up.png')
        self.image2 = self.load_image('plane2_up.png')
        self.image3 = self.load_image('plane3_up.png')
        self.image4 = self.load_image('plane4_up.png')
        self.set_image(self.image1, 89, 55)
        self.curr_img = 1

        self.handle_mouse_events = True

        self.update_image()
        #self.set_timer(30, self.update_image)

    def update_image(self):
        self.curr_img += 1  #update the image each time the timer calls for update_image
        #if self.curr_img > 3:
        #    self.curr_img = 0
        if self.curr_img == 0:
            self.set_image(self.image1, 89, 55)
        elif self.curr_img == 1:
            self.set_image(self.image2, 89, 55)
        elif self.curr_img == 2:
            self.set_image(self.image3, 89, 55)
        elif self.curr_img == 3:
            self.set_image(self.image4, 89, 55)
        elif self.curr_img == 4:
            self.set_image(self.image1, 89, 55)
        
        self.set_timer(120, self.update_image)


    def toggle_state(self):
        if self.state == "up":
            self.state = "down"
            self.image1 = self.load_image('plane1_down.png')
            self.image2 = self.load_image('plane2_down.png')
            self.image3 = self.load_image('plane3_down.png')
            self.image4 = self.load_image('plane4_down.png')

        elif self.state == "down":
            self.state = "up"
            self.image1 = self.load_image('plane1_up.png')
            self.image2 = self.load_image('plane2_up.png')
            self.image3 = self.load_image('plane3_up.png')
            self.image4 = self.load_image('plane4_up.png')

        self.set_image(self.image1, 89, 55)        
        self.curr_img = 1
        self.update_image()

    def clicked(self, button_number):
        self.toggle_state()
