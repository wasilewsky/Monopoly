import pygame
import os
import game_module as gm
import random

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen = pygame.display.set_mode(gm.SIZESCREEN)


class Player:

    def __init__(self, name, color, money):
        self.color = color
        self.name = name
        self.position = 1
        self.money = money

    def move(self, step):
        self.position += step
        if self.position > 40:
            self.position -= 40
            self.money += 100
            # do zrobienia komunikat przeszedłeś przez start czy coś

    def get_position(self):
        return self.position


class PlayerTable:
    def __init__(self, x, y, color, money, name):
        self.pos_x = x
        self.pos_y = y
        self.color = color
        self.money = money
        self.name = name

    def draw(self, screen):
        # for x in player:

        colortable = (255, 255, 255)
        if hasattr(self, 'color'):
            if self.color == "red":
                colortable = (255, 0, 0)
            elif self.color == "green":
                colortable = (0, 255, 0)
            elif self.color == "blue":
                colortable = (0, 0, 255)
            elif self.color == "purple":
                colortable = (100, 0, 255)
            pygame.draw.rect(screen, (255, 255, 255), (self.pos_x, self.pos_y, 210, 117), 0)
            pygame.draw.rect(screen, colortable, (self.pos_x, self.pos_y, 210, 46), 0)
            pygame.draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, 210, 46), 2)
            pygame.draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, 210, 117), 2)
            text = pygame.font.Font.render(pygame.font.SysFont(None, 75), f"{self.name}", True, (0, 0, 0))
            # screen.blit(rectangle, (self.pos_x, self.pos_y))
            screen.blit(text, (self.pos_x + 60, self.pos_y))

        if hasattr(self, 'money'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 65), f"${self.money}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 20, self.pos_y + 60))


class Table:

    def __init__(self, x, y, screen, players):
        self.pos_x = x
        self.pos_y = y
        self.screen = screen
        self.color = []
        self.players = players

    def create_table(self):
        self.color = []
        ptable = PlayerTable(self.pos_x, self.pos_y, self.players[0].color, self.players[0].money,
                             self.players[0].name)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 225, self.pos_y, self.players[1].color, self.players[1].money,
                             self.players[1].name)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 450, self.pos_y, self.players[2].color, self.players[2].money,
                             self.players[2].name)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 675, self.pos_y, self.players[3].color, self.players[3].money,
                             self.players[3].name)
        self.color.append(ptable)

    # ===================================== dodałem bo wcześniej w nieskończonej pętli gry była metoda dreate_table
    # ===================================== by aktualizowało kasę i przez to zamulało grę
    # ===================================== Może lepiej całkowicie przerobić by PlayerTable korzystało z tablicy graczy
    # ===================================== players zamiast tworzyć pola, które trzeba aktualizować
    def update_players(self):
        for player in self.color:            # do zmiany nazwy
            player.money = self.players[self.color.index(player)].money
            # można dodać resztę parametrów

    def draw(self):
        for table in self.color:
            table.draw(self.screen)


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
            # if pygame.mouse.get_pressed()[0]:
            return True

    def set_player_vis(self, player, value):
        if player == 'p1':
            self.p1 = value
        if player == 'p2':
            self.p2 = value
        if player == 'p3':
            self.p3 = value
        if player == 'p4':
            self.p4 = value

    def draw(self, window):
        window.blit(self.image, (self.pos_x, self.pos_y))
        '''
        if hasattr(self, 'typ'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{self.name} {self.typ}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + 10))

        if hasattr(self, 'cena'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"cena: {self.cena}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 10, self.pos_y + 25))'''

        if self.p1:
            pygame.draw.rect(screen, 'RED', (
                self.pos_x + self.image.get_width() / 4, self.pos_y + self.image.get_height() / 4, 15, 15))
        if self.p2:
            pygame.draw.rect(screen, 'GREEN', (
                self.pos_x + self.image.get_width() / 4 + 20, self.pos_y + self.image.get_height() / 4, 15, 15))
        if self.p3:
            pygame.draw.rect(screen, 'BLUE', (
                self.pos_x + self.image.get_width() / 4, self.pos_y + self.image.get_height() / 4 + 20, 15, 15))
        if self.p4:
            pygame.draw.rect(screen, 'PURPLE', (
                self.pos_x + self.image.get_width() / 4 + 20, self.pos_y + self.image.get_height() / 4 + 20, 15, 15))


