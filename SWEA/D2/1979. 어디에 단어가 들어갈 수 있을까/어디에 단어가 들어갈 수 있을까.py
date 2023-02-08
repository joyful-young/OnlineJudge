# SWEA 1979. 어디에 단어가 들어갈 수 있을까

def check(arr, N, K):
    word = '1' * K
    cnt = 0
    one_list = [0] * N
    for i in range(N):
        one_list[i] = arr[i].split('0')     # 0 기준으로 문자열 나눈 리스트
        one_list[i] = [elem for elem in one_list[i] if elem != '']

    for i in range(N):
        for one in one_list[i]:
            if word == one:     # 단어와 같은 길이의 '1' 문자열이 있으면
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    arr = [0] * N
    for i in range(N):
        arr[i] = input().replace(' ', '')       # 한줄씩 문자열로 공백 없애고 받기

    # 세로줄 받기
    arr_col = [''] * N
    for i in range(N):
        for j in range(N):
            arr_col[i] += arr[j][i]

    print(f'#{tc} {check(arr, N, K) + check(arr_col, N, K)}')
