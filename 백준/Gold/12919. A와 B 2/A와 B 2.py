# 백준 12919. A와 B 2
# 연산을 통해 만들어진 문자열은
# A로 끝나거나 B로 시작해야 함
# 원본 문자열과 다른데 A로 시작하고 B로 끝나면 그건 못 만드는 것
def check(S, T):
    if len(T) < len(S):
        return 0

    if S == T:
        return 1

    if T[0] == 'A' and T[-1] == 'B':
        return 0

    if T[0] == 'B' and T[-1] != 'A':
        # 맨 앞의 B를 떼고 거꾸로
        return check(S, T[1:][::-1])

    if T[-1] == 'A' and T[0] != 'B':
        # 맨 뒤의 A 떼기
        return check(S, T[:-1])

    if T[0] == 'B' and T[-1] == 'A':
        # 둘 다 해보고 하나라도 되면 되는 것 -> OR 연산
        return check(S, T[1:][::-1]) | check(S, T[:-1])


S = input()
T = input()

print(check(S, T))