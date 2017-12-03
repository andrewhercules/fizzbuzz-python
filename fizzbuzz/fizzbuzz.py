def divisible_by_three(num):
    return is_divisible_by(num, 3)

def divisible_by_five(num):
    return is_divisible_by(num, 5)

def is_divisible_by(number, divisor):
    return number % divisor == 0

def generate_fizzbuzz_string_or_number(number):
    output_message = ''
    if (divisible_by_three(number)):
        output_message += 'fizz'
    if (divisible_by_five(number)):
        output_message += 'buzz'
    return output_message or number

def play_fizzbuzz(range_start_point, range_end_point):
    for number in range(range_start_point, range_end_point):
        print(generate_fizzbuzz_string_or_number(number))

play_fizzbuzz(1,100)
