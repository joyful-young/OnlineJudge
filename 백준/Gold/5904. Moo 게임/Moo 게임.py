N = int(input())
s = [3]
k = 0
for i in range(1, N):
    s.append(s[i - 1] * 2 + (i + 3))
    if s[i] >= N:
        k = i
        break

idx = N - 1     # N번째 글자의 인덱스


while k > 0:
    if s[k] - s[k - 1] <= idx:
        idx -= s[k] - s[k - 1]
        k -= 1
    elif 0 <= idx < s[k - 1]:
        k -= 1
    else:
        if idx == s[k - 1]:
            print('m')
        else:
            print('o')
        break

    if k == 0 and idx == 0:
        print('m')
    elif k == 0 and idx != 0:
        print('o')