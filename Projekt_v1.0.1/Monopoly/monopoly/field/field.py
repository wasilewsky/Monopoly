class Field:
    def __init__(self, name, pos_x, pos_y, image):
        """
        constructor
        """
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = image

    def field_clicked(self):
        raise Exception("field_clicked() not implemented")

    def field_mouse_on(self):
        raise Exception("field_mouse_on() not implemented")

    def player_on_field_action(self):
        raise Exception("player_on_field_action() not implemented")

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
