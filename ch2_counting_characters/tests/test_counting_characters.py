import unittest


class MyTestCase(unittest.TestCase):
    def test_count_homer(self):
        counter = CharacterCounter()
        counter.ask_input()
        self.assertEqual("Homer has 5 characters.", counter.count_result())


if __name__ == '__main__':
    unittest.main()
