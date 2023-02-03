# 백준 2805

# 나무의 수, 가져가려는 나무 길이
N, M = map(int, input().split())

# 나무 높이 오름차순
tree_height = sorted(list(map(int, input().split())))

# 이분탐색
start = 0       # 절단기 최소 높이
end = tree_height[-1]   # 절단기 최대 가능 높이(나무 높이 최댓값)


while start <= end:
    mid = (start + end) // 2
    # 가져갈 나무
    take = 0

    for height in tree_height:
        # 만약 절단기 높이보다 높으면 자른다
        if height > mid:
            take += height - mid

    # for문 다 돌면 가져갈 양 나옴

    # 필요량보다 많이 가져가면 절단기 높이 높여 봄
    if take > M:
        start = mid + 1
    elif take == M:
        print(mid)
        break
    # 필요량보다 적게 가져가면 절단기 높이 낮춰 봄
    else:
        end = mid - 1
else:
    print(end)
