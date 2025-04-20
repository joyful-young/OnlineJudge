def solution(my_string, n):
    str_list = [c * n for c in my_string]
    return "".join(str_list)