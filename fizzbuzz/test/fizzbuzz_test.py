import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import fizzbuzz

def test_divisible_by_three():
    assert (fizzbuzz.divisible_by_three(3) == True)
    assert (fizzbuzz.divisible_by_three(4) == False)

def test_divisible_by_five():
    assert (fizzbuzz.divisible_by_five(5) == True)
    assert (fizzbuzz.divisible_by_five(8) == False)

def test_is_divisible_by():
    assert (fizzbuzz.is_divisible_by(6, 3) == True)
    assert (fizzbuzz.is_divisible_by(17, 9) == False)

def test_generate_fizzbuzz_string_or_number():
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(3) == 'fizz')
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(5) == 'buzz')
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(15) == 'fizzbuzz')
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(21) == 'fizz')
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(35) == 'buzz')
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(60) == 'fizzbuzz')
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(11) == 11)
    assert (fizzbuzz.generate_fizzbuzz_string_or_number(34) == 34)
