# 1253. 좋다
def search(idx, current_cnt):
    target = numbers[idx]
    left = 0
    right = N - 1
    while left < right:
        if left == idx:
            left += 1
            continue
        if right == idx:
            right -= 1
            continue

        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            current_cnt += 1
            return current_cnt
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return current_cnt

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0

for i in range(N):
    # 합이 numbers[i] 가 되는 경우가 있는지 확인
    result = search(i, result)

print(result)