class Board:
    def __init__(self, x, y, screen):
        self.pos_x = x
        self.pos_y = x
        self.width = None
        self.height = None
        self.screen = screen
        self.fields = []
        self.data = (            # =========== w trakcie zamiany
            (gm.POLE1, 117, 117),
            (gm.POLE2, 72, 117),
            (gm.POLE3, 117, 72),
            (gm.POLE4, 72, 117),
            (gm.POLE5, 117, 72)
        )
        self.dane = (
            (117, 72),
            gm.POLESTART,
            gm.POLEBROWN,
            gm.POLEKASADOL,
            gm.POLEBROWN,
            gm.POLE4,        # =========== zrobić grafikę TAXDOL
            gm.POLESATELITAS,
            gm.POLELIGHTBLUE,
            gm.POLESZANSADOL,
            gm.POLELIGHTBLUE,
            gm.POLELIGHTBLUE,
            gm.POLEJAIL,
            gm.POLEPINK,
            gm.POLEINTERNET,
            gm.POLEPINK,
            gm.POLEPINK,
            gm.POLESATELITAW,
            gm.POLEORANGE,
            gm.POLEKASALEWO,
            gm.POLEORANGE,
            gm.POLEORANGE,
            gm.POLEPARKING,
            gm.POLERED,
            gm.POLESZANSAGORA,
            gm.POLERED,
            gm.POLERED,
            gm.POLESATELITAN,
            gm.POLEYELLOW,
            gm.POLEYELLOW,
            gm.POLECLOUD,
            gm.POLEYELLOW,
            gm.POLEGOTOJAIL,
            gm.POLEGREEN,
            gm.POLEGREEN,
            gm.POLEKASAPRAWO,
            gm.POLEGREEN,
            gm.POLESATELITAE,
            gm.POLESZANSAPRAWO,
            gm.POLEDARKBLUE,
            gm.POLETAX,
            gm.POLEDARKBLUE
        )

    def create_fields(self):   # możliwe, że trzeba będzie całkowicie zmienić by skalowało się z rozdzielczośćią
        self.fields = []
        self.width = 2 * self.data[0][1] + 9 * self.data[1][1]
        self.height = 2 * self.data[0][1] + 9 * self.data[2][2]

        # lewa gora
        field = Field(self.pos_x, self.pos_y, self.dane[21], f"21")
        self.fields.append(field)

        # gora
        number = 22
        for x in range(0, 9):
            if x == 1 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y, self.dane[number],
                              f"{number}")
            else:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y, self.dane[number],
                              f"{number}")
            self.fields.append(field)
            number += 1

        # prawa gora
        field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1], self.pos_y, self.dane[31], f"31")
        self.fields.append(field)

        # lewa bok
        number = 20
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x, self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number],
                              f"{number}")
            else:
                field = Field(self.pos_x, self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number],
                              f"{number}")
            self.fields.append(field)
            number -= 1

        # lewa dol
        field = Field(self.pos_x, self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[11], f"11")
        self.fields.append(field)

        # dol
        number = 10
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 5 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]),
                              self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[number], f"{number}")
            else:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]),
                              self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[number], f"{number}")
            self.fields.append(field)
            number -= 1

        # prawa dol
        field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1],
                      self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[1], f"1")
        self.fields.append(field)

        # prawa
        number = 32
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1],
                              self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number], f"{number}")
            else:
                field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1],
                              self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number], f"{number}")
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


