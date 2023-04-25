# 백준 1253. 좋다
def binary_search(s, e, target, i, j):
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            if mid != i and mid != j:
                good[mid] = 1
            tmp_l = mid - 1
            tmp_r = mid + 1
            while tmp_l >= 0 and arr[tmp_l] == target:
                if tmp_l != i and tmp_l != j:
                    good[tmp_l] = 1
                tmp_l -= 1

            while tmp_r < N and arr[tmp_r] == target:
                if tmp_r != i and tmp_r != j:
                    good[tmp_r] = 1
                tmp_r += 1

            return
        elif arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1


N = int(input())
arr = list(map(int, input().split()))

arr.sort()

good = [0] * N
# check = []

for i in range(N - 1):
    for j in range(i + 1, N):       # 두 개 조합
        tmp = arr[i] + arr[j]       # 합 구해서 이진탐색을 할까
        binary_search(0, N - 1, tmp, i, j)
        # if tmp not in check:
        #     binary_search(0, N - 1, tmp)
        #     check.append(tmp)

# print(good)
print(sum(good))
'''
3
0 0 1
0 나와야
'''