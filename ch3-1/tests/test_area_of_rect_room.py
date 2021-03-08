import unittest
from unittest.mock import patch

from ch3_1.area_of_room import RoomArea


def summary_should_be(mock_print, summary):
    mock_print.assert_called_with(summary)


class MyTestCase(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.input")
    def test_area_of_room(self, mock_input, mock_print):
        room_area = RoomArea()
        mock_input.return_value = '15'
        room_area.ask_for_length()
        mock_input.return_value = '20'
        room_area.ask_for_width()
        room_area.summary()
        summary_should_be(mock_print, """You entered dimensions of 15 feet by 20 feet.
The area is
300 square feet
27.871 square meters""")

    @patch("builtins.input")
    def test_area_of_room_input_not_numerics(self, mock_input):
        room_area = RoomArea()
        mock_input.return_value = 'a'
        with self.assertRaises(Exception):
            room_area.ask_for_length()
        mock_input.return_value = 'a'
        with self.assertRaises(Exception):
            room_area.ask_for_width()


if __name__ == '__main__':
    unittest.main()
