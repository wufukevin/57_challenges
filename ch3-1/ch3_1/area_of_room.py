FEET_TO_METER_RATE = 0.09290304


class RoomArea(object):
    def __init__(self):
        self.unit = 'feet'

    def ask_for_length(self):
        self.length = input("What is the length of the room in feet? ")
        if not self.length.isdigit():
            raise Exception()

    def ask_for_width(self):
        self.width = input("What is the width of the room in feet? ")
        if not self.width.isdigit():
            raise Exception()

    def summary(self):
        self.area = int(self.length) * int(self.width)
        area_in_feet = self.areasInFeet()
        area_in_meters = self.areaInMeter()
        print(
            f"You entered dimensions of {self.length} {self.unit} by {self.width} {self.unit}.\nThe area is\n{area_in_feet} square feet\n{area_in_meters} square meters")

    def ask_for_unit(self):
        self.unit = input('Please choose unit: feet or meter? ')
        if self.unit != 'feet' and self.unit != 'meter':
            raise Exception()

    def areaInMeter(self):
        if self.unit == 'feet':
            return f'{self.area * FEET_TO_METER_RATE:.3f}'
        else:
            return f'{self.area}'

    def areasInFeet(self):
        if self.unit == 'feet':
            return f'{self.area}'
        else:
            return f'{self.area / FEET_TO_METER_RATE:.3f}'