class Turn:
    def __init__(self):
        self.turn_value = 0
        self.dice1 = 0
        self.dice2 = 0
        self.doublet = False

    def dice_roll(self):
        value = random.randint(1, 6)
        return value

    def double_roll(self):
        self.dice1 = self.dice_roll()
        self.dice2 = self.dice_roll()
        if self.dice1 == self.dice2:
            self.doublet = True
        self.turn_value = self.dice1 + self.dice2

    def show_turn_value(self):
        return self.turn_value

    def dice_pics(self):

        # jeszcze przyda się zmiana by sprawdzało i podmieniało tylko po rzucie (kliknięciu przycisku)
        # ============================================================================ dużo krótsza wersja
        dice_images = (gm.DICE1, gm.DICE2, gm.DICE3, gm.DICE4, gm.DICE5, gm.DICE6)
        for x in range(1, 7):
            if self.dice1 == x:
                img1 = dice_images[x-1]
            if self.dice2 == x:
                img2 = dice_images[x-1]
            print(x)

        '''if self.dice1 == 1:
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
            img2 = gm.DICE6'''
        # ============================================================================

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
            window.blit(self.b_image, (self.x + 2, self.y + 2))
        else:
            window.blit(self.b_image, (self.x, self.y))


def game(color):
    turn = Turn()
    rzut_button_clicked = False

    game = Board(40, 40, screen)
    game.create_fields()

    rzut_button = Button(1000, 800, gm.RZUT)

    player1 = Player('p1', None, 1500)
    player2 = Player('p2', None, 1500)
    player3 = Player('p3', None, 1500)
    player4 = Player('p4', None, 1500)
    players = [player1, player2, player3, player4]

    # ========================================================== krotsza wersja
    colors = ('red', 'blue', 'green', 'purple')
    for c in colors:
        players[colors.index(c)].color = c

    while players[0].color != color:
        TEMP = players[0].color
        players[0].color = players[1].color
        players[1].color = players[2].color
        players[2].color = players[3].color
        players[3].color = TEMP

    '''players[0].color = color
    if color == 'red':
        players[1].color = "blue"
        players[2].color = "green"
        players[3].color = "purple"
    if color == 'blue':
        players[1].color = "red"
        players[2].color = "green"
        players[3].color = "purple"
    if color == 'green':
        players[1].color = "blue"
        players[2].color = "red"
        players[3].color = "purple"
    if color == 'purple':
        players[1].color = "blue"
        players[2].color = "green"
        players[3].color = "red"'''
    # ==========================================================

    table = Table(1000, 40, screen, players)

    table.create_table()

    # dodawanie atrybutow do pol
    for x in range(1, 41):
        if gm.data[x][0] == 'POLE':
            for y in range(0, 12):
                game.set_field_att(x, gm.data[0][y], gm.data[x][y])
        else:
            game.set_field_att(x, gm.data[0][0], gm.data[x][0])

    window_open = True
    while window_open:
        screen.blit(gm.BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        game.draw()
        rzut_button.draw(screen)

        field = game.get_field(players[0].get_position())
        field.set_player_vis('p1', True)

        # ================================ do zmiany bo na sztywno na 1 pozycji
        field_one = game.get_field('1')
        field_one.set_player_vis('p2', True)
        field_one.set_player_vis('p3', True)
        field_one.set_player_vis('p4', True)
        # ================================

        if rzut_button.click():
            field.set_player_vis('p1', False)
            turn.double_roll()
            players[0].move(turn.show_turn_value())
            pygame.time.delay(1000)
            rzut_button_clicked = True

        if rzut_button_clicked:
            turn.dice_pics()

        text = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"rzut kostką: {turn.show_turn_value()}",
                                       True, (0, 0, 0))
        screen.blit(text, (220, 170))
        text2 = pygame.font.Font.render(pygame.font.SysFont(None, 72), f"dobra ale osobno: {turn.dice1},{turn.dice2}",
                                        True, (0, 0, 0))
        screen.blit(text2, (220, 220))

        # pokazywania atrybutow
        for field in game.fields:
            if field.click():
                pos_x = 520
                for att in gm.data[0]:
                    if hasattr(field, att):
                        text3 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{att}: {getattr(field, att)}",
                                                        True, (0, 0, 0))
                        screen.blit(text3, (220, pos_x))
                        pos_x += 22

        table.draw()
        table.update_players()
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
    play_button = Button(screen.get_width() / 2 - gm.PLAY_BUTTON.get_width() / 2, 230, gm.PLAY_BUTTON)
    exit_button = Button(screen.get_width() / 2 - gm.PLAY_BUTTON.get_width() / 2, 480, gm.EXIT_BUTTON)

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
