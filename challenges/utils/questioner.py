class Questioner:
    def __init__(self):
        self.questions = []

    def add_question(self, question, validator=None, retry=False):
        self.questions.append((question, validator, retry))
        return self

    def ask(self):
        answers = []
        for question, validator, retry in self.questions:
            while True:
                try:
                    answer = input(question)
                    if validator is not None:
                        answer = validator(answer)
                    answers.append(answer)
                    break
                except Exception as e:
                    if not retry:
                        raise e
        return tuple(answers)

    def reset(self):
        self.questions.clear()
