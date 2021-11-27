import unittest

from python_2_0_fizzbuzz import fizzbuzz
from python_2_10_pretty_table import pretty_mul_table
from python_2_1_len import new_len
from python_2_2_chars_count import chars_count
from python_2_3_distinct_words import distinct_words
from python_2_4_print_lower_5 import print_lower_5
from python_2_5_lists_merge import lists_merge
from python_2_6_divisors import divisors
from python_2_7_sort_dict_by_value import sort_dict_by_value
from python_2_8_dict_unique_values import dict_unique_values
from python_2_9_convert_tuple import convert_tuple


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

    def test_2_4_print_lower_5(self):
        assert "1 2 3" == print_lower_5([11, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_2_5_lists_merge(self):
        assert [1, 2, 3, 5, 8, 13] == lists_merge([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
                                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_2_6_lists_merge(self):
        assert [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60] == divisors(60)

    def test_2_7_sort_dict_by_value(self):
        assert "{'y': 1, 't': 2, 's': 1, 'p': 1, 'o': 2, 'n': 1, 'i': 2, 'h': 2, ',': 1, ' ': 3}" == \
               str(sort_dict_by_value(chars_count('Oh, it is python')))

    def test_2_8_dict_unique_values(self):
        assert ['S005', 'S002', 'S007', 'S001', 'S009'].sort() == dict_unique_values([{"V": "S001"}, {"V": "S002"},
                                                                                      {"VI": "S001"}, {"VI": "S005"},
                                                                                      {"VII": "S005"}, {"V": "S009"},
                                                                                      {"VIII": "S007"}]).sort()

    def test_2_9_convert_tuple(self):
        assert 1234 == convert_tuple((1, 2, 3, 4))

    def test_2_10_pretty_table(self):
        t = pretty_mul_table((2, 4), (3, 7))
        assert \
            '   3   4   5   6   7   \n' + \
            '2  6   8   10  12  14  \n' + \
            '3  9   12  15  18  21  \n' + \
            '4  12  16  20  24  28  \n' == t
