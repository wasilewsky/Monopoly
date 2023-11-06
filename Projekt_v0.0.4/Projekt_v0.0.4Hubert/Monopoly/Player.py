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
            # komunikat przeszedłeś przez start czy coś

    def get_position(self):
        return self.position