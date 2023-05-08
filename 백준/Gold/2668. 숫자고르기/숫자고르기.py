# 백준 2668. 숫자고르기
import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N + 1)
for i in range(1, N + 1):
    arr[i] = int(input())

check = [0] * (N + 1)   # 사이클 확인 여부
cycle = [0] * (N + 1)   # 사이클 여부
for i in range(1, N + 1):
    if not check[i]:    # 확인 안해봤으면
        tmp_cycle_lst = [i]     # 사이클 가능성이 있는 임시 리스트(경로 기록 리스트)
        tmp = arr[i]            # 다음에 가리키는 숫자

        # 아직 확인 안해본 숫자이고 현재의 경로에 없는 숫자이면
        while not check[tmp] and (tmp not in tmp_cycle_lst):
            tmp_cycle_lst.append(tmp)   # 경로 기록
            tmp = arr[tmp]      # 다음에 가리키는 숫자

        if check[tmp]:  # 이미 확인 끝난 숫자가 나왔으면 경로에 기록된 숫자들은 사이클 못 이루는 것
            for num in tmp_cycle_lst:
                check[num] = 1      # 확인 완료

        else:           # tmp in tmp_cycle_lst -> 사이클 존재
            cycle_start = tmp_cycle_lst.index(tmp)      # 사이클 시작 인덱스
            for num in tmp_cycle_lst[:cycle_start]:     # 사이클을 이루지 못하는 부분
                check[num] = 1      # 확인 완료
            for num in tmp_cycle_lst[cycle_start:]:     # 사이클 부분
                check[num] = 1
                cycle[num] = 1      # 사이클

print(sum(cycle))
# print(cycle)
for i in range(1, N + 1):
    if cycle[i]:
        print(i)
        