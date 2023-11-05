import pygame
from Monopoly.Player import Player

player = [Player("TY", 1500), Player("SI1", 1500), Player("SI2", 1500), Player("SI3", 1500)]


class PlayerTable(Player):
    def __init__(self, x, y, color, money):
        super().__init__(color, money)
        self.pos_x = x
        self.pos_y = y

    def draw(self, screen):
        # for x in player:
        colortable = (255, 255, 255)
        if hasattr(self, 'color'):
            if self.color == "TY":
                colortable = (255, 0, 0)
            elif self.color == "SI1":
                colortable = (0, 255, 0)
            elif self.color == "SI2":
                colortable = (0, 0, 255)
            elif self.color == "SI3":
                colortable = (255, 255, 0)
            pygame.draw.rect(screen, (255, 255, 255), (self.pos_x, self.pos_y, 210, 117), 0)
            pygame.draw.rect(screen, colortable, (self.pos_x, self.pos_y, 210, 46), 0)
            pygame.draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, 210, 46), 2)
            pygame.draw.rect(screen, (0, 0, 0), (self.pos_x, self.pos_y, 210, 117), 2)
            text = pygame.font.Font.render(pygame.font.SysFont(None, 75), f"{self.color}", True, (0, 0, 0))
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
        ptable = PlayerTable(self.pos_x, self.pos_y, player[0].color, player[0].money)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 225, self.pos_y, player[1].color, player[1].money)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 450, self.pos_y, player[2].color, player[2].money)
        self.color.append(ptable)

        ptable = PlayerTable(self.pos_x + 675, self.pos_y, player[3].color, player[3].money)
        self.color.append(ptable)

    def draw(self):
        for table in self.color:
            table.draw(self.screen)
