# 백준 1920 수 찾기

N = int(input())
n_lst = list(map(int, input().split()))

M = int(input())
m_lst = list(map(int, input().split()))

# n_lst에 m_lst의 수가 존재하면 1, 없으면 0
# 이분 탐색 이용을 위해 정렬
n_lst.sort()



# m_lst 숫자 하나씩 찾아봄
for m in m_lst:
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        # 중간 값이 딱 찾는 값
        if n_lst[mid] == m:
            print(1)
            break
        # 찾는 값이 중간의 값보다 작으면 왼쪽을 더 찾아봐야 -> 오른쪽 끝 변경
        elif m < n_lst[mid]:
            right = mid - 1
        # 찾는 값이 중간의 값보다 크면 오른쪽을 더 찾아봐야 -> 왼쪽 끝 변경
        else:
            left = mid + 1
    # while문 다 돌았는데 못찾았으면 없는 것
    else:
        print(0)
