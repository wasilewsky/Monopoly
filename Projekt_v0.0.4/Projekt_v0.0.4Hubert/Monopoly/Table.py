import pygame
from Monopoly.Player import Player


class PlayerTable:
    player1 = Player('p1', None, 1500)
    player2 = Player('p2', None, 1500)
    player3 = Player('p3', None, 1500)
    player4 = Player('p4', None, 1500)
    players = [player1, player2, player3, player4]

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

    def __init__(self, x, y, screen):
        self.pos_x = x
        self.pos_y = y
        self.screen = screen
        self.color = []

    def create_table(self):
        ptable = PlayerTable(self.pos_x, self.pos_y, PlayerTable.players[0].color, PlayerTable.players[0].money,
                             PlayerTable.players[0].name)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 225, self.pos_y, PlayerTable.players[1].color, PlayerTable.players[1].money,
                             PlayerTable.players[1].name)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 450, self.pos_y, PlayerTable.players[2].color, PlayerTable.players[2].money,
                             PlayerTable.players[2].name)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 675, self.pos_y, PlayerTable.players[3].color, PlayerTable.players[3].money,
                             PlayerTable.players[3].name)
        self.color.append(ptable)

    def draw(self):
        for table in self.color:
            table.draw(self.screen)
