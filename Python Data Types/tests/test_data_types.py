import unittest

from python_2_0_fizzbuzz import fizzbuzz
from python_2_1_len import new_len
from python_2_2_chars_count import chars_count
from python_2_3_distinct_words import distinct_words


class Tests(unittest.TestCase):

    def test_2_0_fizzbuzz(self):
        assert "FizzBuzz" == fizzbuzz(15)
        assert "Fizz" == fizzbuzz(3)
        assert "Buzz" == fizzbuzz(5)
        assert "Buzz" == fizzbuzz(50)
        assert "FizzBuzz" == fizzbuzz(45)
        assert "1" == fizzbuzz(1)
        assert "98" == fizzbuzz(98)
        assert "Fizz" == fizzbuzz(99)
        assert "Buzz" == fizzbuzz(100)
        assert "49" == fizzbuzz(49)

    def test_2_1_len(self):
        assert 1 == new_len("z")
        assert 2 == new_len("12")
        assert 0 == new_len("")
        assert 0 == new_len()
        assert 0 == new_len(None)
        assert 0 == new_len(True)
        assert 0 == new_len(10000)
        assert 100 == new_len("z" * 100)

    def test_2_2_chars_count(self):
        assert {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1} == chars_count(
            'Oh, it is python')

    def test_2_3_distinct_words(self):
        assert ['black', 'green', 'red', 'white'] == distinct_words(['red', 'white', 'black', 'red', 'green', 'black'])
