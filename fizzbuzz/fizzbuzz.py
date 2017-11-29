def divisible_by_three(num):
    if (is_divisible_by(num, 3)):
        return 'fizz'
    else:
        return num

def divisible_by_five(num):
    if (is_divisible_by(num, 5)):
        return 'buzz'
    else:
        return num

def divisible_by_three_or_five(num):
    if (is_divisible_by(num, 15)):
        return 'fizzbuzz'
    else:
        return num

def is_divisible_by(number, divisor):
    return number % divisor == 0
