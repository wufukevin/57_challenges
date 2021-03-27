import enum
from math import ceil, pi


class Painter(object):
    def __init__(self):
        self.width = None
        self.length = None
        self.radius = None

    def ask_for_input(self):
        self.length = int(input('Please input length: '))
        self.width = int(input('Please input width: '))

    def area_to_paint(self):
        self.area = self.width * self.length

    def calculate_gallons(self):
        self.area_to_paint()
        number_of_gallons = ceil(self.area / PAINTABLE_AREA_IN_FEET_PER_GALLON)
        print(
            f'You will need to purchase {number_of_gallons} gallons of paint to cover {self.area} square feet.')


PAINTABLE_AREA_IN_FEET_PER_GALLON = 350


def get_painter(chosen_painter):
    if chosen_painter == PaintMode.Rectangle:
        return Painter()
    elif chosen_painter == PaintMode.Round:
        return RoundPainter()
    else:
        return LShaprePainter()


def ask_for_painter():
    choice = input('Please choose painter:\n1. Rectangle\n2. Round\n3. L Shape\n')
    valid_choices = ['1', '2', '3']
    if choice not in valid_choices:
        raise Exception()
    return PaintMode(int(choice))


class PaintMode(enum.Enum):
    Rectangle = 1
    Round = 2
    LShape = 3


class LShaprePainter(Painter):
    def ask_for_input(self):
        self.first_length = int(input('Please input first length: '))
        self.first_width = int(input('Please input first width: '))
        self.second_length = int(input('Please input second length: '))
        self.second_width = int(input('Please input second width: '))

    def area_to_paint(self):
        self.area = int(self.first_width * self.first_length + self.second_width * self.second_length)


class RoundPainter(Painter):
    def ask_for_input(self):
        self.radius = int(input('Please input the radius of the round room: '))

    def area_to_paint(self):
        self.area = int(pow(self.radius, 2) * pi)


if __name__ == '__main__':
    painter = get_painter(ask_for_painter())
    painter.ask_for_input()
    painter.calculate_gallons()
