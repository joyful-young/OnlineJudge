# 백준 16434. 드래곤 앤 던전
import sys
input = sys.stdin.readline
N, atk = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

monster = 0
for i in range(N):
    if arr[i][0] == 1:
        monster += arr[i][2]

left = 1
# right = 1e12 * 123456
right = 10 ** 6 * monster
minV = right
while left <= right:
    mid = (left + right) // 2
    cur_hp = mid
    cur_atk = atk
    for t, a, h in arr:
        if t == 1:      # 몬스터   
            need = h // cur_atk            # 필요 공격 횟수
            x = need if h % cur_atk != 0 else need - 1
            tmp_hp = cur_hp - a * x         # 그만큼의 공격 후 용사 생명력
            if tmp_hp <= 0:     # 용사 생명력 모자라면
                left = mid + 1
                break               # for문 break해서 mid 다시 계산
            else:
                cur_hp = tmp_hp
        else:           # 포션
            cur_atk += a
            cur_hp = min(mid, cur_hp + h)
    else:       # 용사가 죽는 일 없이 끝나면 최솟값 찾기 위해 mid 줄여봄
        minV = min(minV, mid)
        right = mid - 1

print(minV)