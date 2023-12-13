import pygame
import os
import game_module as gm
import random

pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen = pygame.display.set_mode(gm.SIZESCREEN)



class Message:
    def __init__(self):
        self.messages = []

    def show_message(self):
        pygame.draw.rect(screen, 'WHITE', (1000, 200, 900, 500), 0, 10, -10, -10, -10, -10)
        x = 230
        for m in self.messages:
            text = pygame.font.Font.render(pygame.font.SysFont(None, 40), f"{m}", True, (0, 0, 0))
            screen.blit(text, (1050, x))
            x += 45

    def add_message(self, message):  # ogarnięte zapisywanie 10 ostatnich wiadomości
        if len(self.messages) >= 10:
            self.messages.pop(0)
        self.messages.append(message)


class Player:
    def __init__(self, name, color, money, message):
        self.color = color
        self.name = name
        self.position = 1
        self.money = money
        self.prison = False
        self.message = message
        self.moving = False

    def move(self, step):
        self.moving = True
        self.position += step
        if self.position > 40:
            self.position -= 40
            self.money += 200
            # do zrobienia komunikat przeszedłeś przez start czy coś
            self.message.add_message(f"gracz {self.name} przeszeł przez START (+ $200)")

    def get_position(self):
        return self.position


class PlayerTable:
    def __init__(self, x, y, player):
        self.pos_x = x
        self.pos_y = y
        self.player = player

    def draw(self, screen):
        colortable = (255, 255, 255)
        if hasattr(self.player, 'color'):
            if self.player.color == "red":
                colortable = (255, 0, 0)
            elif self.player.color == "green":
                colortable = (0, 255, 0)
            elif self.player.color == "blue":
                colortable = (0, 0, 255)
            elif self.player.color == "purple":
                colortable = (100, 0, 255)
            pygame.draw.rect(screen, (255, 255, 255), (self.pos_x, self.pos_y, 210, 117), 0)
            pygame.draw.rect(screen, colortable, (self.pos_x, self.pos_y, 210, 46), 0)
            pygame.draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, 210, 46), 2)
            pygame.draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, 210, 117), 2)
            text = pygame.font.Font.render(pygame.font.SysFont(None, 75), f"{self.player.name}", True, (0, 0, 0))
            # screen.blit(rectangle, (self.pos_x, self.pos_y))
            screen.blit(text, (self.pos_x + 60, self.pos_y))

        if hasattr(self.player, 'money'):
            text = pygame.font.Font.render(pygame.font.SysFont(None, 65), f"${self.player.money}", True, (0, 0, 0))
            screen.blit(text, (self.pos_x + 20, self.pos_y + 60))


class Table:

    def __init__(self, x, y, screen, players):
        self.pos_x = x
        self.pos_y = y
        self.screen = screen
        self.players_table = []
        self.players = players

    def create_table(self):
        ptable = PlayerTable(self.pos_x, self.pos_y, self.players[0])
        self.players_table.append(ptable)

        ptable = PlayerTable(self.pos_x + 225, self.pos_y, self.players[1])
        self.players_table.append(ptable)

        ptable = PlayerTable(self.pos_x + 450, self.pos_y, self.players[2])
        self.players_table.append(ptable)

        ptable = PlayerTable(self.pos_x + 675, self.pos_y, self.players[3])
        self.players_table.append(ptable)

    def draw(self):
        for table in self.players_table:
            table.draw(self.screen)


