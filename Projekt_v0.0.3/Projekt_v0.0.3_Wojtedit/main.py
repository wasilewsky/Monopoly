import pygame
import os
import game_module as gm
import random


pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen = pygame.display.set_mode(gm.SIZESCREEN)


class Player:
    def __init__(self, color):
        self.color = None

    def show_color(self):
       pass

class Field:
    def __init__(self, x, y, image, name):
        self.name = name
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        self.owner = None

    def click(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            #if pygame.mouse.get_pressed()[0]:
            return True

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))

        if hasattr(self, 'typ'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{self.name} {self.typ}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + 10))

        if hasattr(self, 'cena'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"cena: {self.cena}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + 25))

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

def colorPick():
    redBtn = Button(screen.get_width() / 2 - gm.REDBTN.get_width() / 2, 180, gm.REDBTN)
    blueBtn = Button(screen.get_width() / 2 - gm.BLUEBTN.get_width() / 2, 300, gm.BLUEBTN)
    greenBtn = Button(screen.get_width() / 2 - gm.GREENBTN.get_width() / 2, 420, gm.GREENBTN)
    purpleBtn = Button(screen.get_width() / 2 - gm.PURPLEBTN.get_width() / 2, 540, gm.PURPLEBTN)

    window_open = True
    while window_open:
        screen.blit(gm.BACKGROUND, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        if redBtn.click():
            window_open = False
            Player.color = 'red'
            if not game():
                window_open = True

        if blueBtn.click():
            window_open = False
            Player.color = 'blue'
            if not game():
                window_open = True

        if greenBtn.click():
            window_open = False
            Player.color = 'green'
            if not game():
                window_open = True

        if purpleBtn.click():
            window_open = False
            Player.color = 'purple'
            if not game():
                window_open = True

        text = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"wybierz kolor", True, (0, 0, 0))
        screen.blit(text, (screen.get_width() / 2 - 100, 120))
        redBtn.draw(screen)
        blueBtn.draw(screen)
        greenBtn.draw(screen)
        purpleBtn.draw(screen)

        pygame.display.flip()

def game():
    ruch = Turn()
    ruch.double_roll()

    gra = Board(40, 40, screen)
    gra.create_fields()


    data = (('typ', 'cena', 'czynsz', 'czynsz_kolor', 'czynsz1', 'czynsz2', 'czynsz3', 'czynsz4', 'czynszh', 'kosztd', 'koszth', 'hipoteka', 'splatahipoteki'),
            ('START', ''),  # +200
            ('POLE', 60, 2, 4, 10, 30, 90, 160, 250, 50, 50, 30, 33),
            ('KASA_SPOL', ''),
            ('POLE', 60, 4, 8, 20, 60, 180, 320, 450, 50, 50, 30, 33),
            ('PODATEK_DOCHODOWY', 200),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110),  # DWORZEC
            ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55),
            ('SZANSA', ''),
            ('POLE', 100, 6, 12, 30, 90, 270, 400, 550, 50, 50, 50, 55),
            ('POLE', 120, 8, 16, 40, 100, 300, 450, 600, 50, 50, 60, 66),
            ('WIEZIENIE', ''),
            ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77),
            ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83), #ELEKTROWNIA JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
            ('POLE', 140, 10, 20, 50, 150, 450, 625, 750, 100, 100, 70, 77),
            ('POLE', 160, 12, 24, 60, 180, 500, 700, 900, 100, 100, 80, 88),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110),  # DWORZEC
            ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99),
            ('KASA_SPOLECZNA', ''),
            ('POLE', 180, 14, 28, 70, 200, 550, 750, 950, 100, 100, 90, 99),
            ('POLE', 200, 16, 32, 80, 22, 600, 800, 1000, 100, 100, 100, 110),
            ('BEZPLATNY_PARKING', ''),
            ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121),
            ('SZANSA', ''),
            ('POLE', 220, 18, 36, 90, 250, 700, 875, 1050, 150, 150, 110, 121),
            ('POLE', 240, 20, 40, 100, 300, 750, 925, 1100, 150, 150, 120, 132),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110),  # DWORZEC
            ('POLE', 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143),
            ('POLE', 22, 44, 110, 330, 800, 975, 1150, 150, 150, 130, 143),
            ('POLE', 150, 0, 0, 0, 0, 0, 0, 0, 0, 0, 75, 83),  # WODOCIAG, JESLI 1 ZAKLAD - 4*kostka, JESLI 2 - 10*kostka
            ('POLE', 280, 24, 48, 120, 360, 850, 1025, 1200, 150, 150, 140, 154),
            ('IDZ_DO_WIEZIENIA', ''),
            ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165),
            ('POLE', 300, 26, 52, 130, 390, 900, 1100, 1275, 200, 200, 150, 165),
            ('KASA_SPOLECZNA', ''),
            ('POLE', 320, 28, 56, 150, 450, 1000, 1200, 1400, 200, 200, 160, 176),
            ('POLE', 200, 25, 50, 100, 200, 0, 0, 0, 0, 0, 100, 110),  # DWORZEC
            ('SZANSA', ''),
            ('POLE', 350, 35, 70, 175, 500, 1100, 1300, 1500, 200, 200, 175, 193),
            ('PODATEK_DOCHODOWY_DO_ZAPLATY', 100),
            ('POLE', 400, 50, 100, 200, 600, 1400, 1700, 2000, 200, 200, 200, 220))

    #dodawanie atrybutow do pol
    for x in range(1, 41):
        if data[x][0] == 'POLE':
            for y in range(0, 12):
                gra.set_field_att(x, data[0][y], data[x][y])
        else:
            gra.set_field_att(x, data[0][0], data[x][0])



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
        screen.blit(text, (220, 160))
        text2 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"dobra ale osobno: {ruch.dice1},{ruch.dice2}", True, (0, 0, 0))
        screen.blit(text2, (220, 210))
        text3 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"kolor: {Player.color}", True, (0, 0, 0))
        screen.blit(text3, (220, 260))

        #przykład sprawdzania cznszu
        for field in gra.fields:
            if field.click():
                if hasattr(field, 'czynsz'):
                    text3 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"czynsz pola {field.name}: {field.czynsz}", True, (0, 0, 0))
                else:
                    text3 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"czynsz pola {field.name}: brak", True, (0, 0, 0))
                screen.blit(text3, (220, 260))

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
            if not colorPick():
                window_open = True

        if exit_button.click():
            window_open = False

        play_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main()

pygame.quit()
