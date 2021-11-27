import unittest
from python_2_0_fizzbuzz import fizzbuzz


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