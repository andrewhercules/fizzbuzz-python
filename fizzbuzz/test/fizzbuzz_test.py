import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import fizzbuzz

def test_divisible_by_three():
    assert (fizzbuzz.divisible_by_three(3) == 'fizz')