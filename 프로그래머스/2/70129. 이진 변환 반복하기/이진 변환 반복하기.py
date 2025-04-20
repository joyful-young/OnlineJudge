def solution(s):
    cnt = 0
    zero_eliminated = 0
    while s != "1":
        ones = s.count("1")
        zero_eliminated += len(s) - ones
        s = to_bin(ones)
        cnt += 1
    return [cnt, zero_eliminated]


def to_bin(number):
    answer = ""
    while number > 0:
        number, r = divmod(number, 2)
        answer = str(r) + answer
    return answer if answer else "0"