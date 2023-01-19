# 두 수 입력
A, B = input().split()

# 상수가 읽는 수
sang_A = int(A[::-1])
sang_B = int(B[::-1])

# 상수가 생각하는 최댓값 출력
print(max([sang_A, sang_B]))