class Field:
    def __init__(self, x, y, image, name, message):
        self.name = name
        self.image = image
        self.pos_x = x
        self.pos_y = y
        self.hitbox = pygame.Rect(self.pos_x, self.pos_y, self.image.get_width(), self.image.get_height())
        self.message = message
        self.owner = None
        self.red = False
        self.green = False
        self.blue = False
        self.purple = False
        self.players = []
        self.houses = 0

    def mouse_on_field(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            # if pygame.mouse.get_pressed()[0]:
            return True

    ################# Hubert
    def click(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    ################# H end
    def set_players_list(self, players):
        self.players = players

    def update_players_pos(self):
        for player in self.players:
            if f'{player.position}' == self.name:
                value = True
            else:
                value = False

            if player.color == 'red':
                self.red = value
            if player.color == 'green':
                self.green = value
            if player.color == 'blue':
                self.blue = value
            if player.color == 'purple':
                self.purple = value

    def draw(self, window):
        self.update_players_pos()

        window.blit(self.image, (self.pos_x, self.pos_y))

        player_index = [1, 2, 3, 4]  # zdobywamy indexy graczy z danym kolorem
        for p in self.players:
            if p.color == 'red':
                player_index[0] = self.players.index(p)
            if p.color == 'green':
                player_index[1] = self.players.index(p)
            if p.color == 'blue':
                player_index[2] = self.players.index(p)
            if p.color == 'purple':
                player_index[3] = self.players.index(p)

        if self.red:
            if self.name == '11' and self.players[player_index[0]].prison:
                pygame.draw.rect(screen, 'RED', (self.pos_x + 50, self.pos_y + 10, 15, 15))
            elif self.name == '11' and not self.players[player_index[0]].prison:
                pygame.draw.rect(screen, 'RED', (self.pos_x + 10, self.pos_y + 10, 15, 15))
            else:
                pygame.draw.rect(screen, 'RED', (
                self.pos_x + self.image.get_width() / 4, self.pos_y + self.image.get_height() / 4, 15, 15))
        if self.green:
            if self.name == '11' and self.players[player_index[1]].prison:
                pygame.draw.rect(screen, 'GREEN', (self.pos_x + 70, self.pos_y + 10, 15, 15))
            elif self.name == '11' and not self.players[player_index[1]].prison:
                pygame.draw.rect(screen, 'GREEN', (self.pos_x + 10, self.pos_y + 35, 15, 15))
            else:
                pygame.draw.rect(screen, 'GREEN', (
                self.pos_x + self.image.get_width() / 4 + 20, self.pos_y + self.image.get_height() / 4, 15, 15))
        if self.blue:
            if self.name == '11' and self.players[player_index[2]].prison:
                pygame.draw.rect(screen, 'BLUE', (self.pos_x + 50, self.pos_y + 30, 15, 15))
            elif self.name == '11' and not self.players[player_index[2]].prison:
                pygame.draw.rect(screen, 'BLUE', (self.pos_x + 10, self.pos_y + 60, 15, 15))
            else:
                pygame.draw.rect(screen, 'BLUE', (
                self.pos_x + self.image.get_width() / 4, self.pos_y + self.image.get_height() / 4 + 20, 15, 15))
        if self.purple:
            if self.name == '11' and self.players[player_index[3]].prison:
                pygame.draw.rect(screen, 'PURPLE', (self.pos_x + 70, self.pos_y + 30, 15, 15))
            elif self.name == '11' and not self.players[player_index[3]].prison:
                pygame.draw.rect(screen, 'PURPLE', (self.pos_x + 10, self.pos_y + 85, 15, 15))
            else:
                pygame.draw.rect(screen, 'PURPLE', (
                self.pos_x + self.image.get_width() / 4 + 20, self.pos_y + self.image.get_height() / 4 + 20, 15, 15))

        down = ('2', '4', '7', '9', '10')
        left = ('12', '14', '15', '17', '19', '20')
        up = ('22', '24', '25', '27', '28', '30')
        right = ('32', '33', '35', '38', '40')

        if self.houses > 0:
            house_image = gm.DOM_OBR
            house_image = pygame.transform.scale(house_image, (18, 18))

            if self.name in down:
                for i in range(self.houses):
                    window.blit(house_image, (self.pos_x + 3 + i * 16, self.pos_y + 3))
            if self.name in up:
                for i in range(self.houses):
                    window.blit(house_image, (self.pos_x + 3 + i * 16, self.pos_y + 117 - 3 - 18))
            if self.name in left:
                for i in range(self.houses):
                    window.blit(house_image, (self.pos_x + 117 - 3 - 18, self.pos_y + 3 + i * 16))
            if self.name in right:
                for i in range(self.houses):
                    window.blit(house_image, (self.pos_x + 3, self.pos_y + 3 + i * 16))

        if self.owner is not None:
            if self.name in down:
                pygame.draw.rect(screen, f'{self.owner.color.upper()}', (self.pos_x + 1, self.pos_y + 117 - 15, 70, 15))
            if self.name in up:
                pygame.draw.rect(screen, f'{self.owner.color.upper()}', (self.pos_x + 1, self.pos_y, 70, 15))
            if self.name in left:
                pygame.draw.rect(screen, f'{self.owner.color.upper()}', (self.pos_x, self.pos_y + 1, 15, 70))
            if self.name in right:
                pygame.draw.rect(screen, f'{self.owner.color.upper()}', (self.pos_x + 117 - 15, self.pos_y + 1, 15, 70))

    def add_house(self, player_color):
        if self.owner is None:
            self.message.add_message('Nie posiadasz tego pola')
            return
        if self.owner.color is not player_color:
            self.message.add_message('Nie posiadasz tego pola')
            return
        if self.owner.money < self.koszt_domu:
            self.message.add_message('Nie stać cb na domek')
            return
        if not self.houses == 4:
            self.houses += 1
            self.message.add_message(f'Kupiony domek (kasa - ${self.koszt_domu})')
            self.owner.money -= self.koszt_domu
        else:
            self.message.add_message('Maksymalna liczba domków')

    def buy_field(self, player_color):
        fields = ('2', '4', '7', '9', '10', '12', '14', '15', '17', '19', '20', '22', '24', '25', '27', '28', '30', '32', '33', '35', '38', '40')

        if self.name not in fields:
            self.message.add_message('Nie można kupić danego pola')
            return
        if self.owner is not None and self.owner.color is not player_color:
            self.message.add_message(f'Pole już należy do gracza: {self.owner.name}')
            return
        if self.owner is not None and self.owner.color is player_color:
            self.message.add_message(f'Pole już należy do ciebie')
            return
        for player in self.players:
            if player.color == player_color:
                if player.money < self.cena:
                    self.message.add_message(f'Masz za mało kasy')
                    return
                self.owner = player
                self.message.add_message(f'Kupione pole {self.name} (kasa - ${self.cena})')
                self.owner.money -= self.cena


class Board:
    def __init__(self, x, y, screen, message):
        self.pos_x = x
        self.pos_y = x
        self.width = None
        self.height = None
        self.screen = screen
        self.fields = []
        self.message = message
        self.data = (  # =========== w trakcie zamiany
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
            gm.POLETAXDOL,
            gm.POLESATELITAS,
            gm.POLELIGHTBLUE,
            gm.POLESZANSADOL,
            gm.POLELIGHTBLUE,
            gm.POLELIGHTBLUE,
            gm.POLEJAIL,
            gm.POLEPINK,
            gm.POLEELEKTROSLON,  # zmienione POLEINTERNET
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
            gm.POLEELEKTROATOM,  # zmienione POLECRYPTO; POLECLOUD
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

    def create_fields(self):  # możliwe, że trzeba będzie całkowicie zmienić by skalowało się z rozdzielczośćią
        self.fields = []
        self.width = 2 * self.data[0][1] + 9 * self.data[1][1]
        self.height = 2 * self.data[0][1] + 9 * self.data[2][2]

        # lewa gora
        field = Field(self.pos_x, self.pos_y, self.dane[21], f"21", self.message)
        self.fields.append(field)

        # gora
        number = 22
        for x in range(0, 9):
            if x == 1 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y, self.dane[number],
                              f"{number}", self.message)
            else:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]), self.pos_y, self.dane[number],
                              f"{number}", self.message)
            self.fields.append(field)
            number += 1

        # prawa gora
        field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1], self.pos_y, self.dane[31], f"31", self.message)
        self.fields.append(field)

        # lewa bok
        number = 20
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x, self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number],
                              f"{number}", self.message)
            else:
                field = Field(self.pos_x, self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number],
                              f"{number}", self.message)
            self.fields.append(field)
            number -= 1

        # lewa dol
        field = Field(self.pos_x, self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[11], f"11", self.message)
        self.fields.append(field)

        # dol
        number = 10
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 5 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]),
                              self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[number], f"{number}", self.message)
            else:
                field = Field(self.pos_x + self.data[0][1] + (x * self.data[1][1]),
                              self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[number], f"{number}", self.message)
            self.fields.append(field)
            number -= 1

        # prawa dol
        field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1],
                      self.pos_y + self.data[0][2] + 9 * self.data[2][2], self.dane[1], f"1", self.message)
        self.fields.append(field)

        # prawa
        number = 32
        for x in range(0, 9):
            if x == 2 or x == 4 or x == 7:
                field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1],
                              self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number], f"{number}", self.message)
            else:
                field = Field(self.pos_x + self.data[0][1] + 9 * self.data[1][1],
                              self.pos_y + self.data[0][2] + (x * self.data[2][2]), self.dane[number], f"{number}", self.message)
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

    def add_players_to_field(self, players):
        for field in self.fields:
            field.set_players_list(players)

    def buy_house(self, current_player):
        current_field = self.get_field(current_player.get_position())
        current_field.add_house(current_player.color)

    def buy_field(self, current_player):
        current_field = self.get_field(current_player.get_position())
        current_field.buy_field(current_player.color)


