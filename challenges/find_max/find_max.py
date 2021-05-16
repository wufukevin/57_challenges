from utils.questioner import AskMode, InfiniteQuestioner


class DuplicatedInputNumberError(Exception):
    pass


class InputDistinctInt:
    def __init__(self):
        self.number_set = set()

    def __call__(self, input_content):
        try:
            input_number = int(input_content)
            if input_number in self.number_set:
                raise DuplicatedInputNumberError()
            self.number_set.add(input_number)
            return input_number
        except DuplicatedInputNumberError as duplicate:
            raise duplicate
        except Exception:
            raise StopIteration


def generate_question(question_count):
    input_distinct_int = InputDistinctInt()
    count = 1
    while count <= question_count:
        yield f'Enter number {count}: ', input_distinct_int, True
        count += 1


class FindMax:
    def find(self, infinite_questioner):
        max_of_the_input = None
        for answer in infinite_questioner.ask(AskMode.OneByOne):
            input_number = int(answer)
            if max_of_the_input is None or max_of_the_input < input_number:
                max_of_the_input = input_number
        return max_of_the_input


def infinite_questions():
    input_distinct_int = InputDistinctInt()
    count = 1
    while True:
        yield f'Enter Number {count}: ', input_distinct_int, True
        count += 1


if __name__ == '__main__':
    infinite_questioner = InfiniteQuestioner().set_question_generator(infinite_questions())
    find_max = FindMax()
    max_of_input = find_max.find(infinite_questioner)
    print(f'The largest number is {max_of_input}.')
