# 2138. 전구와 스위치
def count(cnt, bulbs, now_bulbs, obj_bulbs):
    for i in range(1, bulbs):
        if now_bulbs[i - 1] != obj_bulbs[i - 1]:
            cnt += 1
            now_bulbs[i - 1] ^= 1
            now_bulbs[i] ^= 1
            if i + 1 < N:
                now_bulbs[i + 1] ^= 1
    if now_bulbs[bulbs - 1] != obj_bulbs[bulbs - 1]:
        return -1
    else:
        return cnt


N = int(input())
now = list(map(int, input()))
obj = list(map(int, input()))

# 첫번째 안 누름
copied = [now[i] for i in range(N)]
cnt1 = count(0, N, copied, obj)

# 첫번째 누름
cnt2 = 1
now[0] ^= 1
now[1] ^= 1
cnt2 = count(cnt2, N, now, obj)

if cnt1 == -1 and cnt2 == -1:
    print(-1)
elif cnt1 == -1:
    print(cnt2)
elif cnt2 == -1:
    print(cnt1)
else:
    print(min(cnt1, cnt2))