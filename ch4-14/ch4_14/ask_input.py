QUESTIONS = {'4-14': ['What is the order amount?', 'What is the state?']}


def ask_input_of_question(question_number):
    return tuple(input(question) for question in (QUESTIONS[question_number]))
