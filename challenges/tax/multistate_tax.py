from utils.convertors import to_lower


def ask_more_questions_by_state(questioner, state):
    questioner.reset()
    state_in_lower = state.lower()
    if state_in_lower == 'wisconsin' or state_in_lower == 'wi':
        questioner.add_question('What county do you live in?', to_lower)
