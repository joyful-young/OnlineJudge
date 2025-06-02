def solution(numbers):
    N = len(numbers)
    answer = [0] * N
    for i in range(N):
        if is_binary_tree(numbers[i]):
            answer[i] = 1
    return answer


def is_binary_tree(number):
    b_number = format(number, 'b')
    
    # 이진트리 노드 수
    length = 1
    while length <= len(b_number):
        length *= 2
    length -= 1
    
    # 길이 맞추기
    b_number = "0" * (length - len(b_number)) + b_number
    
    def check(mid, d):
        if d == 0:
            return True
        
        if b_number[mid] == "0":
            if b_number[mid - d] == "1" or b_number[mid + d] == "1":
                return False
        return check(mid - d, d // 2) and check(mid + d, d // 2)
    
    return check(len(b_number) // 2, (length + 1) // 4)

        
    