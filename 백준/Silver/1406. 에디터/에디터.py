# 백준 1406 에디터
# 스택으로 풀기 ver.2

import sys

# 커서 기준 왼쪽과 오른쪽 스택
left = list(sys.stdin.readline().strip())
right = []

# 명령어 개수
M = int(sys.stdin.readline())

for _ in range(M):
    cmd = sys.stdin.readline().strip()
    if len(cmd) != 1:        # 명령어 길이가 1이 아니면 P
        left.append(cmd[-1])
    else:
        if cmd == 'L' and left:      # 커서 왼쪽 한 칸. 커서 맨 앞 아니면
            right.append(left.pop())    # 왼쪽 마지막 글자를 오른쪽으로

        elif cmd == 'D' and right:    # 커서 오른쪽 한 칸. 커서 맨 끝 아니면
            left.append(right.pop())    # 오른쪽 첫 글자를 왼쪽으로

        elif cmd == 'B' and left:    # 커서 왼쪽 문자 삭제. 커서 맨 앞 아니면
            left.pop()  # 왼쪽 마지막 글자 제거

# left는 순서대로, right는 거꾸로 읽어주면 됨
ans = ''.join(left) + ''.join(right[::-1])
print(ans)