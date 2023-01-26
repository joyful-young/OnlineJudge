# 백준 18870

# N 입력
N = int(input())

# 좌표 리스트로 받기
numbers = list(map(int, input().split()))

# 좌표 오름차순 정렬
numbers_sorted = sorted(numbers)

# 순서대로 딕셔너리에 넣기
cnt = 0
numbers_dict = {0: numbers_sorted[0]} # 일단 하나 넣어 놓기

# 정렬된 숫자들 하나하나에 대해 반복
for i in range(1, len(numbers_sorted)):
    
    # numbers[i]가 직전에 딕셔너리에 들어간 수와 같으면
    if numbers_sorted[i] == numbers_sorted[i - 1]:
        # 딕셔너리의 같은 키(cnt)에 들어감. 어차피 무시됨. pass
        pass
    # 직전에 딕셔너리에 들어간 수와 다르면(= 더 크면)
    else:
        # cnt를 하나 올리고 딕셔너리에 추가
        cnt = cnt + 1
        numbers_dict[cnt] = numbers_sorted[i]

# 반복 끝나면 작은 숫자부터 인덱스를 키로, 숫자를 값으로 하는 딕셔너리가 나올 것

# value 겹치지 않게 만들었음. 바로 key, value 바꿔도 됨
reverse_dict = dict(map(reversed, numbers_dict.items()))

# 처음에 받은 좌표 리스트로 딕셔너리에서 값 찾아 출력
result = []
for number in numbers:
    result.append(str(reverse_dict.get(number)))

print(' '.join(result))
