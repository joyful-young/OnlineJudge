def solution(numbers):
    N = len(numbers)
    answer = [-1 for _ in range(N)]
    stack = [0]
    
    for i in range(1, N):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
            
    return answer