def divisible_by_three(num):
    return is_divisible_by(num, 3)

def divisible_by_five(num):
    return is_divisible_by(num, 5)

def divisible_by_three_or_five(num):
    return is_divisible_by(num, 15)

def is_divisible_by(number, divisor):
    return number % divisor == 0

def play_fizzbuzz(number):
    if (divisible_by_three_or_five(number)):
        return 'fizzbuzz'
    elif (divisible_by_three(number)):
        return 'fizz'
    elif (divisible_by_five(number)):
        return 'buzz'
    else:
        return number
