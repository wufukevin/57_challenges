from enum import Enum


class AskMode(Enum):
    All = 0,
    OneByOne = 1


def _convert_answer_or_retry(question, convertor, retry):
    while True:
        answer = input(question)
        try:
            if convertor is not None:
                return convertor(answer)
            return answer
        except StopIteration:
            raise
        except Exception as e:
            if not retry:
                raise e


class Questioner:
    def __init__(self):
        self.questions = []

    def add_question(self, question, convertor=None, retry=False):
        self.questions.append((question, convertor, retry))
        return self

    def ask(self, mode=AskMode.All):
        return tuple(
            _convert_answer_or_retry(question, convertor, retry) for question, convertor, retry in
            self.questions) if mode == AskMode.All else self


class NotSupportedError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} is not supported'


class InfiniteQuestioner(Questioner):
    def __init__(self):
        super().__init__()
        self.questions = None
        self._iter = None

    def __iter__(self):
        return self

    def __next__(self):
        question, convertor, retry = next(self._iter)
        return _convert_answer_or_retry(question, convertor, retry)

    def add_question(self, question, convertor=None, retry=False):
        raise NotSupportedError(self.add_question.__name__)

    def set_question_generator(self, question_generator):
        self.questions = question_generator
        self._iter = iter(self.questions)
        return self