class Dice:
    def __init__(self):
        self.turn_value = 0
        self.dice1 = 0
        self.dice2 = 0
        self.doublet = False

    @staticmethod
    def dice_roll():
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
                img1 = dice_images[x - 1]
            if self.dice2 == x:
                img2 = dice_images[x - 1]

        if self.dice1 > 0 and self.dice2 > 0:
            img1 = pygame.transform.scale(img1, (200, 200))
            img2 = pygame.transform.scale(img2, (200, 200))
            screen.blit(img1, (250, 300))
            screen.blit(img2, (500, 300))


# przyciski do menu
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


class System:
    def __init__(self):
        self.selected_color = None
        self.message = None
        self.dice = None
        self.game_board = None
        self.rzut_button = None
        self.kup_button = None
        self.dom_button = None
        self.dalej_button = None
        self.players = None
        self.table = None
        self.rzut_button_on = True
        self.current_player_index = 0
        ####### Hubert
        self.chance_card = None
        self.display_time = 2000
        self.display_start_time = 0
        self.show_chance_card = False
        self.display_start_time_chance = 0
        self.show_card = False
        self.display_start_time_card = 0
        ####### H end

    def create_game(self, c):
        self.selected_color = c
        self.message = Message()
        self.dice = Dice()
        self.game_board = Board(40, 40, screen, self.message)

        self.game_board.create_fields()
        self.rzut_button = Button(1000, 800, gm.RZUT, True)
        self.kup_button = Button(1220, 800, gm.KUP, True)
        self.dom_button = Button(1440, 800, gm.DOM, True)
        self.dalej_button = Button(1660, 800, gm.DALEJ, True)

        player1 = Player('p1', None, 1500, self.message)
        player2 = Player('p2', None, 1500, self.message)
        player3 = Player('p3', None, 1500, self.message)
        player4 = Player('p4', None, 1500, self.message)
        self.players = [player1, player2, player3, player4]

        self.set_color()

        self.game_board.add_players_to_field(self.players)  # każde pole ma dostęp do graczy - potrzebne do więzienia
        self.table = Table(1000, 40, screen, self.players)
        self.table.create_table()

        self.set_field_att()

    def set_color(self):
        colors = ['red', 'blue', 'green', 'purple']
        while colors[0] != self.selected_color:
            c = colors[1:4]
            c.append(colors[0])
            colors = c
        for col in colors:
            self.players[colors.index(col)].color = col

    def set_field_att(self):
        for x in range(1, 41):
            if gm.data[x][0] == 'POLE':
                for y in range(0, 15):
                    self.game_board.set_field_att(x, gm.data[0][y], gm.data[x][y])
            else:
                self.game_board.set_field_att(x, gm.data[0][0], gm.data[x][0])

    def draw_card(self):
        att2 = ''
        for field in self.game_board.fields:
            if field.mouse_on_field() and field.typ == 'POLE':
                pos_y = 520
                pos_x = 220
                # rysowanie karty (tło)
                pygame.draw.rect(screen, 'WHITE', (pos_x - 13, pos_y - 13, 176, pos_x + 66), 0, 10, -10, -10, -10,
                                 -10)  # tło karty
                pygame.draw.rect(screen, field.kolor, (pos_x - 7, pos_y - 7, 164, 54), 0, 10, -10, -10, -10,
                                 -10)  # tło kolor
                pygame.draw.rect(screen, (0, 0, 0), (pos_x - 10, pos_y - 10, 170, pos_x + 60), 2, 10, -10, -10, -10,
                                 -10)  # ramka
                pygame.draw.rect(screen, (0, 0, 0), (pos_x - 7, pos_y - 7, 164, 54), 2, 10, -10, -10, -10,
                                 -10)  # ramka koloru
                text5 = pygame.font.Font.render(pygame.font.SysFont(None, 30), f"{field.nazwa}", True, (0, 0, 0))
                screen.blit(text5, (pos_x, (pos_y + 12)))
                # ======================
                if field.cena == 200 and field.czynsz == 25:  # Tylko satelity kosztuja 200 i maja czynsz 20
                    text6 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"Czynsz: ", True, (0, 0, 0))
                    text8 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"Przy 2 stacjach: ", True,
                                                    (0, 0, 0))
                    text9 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"Przy 3 stacjach: ", True,
                                                    (0, 0, 0))
                    text10 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"Przy 4 stacjach: ", True,
                                                     (0, 0, 0))
                    for att in gm.data[0]:
                        if att not in ['typ', 'cena', 'czynsz_z_3', 'czynsz_z_4', 'czynsz_z_hotelem', 'koszt_domu',
                                       'koszt_hotelu', 'kolor', 'nazwa', 'hipoteka', 'splata_hipoteki']:
                            if hasattr(field, att):
                                text7 = pygame.font.Font.render(pygame.font.SysFont(None, 20),
                                                                f"${getattr(field, att)}",
                                                                True, (0, 0, 0))
                                screen.blit(text7, (pos_x + 120, pos_y + 70))
                                pos_y += 50
                    screen.blit(text6, (pos_x - 5, pos_y - 130))
                    screen.blit(text8, (pos_x - 5, pos_y - 80))
                    screen.blit(text9, (pos_x - 5, pos_y - 30))
                    screen.blit(text10, (pos_x - 5, pos_y + 20))

                elif field.cena == 150 and field.czynsz == 0:  # Tylko Starlink i Kryptowaluty kosztuja 150 i maja czynsz 0:
                    text11 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"        Przy posiadaniu", True,
                                                     (0, 0, 0))
                    screen.blit(text11, (pos_x - 5, pos_y + 60))
                    text12 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"   1 Zakładu, czynsz jest", True,
                                                     (0, 0, 0))
                    screen.blit(text12, (pos_x - 5, pos_y + 80))
                    text13 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"  czterokrotnością ilości",
                                                     True,
                                                     (0, 0, 0))
                    screen.blit(text13, (pos_x - 5, pos_y + 100))
                    text14 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"     wyrzuconych oczek.",
                                                     True,
                                                     (0, 0, 0))
                    screen.blit(text14, (pos_x - 5, pos_y + 120))

                    text11 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"        Przy posiadaniu", True,
                                                     (0, 0, 0))
                    screen.blit(text11, (pos_x - 5, pos_y + 180))
                    text12 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f" 2 Zakładów, czynsz jest", True,
                                                     (0, 0, 0))
                    screen.blit(text12, (pos_x - 5, pos_y + 200))
                    text13 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"    dziesięciokrotnością ",
                                                     True,
                                                     (0, 0, 0))
                    screen.blit(text13, (pos_x - 5, pos_y + 220))
                    text14 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"ilości wyrzuconych oczek.",
                                                     True,
                                                     (0, 0, 0))
                    screen.blit(text14, (pos_x - 5, pos_y + 240))

                else:
                    for att in gm.data[0]:
                        if att not in ['typ', 'kolor', 'nazwa', 'hipoteka', 'splata_hipoteki']:
                            att2 = att
                            if att == 'czynsz_z_kolorem':
                                att2 = 'czynsz z kolorem'
                            elif att == 'czynsz_z_1':
                                att2 = 'czynsz z 1'
                            elif att == 'czynsz_z_2':
                                att2 = 'czynsz z 2'
                            elif att == 'czynsz_z_3':
                                att2 = 'czynsz z 3'
                            elif att == 'czynsz_z_4':
                                att2 = 'czynsz z 4'
                            elif att == 'czynsz_z_hotelem':
                                att2 = 'czynsz z hotelem'
                            elif att == 'koszt_domu':
                                att2 = 'koszt domu'
                            elif att == 'koszt_hotelu':
                                att2 = 'koszt hotelu'
                            if hasattr(field, att):
                                text3 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{att2}: ", True,
                                                                (0, 0, 0))
                                text4 = pygame.font.Font.render(pygame.font.SysFont(None, 20),
                                                                f"${getattr(field, att)}",
                                                                True, (0, 0, 0))
                                screen.blit(text3, (pos_x - 5, pos_y + 54))
                                screen.blit(text4, (pos_x + 120, pos_y + 54))
                                pos_y += 22

    ############################## Hubert
    def random_chance(self):
        return random.choice(gm.chance_cards)

    def random_card(self):
        return random.choice(gm.cards)

    def set_chance_card(self):
        for field in self.game_board.fields:
            if field.click() and field.typ == 'SZANSA':
                self.chance_card = self.random_chance()
                self.show_chance_card = True
                self.display_start_time_chance = pygame.time.get_ticks()
                pygame.time.delay(500)

            elif field.click() and field.typ == 'KASA_SPOLECZNA':
                self.card = self.random_card()
                self.show_card = True
                self.display_start_time_card = pygame.time.get_ticks()
                pygame.time.delay(500)

    def display_chance_card(self):
        if self.show_chance_card:
            pos_y = 570
            pos_x = 400
            text2 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{self.chance_card[1]}", True, (0, 0, 0))
            text = pygame.font.Font.render(pygame.font.SysFont(None, 40), f"KARTA SZANSY", True, (0, 0, 0))
            pygame.draw.rect(screen, 'WHITE', (400 - 13, 520 - 13, 410, 100), 0, 10, -10, -10, -10,
                             -10)  # tło karty
            pygame.draw.rect(screen, (0, 0, 0), (398 - 10, 518 - 10, 408, 98), 2, 10, -10, -10, -10,
                             -10)  # ramka
            screen.blit(text2, (pos_x, pos_y))
            screen.blit(text, (480, 520))

            # Sprawdź czy minął czas wyświetlania
            current_time = pygame.time.get_ticks()
            if current_time - self.display_start_time_chance >= 2000:
                self.show_chance_card = False

    def display_card(self):
        if self.show_card:
            pos_y = 570
            pos_x = 400
            text2 = pygame.font.Font.render(pygame.font.SysFont(None, 20), f"{self.card[1]}", True, (0, 0, 0))
            text = pygame.font.Font.render(pygame.font.SysFont(None, 40), f"KASA SPOLECZNA", True, (0, 0, 0))
            pygame.draw.rect(screen, 'WHITE', (400 - 13, 520 - 13, 410, 100), 0, 10, -10, -10, -10,
                             -10)  # tło karty
            pygame.draw.rect(screen, (0, 0, 0), (398 - 10, 518 - 10, 408, 98), 2, 10, -10, -10, -10,
                             -10)  # ramka
            screen.blit(text2, (pos_x, pos_y))
            screen.blit(text, (480, 520))

            # Sprawdź czy minął czas wyświetlania
            current_time = pygame.time.get_ticks()
            if current_time - self.display_start_time_card >= 2000:
                self.show_card = False
    ################################### H end

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        if self.current_player_index == 0:
            self.message.add_message('@ twoja kolej:')
            self.dalej_button.set_visible(True)

    def ai_actions(self):
        if self.current_player_index != 0:
            # akcje ai graczy
            self.message.add_message(f"@ ruch gracza {self.players[self.current_player_index].name}:")
            self.draw_game(True, False)
            pygame.time.delay(1000)
            self.dice.double_roll()
            self.message.add_message(
                f"gracz {self.players[self.current_player_index].name} poruszył się o {self.dice.show_turn_value()}")
            for x in range(0, self.dice.show_turn_value()):
                self.players[self.current_player_index].move(1)
                pygame.time.delay(200)
                self.draw_game(True, False)

            # ==================  kupowanie pola jak więcej niż 1000 money
            fields = (
                '2', '4', '7', '9', '10', '12', '14', '15', '17', '19', '20', '22', '24', '25', '27', '28', '30', '32',
                '33',
                '35', '38', '40')
            actual_field = None

            for field in self.game_board.fields:
                if field.name == str(self.players[self.current_player_index].get_position()):
                    actual_field = field
            if actual_field is not None:
                print("not none")
                if actual_field.name in fields:
                    print("in fields")
                    if actual_field.owner is None:
                        print("owner none")
                        print(self.players[self.current_player_index].money)
                        print(actual_field.koszt_domu)
                        if self.players[self.current_player_index].money > actual_field.koszt_domu:
                            print("stać go")
                            actual_field.buy_field(self.players[self.current_player_index].color)
                            pygame.time.delay(1000)
                            self.draw_game(True, False)
                            print("buy")
                    how_long = random.randint(1, 4)
                    while how_long > 0:
                        if actual_field.owner is not None and actual_field.owner.color is self.players[self.current_player_index].color:
                            if self.players[self.current_player_index].money > actual_field.cena:
                                if actual_field.houses != 4:
                                    actual_field.add_house(self.players[self.current_player_index].color)
                                    pygame.time.delay(1000)
                                    self.draw_game(True, False)
                                    print("buy")
                        how_long -= 1
            # ==================
            self.switch_player()

    def draw_game(self, ai_turn, buttons):
        self.game_board.draw()
        self.dice.dice_pics()
        self.table.draw()
        self.message.show_message()
        self.draw_card()
        ## Hubert
        self.set_chance_card()
        self.display_chance_card()
        self.display_card()
        ## H end
        fields = (
        '2', '4', '7', '9', '10', '12', '14', '15', '17', '19', '20', '22', '24', '25', '27', '28', '30', '32', '33',
        '35', '38', '40')

        if self.current_player_index != 0 and not ai_turn:
            self.ai_actions()
        if self.current_player_index == 0 and buttons:
            self.dalej_button.set_visible(True)
            if self.rzut_button_on:
                self.rzut_button.set_visible(True)
                self.kup_button.set_visible(False)
                self.dom_button.set_visible(False)
                self.dalej_button.set_visible(False)
            else:
                actual_field = None
                self.rzut_button.set_visible(False)
                self.kup_button.set_visible(True)
                self.dom_button.set_visible(True)
                self.dalej_button.set_visible(True)

                if not self.players[0].moving:
                    for field in self.game_board.fields:
                        if field.name == str(self.players[0].get_position()):
                            actual_field = field
                if actual_field is not None:
                    if actual_field.name not in fields:
                        self.kup_button.set_visible(False)
                        self.dom_button.set_visible(False)
                        self.dalej_button.set_visible(True)
                    if actual_field.owner is None:
                        self.dom_button.set_visible(False)
                    if actual_field.owner is not None and actual_field.owner != self.players[0]:
                        self.dom_button.set_visible(False)
                    if actual_field.name in fields and self.players[0].money < actual_field.koszt_domu:
                        self.dom_button.set_visible(False)
                    if actual_field.owner is not None and actual_field.owner.color is not self.players[0].color:
                        self.kup_button.set_visible(False)
                        self.dom_button.set_visible(False)
                    if actual_field.owner is not None and actual_field.owner.color is self.players[0].color:
                        self.kup_button.set_visible(False)
                    if actual_field.name in fields and self.players[0].money < actual_field.cena:
                        self.kup_button.set_visible(False)
                    if actual_field.houses == 4:
                        self.dom_button.set_visible(False)

        self.rzut_button.draw(screen)
        self.kup_button.draw(screen)
        self.dom_button.draw(screen)
        self.dalej_button.draw(screen)

        pygame.display.flip()


