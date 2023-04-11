# 백준 17609. 회문
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    string = input().rstrip()
    left = 0            # 왼쪽 글자 인덱스
    right = len(string) - 1     # 오른쪽 글자 인덱스

    ans = 0
    delete = 1      # 삭제 가능 횟수
    flag = False        # 답이 나왔는가
    while left <= right:
        if string[left] == string[right]:       # 두 글자 같으면 양쪽 다 자리 옮겨 비교
            left += 1
            right -= 1
        else:                                   # 두 글자 다르면
            tmp_left, tmp_right = left, right       # 일단 그 지점들 임시저장

            left += 1                           # 왼쪽 글자 제거하고 확인
            ans = 1         # 유사회문인가
            while left <= right:
                if string[left] == string[right]:
                    left += 1
                    right -= 1
                else:
                    ans = 2     # 왼쪽은 아님
                    break

            if ans == 1:
                print(ans)
                flag = True
                break

            ans = 1
            left = tmp_left
            right = tmp_right - 1               # 오른쪽 글자 제거하고 확인
            while left <= right:
                if string[left] == string[right]:
                    left += 1
                    right -= 1
                else:
                    ans = 2         # 여기도 아니면 회문 아님
                    break

            print(ans)
            flag = True
            break

    if not flag:
        print(ans)