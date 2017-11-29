import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import fizzbuzz

def test_divisible_by_three():
    assert (fizzbuzz.divisible_by_three(3) == 'fizz')
    assert (fizzbuzz.divisible_by_three(4) == 4)

def test_divisible_by_five():
    assert (fizzbuzz.divisible_by_five(5) == 'buzz')
    assert (fizzbuzz.divisible_by_five(8) == 8)

def test_divisible_by_three_or_five():
    assert (fizzbuzz.test_divisible_by_three_or_five(15) == 'fizzbuzz')
    assert (fizzbuzz.test_divisible_by_three_or_five(21) == 21)
