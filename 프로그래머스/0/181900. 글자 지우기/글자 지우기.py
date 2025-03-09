def solution(my_string, indices):
    idx_set = set(indices)
    answer = [my_string[idx] if idx not in idx_set else '' for idx in range(len(my_string))]
    return ''.join(answer)