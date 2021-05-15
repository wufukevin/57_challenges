from collections import defaultdict

from utils.questioner import Questioner


def split_string_into_character_dict(string_content):
    character_dict = defaultdict(int)
    for char in string_content:
        character_dict[char] += 1
    return character_dict


class AnagramChecker:
    def is_anagram(self, first_string, second_string):
        self.first_string = first_string
        self.second_string = second_string
        first_char_set = split_string_into_character_dict(first_string)
        second_char_set = split_string_into_character_dict(second_string)
        if len(first_string) != len(second_string):
            return False

        for char, count in first_char_set.items():
            if char not in second_char_set or second_char_set[char] != count:
                return False
        return True

    def report(self, is_anagram):
        print(
            f'"{self.first_string}" and "{self.second_string}" are {"anagrams." if is_anagram else "not anagrams."}')


def given_questioner():
    questioner = Questioner().add_question(
        "Enter two strings and I'll tell you if they are anagrams:\nEnter the first string:").add_question(
        "Enter the second string:")
    return questioner


if __name__ == '__main__':
    questioner = given_questioner()
    first_string, second_string = questioner.ask()
    checker = AnagramChecker()
    checker.report(checker.is_anagram(first_string, second_string))
