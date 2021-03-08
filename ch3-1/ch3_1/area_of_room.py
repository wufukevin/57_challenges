FEET_TO_METER_RATE = 0.09290304


class RoomArea(object):
    def ask_for_length(self):
        self.length = input("What is the length of the room in feet? ")
        if not self.length.isdigit():
            raise Exception()

    def ask_for_width(self):
        self.width = input("What is the width of the room in feet? ")
        if not self.width.isdigit():
            raise Exception()

    def summary(self):
        area_in_feet = int(self.length) * int(self.width)
        area_in_meters = area_in_feet * FEET_TO_METER_RATE
        print(
            f"You entered dimensions of {self.length} feet by {self.width} feet.\nThe area is\n{area_in_feet} square feet\n{area_in_meters:.3f} square meters")