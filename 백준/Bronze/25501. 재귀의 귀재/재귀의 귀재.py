# 함수
def recursion(s, l, r):
    global cnt
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        # recursion 다시 호출하면 global 변수 cnt 1 증가
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

# 테스트케이스
T = int(input())

for _ in range(T):
    # isPalindrome 호출하면서 recursion 한 번은 호출
    cnt = 1
    word = input()
    print(isPalindrome(word), cnt)