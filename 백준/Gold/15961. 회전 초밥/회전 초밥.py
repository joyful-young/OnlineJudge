import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
eaten = [0 for _ in range(d + 1)]    # eaten[초밥 종류] = 먹은 개수
eaten[c] += 1    # 쿠폰 사용

dishes = [int(input()) for _ in range(N)]    # 벨트 위 초밥 종류
dishes = dishes + [dishes[i] for i in range(k - 1)]
for sushi in dishes[:k]:
    eaten[sushi] += 1

max_value = sum([0 if eaten[i] == 0 else 1 for i in range(1, d + 1)])
current = max_value    # 먹은 초밥 가짓수

idx = k
while idx < N + k - 1:
    # idx 번 접시 in, (idx - k)번 접시 out
    if eaten[dishes[idx]] == 0:
        current += 1
    
    eaten[dishes[idx]] += 1
    eaten[dishes[idx - k]] -= 1
    
    if eaten[dishes[idx - k]] == 0:
        current -= 1

    max_value = max(max_value, current)
    idx += 1
print(max_value)