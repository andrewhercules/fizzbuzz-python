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

def test_divisible_by_three_or_five():
    assert (fizzbuzz.divisible_by_three_or_five(15) == True)
    assert (fizzbuzz.divisible_by_three_or_five(21) == False)

def test_is_divisible_by():
    assert (fizzbuzz.is_divisible_by(6, 3) == True)
    assert (fizzbuzz.is_divisible_by(17, 9) == False)

def test_play_fizzbuzz():
    assert (fizzbuzz.play_fizzbuzz(3) == 'fizz')
    assert (fizzbuzz.play_fizzbuzz(5) == 'buzz')
    assert (fizzbuzz.play_fizzbuzz(15) == 'fizzbuzz')
    assert (fizzbuzz.play_fizzbuzz(21) == 'fizz')
    assert (fizzbuzz.play_fizzbuzz(35) == 'buzz')
    assert (fizzbuzz.play_fizzbuzz(60) == 'fizzbuzz')
    assert (fizzbuzz.play_fizzbuzz(11) == 11)
    assert (fizzbuzz.play_fizzbuzz(34) == 34)
