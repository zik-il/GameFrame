import pygame
from spritesheet import Spritesheet
from GameFrame import Globals
from GameFrame import RoomObject

class AnimatedObject(RoomObject):


    def __init__(self, room, x, y): # changed for RoomObject
        RoomObject.__init__(self, room, x, y) # changed for RoomObject
        self.LEFT_KEY, self.RIGHT_KEY = False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        #self.rect.midbottom = placement
        self.current_frame = 0
        self.last_updated = 0
        self.velocity = 0
        self.state = 'facing left'
        self.keys_are_pressed = False
        self.WAS_FACING_LEFT = True 
        self.current_image = self.idle_frames_left[0]
        self.Objclicked = True        
        self.st = 0 #variable for animation toggle steps

        # for RoomObject -#
        self.image = self.current_image

        # for RoomObject
        self.depth = 100 

        # - Register the object to handle key \ mouse events - #
        self.handle_key_events = True
        self.handle_mouse_events = True

        # - Allow bullet fire (limit firing) - #
        self.can_shoot = False

        # - Register collisions with enemy - #
        #self.register_collision_object('Enemy')



    def load_frames(self):
        my_spritesheet = Spritesheet('spritesheet.png')
        #pygame.image.load('MY_IMAGE_NAME.png').convert()
        
        self.walking_frames_left = [my_spritesheet.parse_sprite("L3E"), my_spritesheet.parse_sprite("L2E"),
                           my_spritesheet.parse_sprite("L1E")]
        
        self.walking_frames_right = []
        for frame in self.walking_frames_left:
            self.walking_frames_right.append(pygame.transform.flip(frame, True, False))

        # "idle frame length" has to be equal to "walking frame length" = 3
        self.idle_frames_left = [my_spritesheet.parse_sprite("L1E"),my_spritesheet.parse_sprite("L1E"),my_spritesheet.parse_sprite("L1E")]
        
        self.idle_frames_right = []
        for frame in self.idle_frames_left:
            self.idle_frames_right.append( pygame.transform.flip(frame,True, False))


    def key_pressed(self, key):    
        # character left right functionality using the keys
        # this event runs ***all the time*** even if no keys are pressed.
        # this is a "default idle state no key is pressed" if statement
        
        if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT] and not self.Objclicked:
            if self.WAS_FACING_LEFT:
                self.state = 'facing left'
            else:
                self.state = 'facing right'

        if key[pygame.K_LEFT]:
            self.keys_are_pressed = True
            self.state = 'moving left'  
            self.Objclicked = False            
            self.WAS_FACING_LEFT = True
            self.x += self.velocity

        if key[pygame.K_RIGHT]:
            self.keys_are_pressed = True
            self.state = 'moving right'
            self.WAS_FACING_LEFT = False
            self.Objclicked = False
            self.x += self.velocity
        
        self.set_state()    # set velocity according to state
        self.animate()      # set images


    def clicked(self, button_number):   # animation transition through steps by clicking them
        self.Objclicked = True  # nutrilize the "default idle no key is pressed" if statement in key_pressed() function
        self.toggle_state()     # circular steps
        self.set_state()        # sets velocity according to state
        self.animate()          # update the image according to state
        print(self.state)       # debugging animation state


    def toggle_state(self):
        print(self.st)
        if self.st==1 or self.st==7:
            self.state = 'moving left'
            self.st = 1
        if self.st==2:
            self.state = 'facing left'
        if self.st==3:
            self.state = 'facing right'     
        if self.st == 4:
            self.state = 'moving right'
        if self.st == 5:
            self.state = 'facing right'
        if self.st == 6:
            self.state = 'facing left'
        self.st +=1


    def set_state(self):
        if self.state == 'moving right':
            self.velocity = 2
        elif self.state == 'moving left':
            self.velocity = -2
        elif self.state == 'facing right':
            self.velocity = 0       
        elif self.state == 'facing left':
            self.velocity = 0

 
    def animate(self):
        now = pygame.time.get_ticks()  
        if now - self.last_updated > 100:
            self.last_updated = now
            self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)               
            if self.state == 'moving left':
                self.current_image = self.walking_frames_left[self.current_frame]
            elif self.state == 'moving right':
                self.current_image = self.walking_frames_right[self.current_frame]
            elif self.state == 'facing left':
                self.current_image = self.idle_frames_left[self.current_frame]
            elif self.state == 'facing right':
                self.current_image = self.idle_frames_right[self.current_frame]      

        # if now - self.last_updated > 200:
        #     self.last_updated = now
        #     self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
        #     if self.WAS_FACING_LEFT:
        #         self.current_image = self.idle_frames_left[self.current_frame]
        #     elif not self.WAS_FACING_LEFT:
        #         self.current_image = self.idle_frames_right[self.current_frame]    

        self.image = self.current_image # this actually draws the object in GAME FRAME (instead of calling blit)
        self.set_timer(1, self.animate)