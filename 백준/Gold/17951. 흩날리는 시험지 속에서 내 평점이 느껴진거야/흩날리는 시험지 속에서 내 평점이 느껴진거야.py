# chat GPT 코드
n, k = map(int, input().split())
scores = list(map(int, input().split()))

left, right = 0, sum(scores)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    total = 0
    
    for i in range(n):
        total += scores[i]
        if total >= mid:
            cnt += 1
            total = 0
    
    if cnt >= k:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
        
print(ans)
