# 백준 5430. AC
# R은 순서 뒤집기, D는 첫번째 수 버리기
# 배열 비어있는데 D 사용하면 에러

import sys
from collections import deque

T = int(sys.stdin.readline())
for _ in range(T):
    p = sys.stdin.readline().rstrip()     # 수행할 함수
    n = int(sys.stdin.readline())    # 배열 내 수의 개수
    input_string = sys.stdin.readline().rstrip()
    if input_string == '[]':
        int_lst = deque(list())
    else:
        int_lst = deque(list(map(int, input_string[1:-1].split(','))))

    R = 1   # 뒤집힘 판단
    for cmd in p:
        if cmd == 'R':
            R *= -1

        elif not int_lst:    # D 함수인데 배열이 비어있을 경우
            print('error')
            break               # 에러 출력하고 for문 break

        else:       # D 함수이고 배열이 비지 않았을 경우
            if R == 1:      # 정방향
                int_lst.popleft()   # 왼쪽에서 제거
            else:           # 역방향
                int_lst.pop()       # 오른쪽에서 제거
    else:   # break 없이 for문 다 돌면
        if R == 1:      # 정방향으로 출력
            print(f'[{",".join(list(map(str, list(int_lst))))}]')
        else:           # 역방향으로 출력
            print(f'[{",".join(list(map(str, list(int_lst)))[::-1])}]')