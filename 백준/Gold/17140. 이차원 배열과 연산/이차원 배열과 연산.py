import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
R -= 1
C -= 1
A = [list(map(int, input().split())) for _ in range(3)]

def change_r_c(arr):
    return list(zip(*arr))


def r_sort(arr):
    rows = len(arr)
    max_length = 0
    for i in range(rows):
        number_dict = {}
        for num in arr[i]:
            if num == 0:
                continue
            if num in number_dict:
                number_dict[num] += 1
            else:
                number_dict[num] = 1
        pair_list = [(k, v) for k, v in number_dict.items()]
        pair_list.sort(key = lambda x: (x[1], x[0]))
        arr[i] = [n for pair in pair_list for n in pair]
        max_length = max(max_length, len(arr[i]))

    
    for i in range(rows):
        if len(arr) > 100:
            arr[i] = arr[i][:100]
        elif len(arr[i]) < max_length:
            arr[i] += [0] * (max_length - len(arr[i]))
    return arr

def apply_operation():
    if len(A) >= len(A[0]):
        return r_sort(A)
    else:
        transposed = [list(row) for row in zip(*A)]
        return [list(row) for row in zip(*r_sort(transposed))]
T = 0
while T <= 100 and not (R < len(A) and C < len(A[0]) and A[R][C] == K):    
    T += 1
    A = apply_operation()

if T > 100:
    print(-1)
else:
    print(T)