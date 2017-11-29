def divisible_by_three(num):
    if (num % 3 == 0):
        return 'fizz'

def divisible_by_five(num):
    if (num % 5 == 0):
        return 'buzz'

def test_divisible_by_three_or_five(num):
    if (num % 15 == 0):
        return 'fizzbuzz'
