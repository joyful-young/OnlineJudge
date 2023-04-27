# 백준 7490. 0 만들기
import sys
input = sys.stdin.readline

# 다 해봐?
op_dict = {0: '+', 1: '-', 2: ' '}


def f(i, k):
    if i == k:
        # 일단 식 만들기
        tmp = numbers[0]
        for op_idx in range(N - 1):
            tmp += op[op_idx]
            tmp += numbers[op_idx + 1]

        # 식 계산하기
        calc_tmp = tmp.replace(' ', '')     # 중간 공백 제거
        calc_tmp = calc_tmp.replace('+', ' + ')
        calc_tmp = calc_tmp.replace('-', ' - ')

        calc_tmp_list = calc_tmp.split()

        calc = int(calc_tmp_list[0])
        M = len(calc_tmp_list) // 2
        for i in range(1, M + 1):
            if calc_tmp_list[2 * i - 1] == '+':
                calc += int(calc_tmp_list[2 * i])
            else:
                calc -= int(calc_tmp_list[2 * i])

        if calc == 0:
            ans_lst.append(tmp)

        return

    for j in range(3):
        op[i] = op_dict[j]
        f(i + 1, k)


T = int(input())
for _ in range(T):
    N = int(input())
    op = [0] * (N - 1)      # 결정된 연산자가 들어갈 배열
    numbers = list(map(str, list(range(1, N + 1))))
    ans_lst = []
    f(0, N - 1)

    print(*sorted(ans_lst), sep='\n')
    print()
