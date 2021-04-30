import unittest
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    @patch('builtins.input')
    def test_questioner(self, mock_input):
        questioner = Questioner()
        questioner.add_question('Select a measure unit, I)Imperial or M)Metric? ', validator=to_measure_unit,
                                retry=True)
        .add_question('Select the unit of the height, F)Feet or I)Inches? ', validator=to_float, retry=True)
        .add_question('Please input the height in feet: ', validator=to_float, retry=True)
        .add_question('Select the unit of the weight, P)Ponds or S)Stones? ', validator=to_float, retry=True)
        .add_question('Please input the weight in ponds: ', validator=to_float, retry=True)
        mock_input.side_effect = ['I', 'F', '7', 'P', '155']
        questioner.ask()
        self.assertEqual(5, mock_input.call_count)
        mock_input.reset_mock()
        mock_input.side_effect = ['j', 'i', 'F', '7', 'P', '155']
        questioner.ask()
        self.assertEqual(6, mock_input.call_count)


if __name__ == '__main__':
    unittest.main()
