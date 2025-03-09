# 문제 오류 'idx 보다 크면서'라고 되어 있음
def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1