from collections import deque

def can_convert(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    return cnt == 1


def solution(begin, target, words):
    if begin not in words:
        words.append(begin)
        
    N = len(words)
    graph = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if can_convert(words[i], words[j]):
                graph[i][j] = True
                graph[j][i] = True

    q = deque([N - 1])
    visited = [-1 for _ in range(N)]
    visited[N - 1] = 0
    while q:
        v = q.popleft()
        
        if words[v] == target:
            return visited[v]
        
        for w in range(N):
            if graph[v][w] and visited[w] == -1:
                visited[w] = visited[v] + 1
                q.append(w)
        
    return 0