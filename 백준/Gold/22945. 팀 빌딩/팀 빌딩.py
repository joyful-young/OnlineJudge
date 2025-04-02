N = int(input())
developers = list(map(int, input().split()))

small, big = sorted([0, N - 1], key=lambda x: developers[x])
max_v = (N - 2) * developers[small]

while small != big:
    # 능력치가 더 작은 쪽을 옮겨봐야 함
    nxt = small
    if small < big:    # 능력치 낮은 게 더 왼쪽 인덱스. 오른쪽으로
        while nxt < big and developers[small] >= developers[nxt]:
            nxt += 1
    else:              # 능력치 낮은 게 더 오른쪽 인덱스. 왼쪽으로
        while big < nxt and developers[small] >= developers[nxt]:
            nxt -= 1

    # nxt는 big과 같아졌거나 이전 A, B 능력치 최솟값보다 큰 값을 갖거나
    if developers[nxt] <= developers[big]:
        small = nxt
    else:
        small = big
        big = nxt

    max_v = max(max_v, (abs(big - small) - 1) * developers[small])

print(max_v)