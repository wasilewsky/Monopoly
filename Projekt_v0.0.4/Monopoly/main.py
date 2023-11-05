import pygame
import os
import game_module as gm
import random


pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen = pygame.display.set_mode(gm.SIZESCREEN)




class Player:
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.position = 1
        self.money = 1200

    def show_color(self):
       return self.color

    def move(self, step):
        self.position += step
        if self.position > 40:
            self.position -= 40
            self.money += 100
            #komunikat przeszedłeś przez start czy coś

    def get_position(self):
        return self.position


class Field:
    def __init__(self, x, y, image, name):
        self.name = name
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        self.owner = None
        self.p1 = False
        self.p2 = False
        self.p3 = False
        self.p4 = False

    def click(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            #if pygame.mouse.get_pressed()[0]:
            return True

    def set_player_vis(self, player, value):
        if player == 'p1':
            self.p1 = value

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))

        if hasattr(self, 'typ'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{self.name} {self.typ}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + 10))

        if hasattr(self, 'cena'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"cena: {self.cena}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + 25))

        if self.p1:
            pygame.draw.rect(screen, 'RED', (self.pos_x + self.image.get_width()/4, self.pos_y + self.image.get_height()/4, 15, 15))
        if self.p2:
            pygame.draw.rect(screen, 'GREEN', (self.pos_x + self.image.get_width()/4 +20, self.pos_y + self.image.get_height()/4, 15, 15))
        if self.p3:
            pygame.draw.rect(screen, 'BLUE', (self.pos_x + self.image.get_width()/4, self.pos_y + self.image.get_height()/4 + 20, 15, 15))
        if self.p4:
            pygame.draw.rect(screen, 'PURPLE', (self.pos_x + self.image.get_width()/4 + 20, self.pos_y + self.image.get_height()/4 + 20, 15, 15))

class Board:
    def __init__(self, x, y, screen):
        self.pos_x = x
        self.pos_y = x
        self.width = None
        self.height = None
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
        self.width = 2*self.data[0][1] + 9*self.data[1][1]
        self.height = 2*self.data[0][1] + 9*self.data[2][2]

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
            if x == 2 or x == 4 or x == 5 or x == 7:
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
        pygame.draw.rect(screen, 'LIGHTBLUE', (self.pos_x, self.pos_y, self.width, self.height))
        for field in self.fields:
            field.draw(self.screen)

    def set_field_att(self, name, att, value):
        for field in self.fields:
            if field.name == f'{name}':
                setattr(field, f'{att}', value)

    def get_field(self, name):
        for field in self.fields:
            if field.name == f'{name}':
                return field


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


def game(color):
    #color = color # hubert masz tu wybrany kolor jako string
    ruch = Turn()
    rzut_clicked = False

    gra = Board(40, 40, screen)
    gra.create_fields()

    player1 = Player('p1', color)
    player2 = Player('p2', color)
    player3 = Player('p3', color)
    player4 = Player('p4', color)

    rzut = Button(1000, 800, gm.RZUT)



    #dodawanie atrybutow do pol
    for x in range(1, 41):
        if gm.data[x][0] == 'POLE':
            for y in range(0, 12):
                gra.set_field_att(x, gm.data[0][y], gm.data[x][y])
        else:
            gra.set_field_att(x, gm.data[0][0], gm.data[x][0])



    window_open = True
    while window_open:
        screen.blit(gm.BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        gra.draw()
        rzut.draw(screen)

        field = gra.get_field(player1.get_position())
        field.set_player_vis('p1', True)

        if rzut.click():
            field.set_player_vis('p1', False)
            ruch.double_roll()
            player1.move(ruch.show_turn_value())
            pygame.time.delay(1000)
            rzut_clicked = True

        if rzut_clicked:
            ruch.dice_pics()

        text = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"rzut {color} kostką: {ruch.show_turn_value()}", True, (0, 0, 0))
        screen.blit(text, (220, 170))
        text2 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"dobra ale osobno: {ruch.dice1},{ruch.dice2}", True, (0, 0, 0))
        screen.blit(text2, (220, 220))


        #pokazywania atrybutow
        for field in gra.fields:
            if field.click():
                pos_x = 520
                for att in gm.data[0]:
                    if hasattr(field, att):
                        text3 = pygame.font.Font.render(pygame.font.SysFont(None,20), f"{att}: {getattr(field, att)}", True, (0, 0, 0))
                        screen.blit(text3, (220, pos_x))
                        pos_x += 22







        pygame.display.flip()


def color():
    pygame.time.delay(100)
    window_open = True

    redBtn = Button(screen.get_width() / 2 - gm.REDBTN.get_width() / 2, 180, gm.REDBTN)
    blueBtn = Button(screen.get_width() / 2 - gm.BLUEBTN.get_width() / 2, 300, gm.BLUEBTN)
    greenBtn = Button(screen.get_width() / 2 - gm.GREENBTN.get_width() / 2, 420, gm.GREENBTN)
    purpleBtn = Button(screen.get_width() / 2 - gm.PURPLEBTN.get_width() / 2, 540, gm.PURPLEBTN)

    while window_open:
        screen.fill(gm.LIGHTBLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        if redBtn.click():
            window_open = False
            if not game("red"):
                window_open = True
        if blueBtn.click():
            window_open = False
            if not game("blue"):
                window_open = True
        if greenBtn.click():
            window_open = False
            if not game("green"):
                window_open = True
        if purpleBtn.click():
            window_open = False
            if not game("purple"):
                window_open = True

        redBtn.draw(screen)
        blueBtn.draw(screen)
        greenBtn.draw(screen)
        purpleBtn.draw(screen)

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
            if not color():
                window_open = True

        if exit_button.click():
            window_open = False

        play_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()

pygame.quit()

