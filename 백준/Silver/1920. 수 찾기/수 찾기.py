# 백준 1920. 수 찾기

import sys
input = sys.stdin.readline


def binary_search(x):
    left = 0    # 왼쪽 끝 인덱스
    right = N - 1   # 오른쪽 끝 인덱스

    while left <= right:
        mid = (left + right) // 2   # 중간 인덱스
        if x == arr[mid]:   # 찾는 값과 일치하면
            return 1
        elif x < arr[mid]:      # 찾는 값보다 작으면 왼쪽 구간 다시 탐색
            right = mid - 1
        else:                   # 찾는 값보다 크면 오른쪽 구간 다시 탐색
            left = mid + 1
    return 0


N = int(input())

arr = sorted(list(map(int, input().split())))   # 오름차순 정렬

M = int(input())

numbers = list(map(int, input().split()))

for num in numbers:
    print(binary_search(num))