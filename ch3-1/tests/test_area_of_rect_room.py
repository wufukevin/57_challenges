import unittest
from unittest.mock import patch


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
        mock_print.assert_called_with("""
You entered dimensions of 15 feet by 20 feet.
The area is
300 square feet
27.871 square meters
""")


if __name__ == '__main__':
    unittest.main()
