def solution(nodes, edges):
    N = len(nodes)
    
    # 트리 나누기
    rep = [i for i in range(N)]
    
    def find(x):
        if rep[x] == x:
            return x
        
        rep[x] = find(rep[x])
        return rep[x]
    
    def union(x, y):
        rep_x, rep_y = find(x), find(y)
        
        if rep_x < rep_y:
            rep[rep_y] = rep_x
        else:
            rep[rep_x] = rep_y
    
    nodes_idx = {nodes[i]: i for i in range(N)} # node 번호: node 인덱스
    edge_cnt = {i: 0 for i in range(N)}         # node 인덱스: 간선 수
    
    for a, b in edges:
        a_idx, b_idx = nodes_idx[a], nodes_idx[b]
        union(a_idx, b_idx)
        edge_cnt[a_idx] += 1
        edge_cnt[b_idx] += 1
        
    forest = {}
    for i in range(N):
        rep_i = find(i)
        if rep_i in forest:
            forest[rep_i].append(i)
        else:
            forest[rep_i] = [i]
    
    answer = [0, 0]     # [홀짝 트리, 역홀짝 트리]
    for tree in forest.values():
        odd = []
        even = []
        for node_idx in tree:
            sum_of_node_num_and_edge_cnt = nodes[node_idx] + edge_cnt[node_idx]
            if sum_of_node_num_and_edge_cnt % 2:
                odd.append(sum_of_node_num_and_edge_cnt)
            else:
                even.append(sum_of_node_num_and_edge_cnt)
        
        if len(tree) == 1:
            if odd:
                answer[1] += 1
            else:
                answer[0] += 1
        elif len(tree) == 2:
            if odd and even:
                answer[0] += 1
                answer[1] += 1
        else:
            if len(odd) == 1:
                answer[1] += 1
            elif len(even) == 1:
                answer[0] += 1
    
    return answer
