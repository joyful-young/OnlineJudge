# 1135. 뉴스 전하기

def dfs(employee):
	if not adjL[employee]:
		return 0
	
	duration = []
	for i in adjL[employee]:
		duration.append(dfs(i))
	
	duration.sort(reverse=True)		# 내림차순

	max_time = 0
	for i, time in enumerate(duration):
		max_time = max(max_time, time + i + 1)	# 오래 걸리는 직원한테 먼저 전달
	
	return max_time


N = int(input())
arr = list(map(int, input().split()))
adjL = [[] for _ in range(N)]

for idx, par in enumerate(arr[1:]):
	adjL[par].append(idx + 1)


print(dfs(0))