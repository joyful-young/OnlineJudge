# 백준 1863. 스카이라인 쉬운거
import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
arr = [list(map(int, input().split())) for _ in range(n)] + [[1000000, 0]]

stack = [arr[0][1]]

for i in range(1, n + 1):
    h = arr[i][1]
    if stack[-1] < h:       # 보이는 높이보다 낮은 건물들은 아직 있을 수 있음
        stack.append(h)
    else:
        while stack and stack[-1] > h:      # 보이는 높이가 낮아졌다는 건 그보다 위에 있는 건물 윤곽은 끝난 것
            stack.pop()
            cnt += 1        # 높은 건물 빼서 개수 세기
        if stack and stack[-1] == h:        # 보이는 높이와 같은 건물은 아직 더 이어질 수 있음
            stack.pop()
        stack.append(h)

print(cnt)
