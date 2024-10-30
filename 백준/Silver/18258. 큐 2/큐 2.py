# 백준 18258. 큐2

import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque()

for _ in range(N):
    cmd = sys.stdin.readline().strip()
    if cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    else:
        queue.append(int(cmd.split()[1]))