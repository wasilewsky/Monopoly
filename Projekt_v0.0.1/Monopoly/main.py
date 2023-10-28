import pygame
import os
import game_module as gm
import random


pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen = pygame.display.set_mode(gm.SIZESCREEN)


class Field:
    def __init__(self, x, y, image, name):
        self.name = name
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        #self.klikniety =

    def click(self):
        if self.enable:
            if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    return True

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))


class Board:
    def __init__(self, x, y, screen):
        self.pos_x = x
        self.pos_y = x
        self.screen = screen
        self.fields = []

    def create_fields(self):
        self.fields = []
        for x in range(0, 10):
            field = Field(self.pos_x + (x * 86), self.pos_y, gm.POLE1, f"{x}")
            self.fields.append(field)

        for y in range(0, 9):
            field = Field(self.pos_x + (10 * 86), self.pos_y + (y * 87), gm.POLE1, f"{y}")
            self.fields.append(field)

        for x in range(1, 10):
            field = Field(self.pos_x + (x * 86), self.pos_y + (8 * 87), gm.POLE1, f"{x}")
            self.fields.append(field)

        for y in range(0, 9):
            field = Field(self.pos_x, self.pos_y + (y * 87), gm.POLE1, f"{y}")
            self.fields.append(field)

    def draw(self):
        for field in self.fields:
            field.draw(self.screen)


#ruch - rzut dwoma kostkami
class Turn:
    def __init__(self):
        self.turn_value = 0
        self.kostki = []
        self.dublet = False

    def double_roll(self):
        kostka1 = Dice()
        kostka2 = Dice()
        kostka1.roll()
        kostka2.roll()
        if kostka1.show() == kostka2.show():
            self.dublet = True
        self.turn_value = kostka1.show() + kostka2.show()
        self.kostki = [kostka1.show(), kostka2.show()]

    def show_dice_value(self):
        return self.turn_value

    def show_dice(self):
        return self.kostki


# rzut kostką
class Dice:
    def __init__(self):
        self.value = 0

    def roll(self):
        value = random.randint(1, 6)
        self.value = value

    def show(self):
        return self.value


# przyciski do menu
class Button:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.b_image = image
        self.hitbox = pygame.Rect(self.x, self.y, self.b_image.get_width(), self.b_image.get_height())

    def click(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.b_image, (self.x, self.y))
        else:
            window.blit(self.b_image, (self.x+2, self.y+2))


def game():
    ruch = Turn()
    ruch.double_roll()

    gra = Board(0, 0, screen)
    gra.create_fields()


    window_open = True
    while window_open:
        screen.blit(gm.BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        text = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"rzut kostką: {ruch.show_dice_value()}", True, (0, 0, 0))
        screen.blit(text, (100, 150))
        text2 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"dobra ale osobno: {ruch.show_dice()[0]},{ruch.show_dice()[1]}", True, (0, 0, 0))
        screen.blit(text2, (100, 200))

        gra.draw()

        pygame.display.flip()


def main():
    window_open = True
    play_button = Button(screen.get_width()/2 - gm.PLAY_BUTTON.get_width()/2, 230, gm.PLAY_BUTTON)
    exit_button = Button(screen.get_width()/2 - gm.PLAY_BUTTON.get_width()/2, 480, gm.EXIT_BUTTON)
    while window_open:
        screen.fill(gm.LIGHTBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        if play_button.click():
            window_open = False
            if not game():
                window_open = True

        if exit_button.click():
            window_open = False

        play_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()

pygame.quit()

