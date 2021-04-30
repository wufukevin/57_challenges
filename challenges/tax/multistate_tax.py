from utils.convertors import to_lower, to_float, to_state
from utils.questioner import Questioner


def ask_more_questions_by_state(questioner, state):
    questioner.reset()
    state_in_lower = state.lower()
    if state_in_lower == 'wisconsin' or state_in_lower == 'wi':
        questioner.add_question('What county do you live in?', to_lower)


class TaxCalculator:
    def calculate(self, amount, state, county):
        tax_mapping = {
            'Wisconsin,eau claire': 0.05,
            'Wisconsin,dunn': 0.04,
            'Illinos,': 0.08
        }
        sub_total = 0
        tax = tax_mapping.get(','.join([state, '' if county is None else county]), 0)
        if tax > 0:
            sub_total = tax * amount
            print(f'The tax is ${sub_total :.2f}.')
        total_amount = amount + sub_total
        print(f'The total is ${total_amount:.2f}.')


def prepare_questions():
    questioner = Questioner().add_question('What is the order amount?', to_float) \
        .add_question('What state do you live in?', to_state)
    return questioner


if __name__ == '__main__':
    questioner = prepare_questions()
    (amount, state) = questioner.ask()
    ask_more_questions_by_state(questioner, state)
    county, = questioner.ask()
    calculator = TaxCalculator()
    calculator.calculate(amount, state, county)
