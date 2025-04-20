def solution(x):
    sum_of_numbers = 0
    number = x
    while number > 0:
        number, r = divmod(number, 10)
        sum_of_numbers += r
    return x % sum_of_numbers == 0