def game(c):
    system = System()
    system.create_game(c)

    # ============================================== nieskończona pętla gry
    window_open = True
    while window_open:
        screen.blit(gm.BACKGROUND, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window_open = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    window_open = False

        system.draw_game(False, True)

        if system.rzut_button.click() and system.rzut_button_on:
            system.rzut_button_on = False
            system.dice.double_roll()
            system.message.add_message(f"gracz {system.players[0].name} poruszył się o {system.dice.show_turn_value()}")
            for x in range(0, system.dice.show_turn_value()):
                system.players[0].move(1)
                pygame.time.delay(200)
                system.draw_game(False, False)
            system.players[0].moving = False  # informacja ze jest na ostatnim polu
            # pygame.time.delay(1000)

        if system.dom_button.click():
            if system.dom_button.click() and not system.rzut_button_on:
                current_player = system.players[0]
                system.game_board.buy_house(current_player)
                pygame.time.delay(200)

        if system.kup_button.click():
            if system.kup_button.click() and not system.rzut_button_on:
                current_player = system.players[0]
                system.game_board.buy_field(current_player)
                pygame.time.delay(200)

        if system.dalej_button.click() and not system.rzut_button_on:
            system.kup_button.set_visible(False)
            system.dom_button.set_visible(False)
            system.dalej_button.set_visible(False)

            system.rzut_button_on = True
            system.switch_player()

        pygame.display.flip()


def color():
    pygame.time.delay(100)
    window_open = True

    redBtn = Button(screen.get_width() / 2 - gm.REDBTN.get_width() / 2, 180, gm.REDBTN, True)
    blueBtn = Button(screen.get_width() / 2 - gm.BLUEBTN.get_width() / 2, 330, gm.BLUEBTN, True)
    greenBtn = Button(screen.get_width() / 2 - gm.GREENBTN.get_width() / 2, 480, gm.GREENBTN, True)
    purpleBtn = Button(screen.get_width() / 2 - gm.PURPLEBTN.get_width() / 2, 630, gm.PURPLEBTN, True)

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
    play_button = Button(screen.get_width() / 2 - gm.PLAY_BUTTON.get_width() / 2, 230, gm.PLAY_BUTTON, True)
    exit_button = Button(screen.get_width() / 2 - gm.PLAY_BUTTON.get_width() / 2, 480, gm.EXIT_BUTTON, True)

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
