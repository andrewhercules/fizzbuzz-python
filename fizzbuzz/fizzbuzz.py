def divisible_by_three(num):
    if (num % 3 == 0):
        return 'fizz'
    else:
        return num

def divisible_by_five(num):
    if (num % 5 == 0):
        return 'buzz'
    else:
        return num

def divisible_by_three_or_five(num):
    if (num % 15 == 0):
        return 'fizzbuzz'
    else:
        return num
