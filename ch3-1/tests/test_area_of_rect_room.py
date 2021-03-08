import unittest
from unittest.mock import patch

FEET_TO_METER_RATE = 0.09290304


class RoomArea(object):
    def ask_for_length(self):
        self.length = input("What is the length of the room in feet? ")

    def ask_for_width(self):
        self.width = input("What is the width of the room in feet? ")

    def summary(self):
        area_in_feet = int(self.length) * int(self.width)
        area_in_meters = area_in_feet * FEET_TO_METER_RATE
        print(
            f"You entered dimensions of {self.length} feet by {self.width} feet.\nThe area is\n{area_in_feet} square feet\n{area_in_meters:.3f} square meters")


class MyTestCase(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input")
    def test_area_of_room(self, mock_input, mock_print):
        room_area = RoomArea()
        mock_input.return_value = 15
        room_area.ask_for_length()
        mock_input.return_value = 20
        room_area.ask_for_width()
        room_area.summary()
        mock_print.assert_called_with("""You entered dimensions of 15 feet by 20 feet.
The area is
300 square feet
27.871 square meters""")


if __name__ == '__main__':
    unittest.main()
