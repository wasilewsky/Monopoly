import pygame
from ..sound import BUTTON_SOUND1


class Button:
    def __init__(self, x, y, image, is_visible):
        self.x = x
        self.y = y
        self.b_image = image
        self.hitbox = pygame.Rect(self.x, self.y, self.b_image.get_width(), self.b_image.get_height())
        self.visible = is_visible

    def click(self):
        if not self.visible:
            return
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                # make sound
                return True

    def set_visible(self, value):
        self.visible = value

    def draw(self, window):
        if not self.visible:
            return
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.b_image, (self.x + 2, self.y + 2))
        else:
            window.blit(self.b_image, (self.x, self.y))
