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
        self.question_iterators = []

    def add_question(self, question, convertor=None, retry=False):
        question_iterator = SimpleQuestionIterator().add_question(question, convertor, retry)
        self.question_iterators.append(question_iterator)
        return self

    def ask(self, mode=AskMode.All):
        if mode == AskMode.All:
            answers = []
            for question_iterator in self.question_iterators:
                for question, convertor, retry in question_iterator:
                    answers.append(_convert_answer_or_retry(question, convertor, retry))
            return tuple(answers)
        return self

    def __iter__(self):
        self._current_iterator_index = 0
        return self

    def __next__(self):
        if len(self.question_iterators) == 0:
            raise StopIteration
        try:
            question, convertor, retry = next(self.question_iterators[self._current_iterator_index])
            return _convert_answer_or_retry(question, convertor, retry)
        except StopIteration:
            self._current_iterator_index += 1
        finally:
            if self._current_iterator_index >= len(self.question_iterators):
                raise StopIteration

    def add_question_iterator(self, iterator):
        self.question_iterators.append(iterator)
        return self


class NotSupportedError(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} is not supported'


class QuestionIterator:
    def __init__(self):
        self._current_question_index = 0

    def __iter__(self):
        self._current_question_index = 0
        return self

    def __next__(self):
        raise StopIteration


class SimpleQuestionIterator(QuestionIterator):
    def __init__(self):
        super().__init__()
        self.questions = []

    def __next__(self):
        if self._current_question_index >= len(self.questions):
            raise StopIteration
        question = self.questions[self._current_question_index]
        self._current_question_index += 1
        return question

    def add_question(self, question, convertor, retry):
        self.questions.append((question, convertor, retry))
        return self
