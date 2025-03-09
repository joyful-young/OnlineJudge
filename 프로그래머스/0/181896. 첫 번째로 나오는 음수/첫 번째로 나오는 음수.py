def solution(num_list):
    for idx in range(len(num_list)):
        if num_list[idx] < 0:
            return idx
    return -1