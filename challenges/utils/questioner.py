from enum import Enum, auto
from types import GeneratorType


class AskMode(Enum):
    All = 0,
    OneByOne = 1


def convert_answer_or_retry(question, convertor, retry):
    while True:
        try:
            answer = input(question)
            if convertor is not None:
                return convertor(answer)
            return answer
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
            convert_answer_or_retry(question, convertor, retry) for question, convertor, retry in
            self.questions) if mode == AskMode.All else (
            convert_answer_or_retry(question, convertor, retry) for question, convertor, retry in self.questions)


def _default_question_generator():
    while True:
        yield '', None, False


class NotSupportedError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} is not supported'


class InfiniteQuestioner(Questioner):
    def __init__(self):
        super().__init__()
        self.questions = _default_question_generator()

    def add_question(self, question, convertor=None, retry=False):
        raise NotSupportedError(self.add_question.__name__)

    def set_question_generator(self, question_generator):
        self.questions = question_generator
        return self
