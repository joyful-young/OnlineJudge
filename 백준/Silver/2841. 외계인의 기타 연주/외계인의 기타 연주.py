N, P = map(int, input().split())

stack = [[0] * N for _ in range(7)]     # 1행부터 6행 쓸 것임 - 줄 번호
tops = [-1] * 7

cnt = 0
for _ in range(N):
    n, p = map(int, input().split())        # 줄 번호, 프렛 번호

    if tops[n] == -1 or stack[n][tops[n]] < p:     # 그 줄의 스택이 비었거나, top의 프렛번호보다 높으면
        tops[n] += 1
        stack[n][tops[n]] = p      # push
        cnt += 1                # 누르기만 하면 됨

    elif tops[n] > -1 and stack[n][tops[n]] > p:           # 스택이 비지 않았고 top의 프렛번호보다 낮으면
        while tops[n] != -1 and stack[n][tops[n]] > p:     # 스택이 비거나 top의 프렛번호 이상이 될 때까지
            tops[n] -= 1        # pop시키고
            cnt += 1            # 손 뗀만큼 카운트
        if tops[n] == -1:       # 스택이 빈 거면
            cnt += 1            # 다시 누름
            tops[n] += 1        # 새로 누른 음 push
            stack[n][tops[n]] = p
        elif stack[n][tops[n]] < p:                   # 눌렀던 적 없는 줄이면
            cnt += 1            # 누름
            tops[n] += 1        # 새로 누른 음 push
            stack[n][tops[n]] = p

print(cnt)