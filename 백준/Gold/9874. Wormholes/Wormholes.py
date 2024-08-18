# 9874. Wormholes
def link_wormholes(cnt, is_linked, wormhole_pairs):
    global ans
    if cnt == N // 2:
        # 웜홀 연결 완료
        # cycle 도는지 확인
        if check_cycle(wormhole_pairs):
            ans += 1
        return

    # for i in range(N):
    #     if not is_linked[i]:
    #         is_linked[i] = True
    #         for j in range(i + 1, N):
    #             if not is_linked[j]:
    #                 is_linked[j] = True
    #                 wormhole_pairs[2*cnt] = i    # i, j번 웜홀 연결
    #                 wormhole_pairs[2*cnt + 1] = j
    #                 link_wormholes(cnt + 1, is_linked, wormhole_pairs)
    #                 is_linked[j] = False
    #         is_linked[i] = False
    
    i_idx = -1
    for i in range(N):
        if not is_linked[i]:
            is_linked[i] = True
            wormhole_pairs[2*cnt] = i
            i_idx = i
            break
    
    for j in range(i_idx + 1, N):
        if not is_linked[j]:
            is_linked[j] = True
            wormhole_pairs[2*cnt + 1] = j
            link_wormholes(cnt + 1, is_linked, wormhole_pairs)
            is_linked[j] = False
    is_linked[i] = False
    

def check_cycle(wormhole_pairs):
    adjL = [0 for _ in range(N)]
    for idx in range(0, N, 2):
        adjL[wormhole_pairs[idx]] = wormhole_pairs[idx + 1]
        adjL[wormhole_pairs[idx + 1]] = wormhole_pairs[idx]

    for start in range(N):
        visited = [False for _ in range(N)]
        stack = [start]
        while stack:
            hole = stack.pop()
            linked_hole = adjL[hole]
            if visited[linked_hole]:
                return True
            visited[linked_hole] = True
            next_hole = right_wormhole[linked_hole]
            if next_hole == -1:
                continue
            stack.append(next_hole)
    return False


N = int(input())
wormholes = [tuple(map(int, input().split())) for _ in range(N)]
wormholes.sort()    # x축 기준 정렬
right_wormhole = [-1 for _ in range(N)] # 오른쪽(+x 방향) 웜홀
for i in range(N):
    for j in range(i + 1, N):
        if wormholes[i][1] == wormholes[j][1] and wormholes[i][0] < wormholes[j][0]:
            right_wormhole[i] = j
            break

ans = 0
link_wormholes(0, [False for _ in range(N)], [0 for _ in range(N)])
print(ans)
