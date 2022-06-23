import pygame
from GameFrame import Globals
from GameFrame import RoomObject
from Objects.Bullet import Bullet


class Plane(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image1 = self.load_image('plane1.png')
        self.image2 = self.load_image('plane2.png')
        self.image3 = self.load_image('plane3.png')
        self.image4 = self.load_image('plane4.png')
        self.set_image(self.image1, 89, 55)
        self.curr_img = 1

        self.depth = 100

        # - Register the Plane to handle key events - #
        self.handle_key_events = True

        # - Allow bullet fire (limit firing) - #
        self.can_shoot = True

        # - Register collisions with enemy - #
        self.register_collision_object('Enemy')

        self.set_timer(5, self.update_image)

    def update_image(self):
        self.curr_img += 1
        if self.curr_img > 3:
            self.curr_img = 0
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
        self.set_timer(5, self.update_image)

    def step(self):
        # - Keep object in the room - #
        if self.rect.left <= 0:
            self.x = 0
        elif self.rect.right >= Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width
        if self.rect.top <= 0:
            self.y = 0
        elif self.rect.bottom >= Globals.SCREEN_HEIGHT - 60:
            self.y = Globals.SCREEN_HEIGHT - 60 - self.height

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.x -= 4
        if key[pygame.K_RIGHT]:
            self.x += 4
        if key[pygame.K_UP]:
            self.y -= 4
        if key[pygame.K_DOWN]:
            self.y += 4
        if key[pygame.K_SPACE]:
            self.fire_bullet()

    def fire_bullet(self):
        if self.can_shoot:
            self.room.fire_bullet_sound.play()
            new_bullet = Bullet(self.room, self.rect.centerx, self.y)
            new_bullet.x -= 4
            self.room.add_room_object(new_bullet)
            self.room.set_timer(15, self.reset_shooting)
            self.can_shoot = False

    def reset_shooting(self):
        self.can_shoot = True

    def handle_collision(self, other, other_type):
        if other_type == 'Enemy':
            self.delete_object(other)
            Globals.destroyed_count += 1
            if Globals.destroyed_count >= 10:
                self.room.running = False
                Globals.total_count = 0
                Globals.destroyed_count = 0
            self.room.update_score(-1)
            if Globals.LIVES <= 0:
                self.room.running = False
                self.room.quitting = True
