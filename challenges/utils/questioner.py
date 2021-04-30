class Questioner:
    def __init__(self):
        self.questions = []

    def add_question(self, question, convertor=None, retry=False):
        self.questions.append((question, convertor, retry))
        return self

    def ask(self):
        answers = []
        if len(self.questions) == 0:
            return None,
        for question, convertor, retry in self.questions:
            while True:
                try:
                    answer = input(question)
                    if convertor is not None:
                        answer = convertor(answer)
                    answers.append(answer)
                    break
                except Exception as e:
                    if not retry:
                        raise e
        return tuple(answers)

    def reset(self):
        self.questions.clear()
