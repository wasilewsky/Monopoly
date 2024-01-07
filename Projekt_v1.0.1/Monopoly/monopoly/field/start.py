from .field import Field


class Start(Field):
    """
    Representation START field
    """
    def __init__(self, pos_x, pos_y, image):
        super().__init__('start', pos_x, pos_y, image)

    def field_clicked(self):
        pass

    def field_mouse_on(self):
        pass

    def player_on_field_action(self):
        pass
