def solution(s):
    s_list = list(s.lower())
    s_list[0] = s_list[0].upper()
    for i in range(1, len(s_list)):
        if s_list[i - 1] == " ":
            s_list[i] = s_list[i].upper()
    return "".join(s_list)