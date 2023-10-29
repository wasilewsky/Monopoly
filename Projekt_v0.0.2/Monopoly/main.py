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

    def click(self):
        if self.enable:
            if self.hitbox.collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    return True

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))
        text = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"{self.name}", True, (0, 0, 0))
        screen.blit(text, (self.pos_x + 10, self.pos_y + 10))


class Board:
    def __init__(self, x, y, screen):
        self.pos_x = x
        self.pos_y = x
        self.screen = screen
        self.fields = []
        self.data = (
            (gm.POLE1, 117, 117),
            (gm.POLE2, 72, 117),
            (gm.POLE3, 117, 72),
            (gm.POLE4, 72, 117),
            (gm.POLE5, 117, 72)
        )

    def create_fields(self):
        self.fields = []

        #lewa gora
        field = Field(self.pos_x, self.pos_y, self.data[0][0], f"21")
        self.fields.append(field)

        #gora
        number = 22
        for x in range(0, 9):
            if x == 1 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y, self.data[3][0], f"{number}")
            else:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y, self.data[1][0], f"{number}")
            self.fields.append(field)
            number += 1

        #prawa gora
        field = Field(self.pos_x + self.data[0][1] + 9*self.data[1][1], self.pos_y, self.data[0][0], f"31")
        self.fields.append(field)

        #lewa bok
        number = 20
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x, self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.data[4][0], f"{number}")
            else:
                field = Field(self.pos_x, self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.data[2][0], f"{number}")
            self.fields.append(field)
            number -= 1

        #lewa dol
        field = Field(self.pos_x, self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.data[0][0], f"11")
        self.fields.append(field)

        #dol
        number = 10
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.data[3][0], f"{number}")
            else:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.data[1][0], f"{number}")
            self.fields.append(field)
            number -= 1

        #prawa dol
        field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1], self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.data[0][0], f"1")
        self.fields.append(field)

        #prawa
        number = 32
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1], self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.data[4][0], f"{number}")
            else:
                field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1], self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.data[2][0], f"{number}")
            self.fields.append(field)
            number += 1

    def draw(self):
        for field in self.fields:
            field.draw(self.screen)

    def set_field_att(self, name, att, value):
        for field in self.fields:
            if field.name == f'{name}':
                setattr(field, f'{att}', value)


#ruch - rzut dwoma kostkami
class Turn:
    def __init__(self):
        self.turn_value = 0
        self.dice1 = 0
        self.dice2 = 0
        self.dublet = False

    def dice_roll(self):
        value = random.randint(1, 6)
        return value

    def double_roll(self):
        self.dice1 = self.dice_roll()
        self.dice2 = self.dice_roll()
        if self.dice1 == self.dice2:
            self.dublet = True
        self.turn_value = self.dice1 + self.dice2

    def show_turn_value(self):
        return self.turn_value

    def dice_pics(self):
        if self.dice1 == 1:
            img1 = gm.DICE1
        elif self.dice1 == 2:
            img1 = gm.DICE2
        elif self.dice1 == 3:
            img1 = gm.DICE3
        elif self.dice1 == 4:
            img1 = gm.DICE4
        elif self.dice1 == 5:
            img1 = gm.DICE5
        elif self.dice1 == 6:
            img1 = gm.DICE6

        if self.dice2 == 1:
            img2 = gm.DICE1
        elif self.dice2 == 2:
            img2 = gm.DICE2
        elif self.dice2 == 3:
            img2 = gm.DICE3
        elif self.dice2 == 4:
            img2 = gm.DICE4
        elif self.dice2 == 5:
            img2 = gm.DICE5
        elif self.dice2 == 6:
            img2 = gm.DICE6

        img1 = pygame.transform.scale(img1, (200, 200))
        img2 = pygame.transform.scale(img2, (200, 200))
        screen.blit(img1, (250, 300))
        screen.blit(img2, (500, 300))


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

    gra = Board(40, 40, screen)
    gra.create_fields()

    #dodawanie wartości
    '''
    dane = (
        (cena, czynsz),
        (60, 2, 4),
        (10, 6)
    )
    for x in range(1, 40):
        gra.set_field_att(1, dane[0][0], dane[0][1])
        gra.set_field_att(1, dane[0][1], dane[1][1])'''

    window_open = True
    while window_open:
        screen.blit(gm.BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        text = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"rzut kostką: {ruch.show_turn_value()}", True, (0, 0, 0))
        screen.blit(text, (220, 170))
        text2 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"dobra ale osobno: {ruch.dice1},{ruch.dice2}", True, (0, 0, 0))
        screen.blit(text2, (220, 220))
        ruch.dice_pics()

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

