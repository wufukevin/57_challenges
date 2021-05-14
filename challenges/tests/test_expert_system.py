import unittest
from unittest.mock import patch

from expert_system.expert_system import CheckCarSilentRule, CheckBatteryRule, CheckClickingNoiseRule, ExpertSystem
from utils.convertors import to_yes_no_enum
from utils.questioner import Questioner


class TestExpertSystem(unittest.TestCase):
    @patch('builtins.input')
    def test_next_check_car_silent(self, mock_input):
        mock_input.return_value = 'y'
        rule = CheckCarSilentRule()
        questioner = Questioner().add_question(rule.question, to_yes_no_enum, True)
        answer, = questioner.ask()
        rule.set_answer(answer)
        next_rule = next(rule)
        self.assertIsInstance(next_rule, CheckBatteryRule)
        mock_input.return_value = 'n'
        answer, = questioner.ask()
        rule.set_answer(answer)
        next_rule = next(rule)
        self.assertIsInstance(next_rule, CheckClickingNoiseRule)

    @patch('builtins.input')
    def test_clean_and_try_again(self, mock_input):
        mock_input.side_effect = ['y', 'y']
        expert_system = ExpertSystem()
        rule = CheckCarSilentRule()
        expert_system.set_root_rule(rule)
        answer = expert_system.check_rules()
        self.assertEqual('Clean terminals and try starting again.', answer)


if __name__ == '__main__':
    unittest.main()
