def solution(info, edges):
    # info[i]: 0은 양, 1은 늑대
    tree = {i: [] for i in range(len(info))}
    for p, c in edges:
        tree[p].append(c)
        
    answer = 0
    
    def backtrack(now, sheep, wolf, nxt_nodes):
        nonlocal answer
        
        if info[now] == 0:
            sheep += 1
        else:
            wolf += 1
        
        if sheep == wolf:
            return
        
        answer = max(answer, sheep)
        nxt_nodes.update(tree[now])
        nxt_nodes.remove(now)
        for nxt in nxt_nodes:
            backtrack(nxt, sheep, wolf, nxt_nodes)
        nxt_nodes.add(now)
        nxt_nodes.difference_update(tree[now])
    
    backtrack(0, 0, 0, set([0]))

    return answer