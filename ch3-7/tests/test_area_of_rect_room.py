import unittest
from unittest.mock import patch

from ch3_7.area_of_room import RoomArea


def summary_should_be(mock_print, summary):
    mock_print.assert_called_with(summary)


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.areaOfRoom = RoomArea()

    @patch("builtins.print")
    @patch("builtins.input")
    def test_area_of_room(self, mock_input, mock_print):
        mock_input.return_value = '15'
        self.areaOfRoom.ask_for_length()
        mock_input.return_value = '20'
        self.areaOfRoom.ask_for_width()
        self.areaOfRoom.summary()
        summary_should_be(mock_print, """You entered dimensions of 15 feet by 20 feet.
The area is
300 square feet
27.871 square meters""")

    @patch("builtins.input")
    def test_area_of_room_input_not_numerics(self, mock_input):
        mock_input.return_value = 'a'
        with self.assertRaises(Exception):
            self.areaOfRoom.ask_for_length()
        mock_input.return_value = 'a'
        with self.assertRaises(Exception):
            self.areaOfRoom.ask_for_width()

    @patch("builtins.print")
    @patch("builtins.input")
    def test_select_unit(self, mock_input, mock_print):
        mock_input.return_value = 'meter'
        self.areaOfRoom.ask_for_unit()
        self.unit_should_be(self.areaOfRoom, 'meter')
        mock_input.return_value = '20'
        self.areaOfRoom.ask_for_length()
        mock_input.return_value = '15'
        self.areaOfRoom.ask_for_width()
        self.areaOfRoom.summary()
        summary_should_be(mock_print,
                          f"You entered dimensions of {self.areaOfRoom.length} {self.areaOfRoom.unit} by {self.areaOfRoom.width} {self.areaOfRoom.unit}.\nThe area is\n{self.areaOfRoom.areasInFeet()} square feet\n{self.areaOfRoom.areaInMeter()} square meters")

    def unit_should_be(self, room_area, expected_unit):
        self.assertEqual(expected_unit, room_area.unit)


if __name__ == '__main__':
    unittest.main()
