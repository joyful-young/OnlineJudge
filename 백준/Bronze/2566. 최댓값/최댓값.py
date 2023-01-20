# 2차원 배열 받을 리스트
numbers = []

import sys

# 한 줄을 한 리스트로 numbers에 넣기
for _ in range(9):
    numbers.append(list(map(int, sys.stdin.readline().split())))

# 각 줄에서 최댓값을 모은 리스트
max_nums = []

for rows in numbers:
    max_nums.append(max(rows))

# row 최댓값 중 최댓값
max_number = max(max_nums)

# 행 번호 - 1
max_number_row = max_nums.index(max_number)

# 열 번호 - 1
max_number_col = numbers[max_number_row].index(max_number)

print(max_number)
print(max_number_row + 1, max_number_col + 1)