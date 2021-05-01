from utils.convertors import to_language, to_int
from utils.enums import Language
from utils.questioner import Questioner


class Month:
    __month = {
        Language.English: {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December',
        },
        Language.ChineseTraditional: {
            1: '一月',
            2: '二月',
            3: '三月',
            4: '四月',
            5: '五月',
            6: '六月',
            7: '七月',
            8: '八月',
            9: '九月',
            10: '十月',
            11: '十一月',
            12: '十二月',
        }
    }

    def __init__(self, language, month):
        self.language = language
        self.month = month

    def __str__(self):
        return self.__month[self.language][
            self.month] if 1 <= self.month <= 12 else 'unknown'


def prepare_questions():
    questioner = Questioner().add_question('Select the language, 1)English 2)Chines Traditional: ',
                                           to_language).add_question('Please enter the number of the month:',
                                                                     to_int)
    return questioner


if __name__ == '__main__':
    questioner = prepare_questions()
    language, month = questioner.ask()
    print(f'The name of the month is {Month(language, month)}.')
