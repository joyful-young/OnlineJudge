# 백준 2812. 크게 만들기

N, K = map(int, input().split())
numbers = list(map(int, list(input())))

cnt = 0         # 지운 수 카운트
stack = list()      # 빈 스택

stack.append(numbers[0])    # 첫번째 수 스택에 넣기

for i in range(1, N):       # 두번째 숫자부터 넣는데
    # 스택이 비지 않았고 카운트는 K 이하이고 스택 마지막 수보다 새로 들어올 숫자가 더 크면
    while stack and cnt < K and stack[-1] < numbers[i]:
        stack.pop()     # 마지막 수 빼냄
        cnt += 1        # 빼낸 수 카운트 증가
    stack.append(numbers[i])    # 새로 들어올 수보다 작은 수 빼낼만큼 빼냈으면 숫자 넣기

'''
6 2
989999
답 9999
출력 99999
'''

# 만약 들어오는 숫자가 스택이랑 계속 같은 수여서 카운트가 채워지지 않았으면
while cnt < K:
    stack.pop()
    cnt += 1

print(''.join(list(map(str, stack))))
