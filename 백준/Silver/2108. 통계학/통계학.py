from collections import Counter
import sys


N = int(sys.stdin.readline()) # 배열의 개수
arr = [0] * N
for i in range(N):
    arr[i] = int(sys.stdin.readline())
arr.sort()
num_count = Counter(arr)
most_common_num = num_count.most_common(2)

print((lambda arr : int(round((sum(arr) / len(arr)), 0)))(arr)) # 평균 구하기
print((lambda arr : arr[(len(arr) // 2)])(arr)) # 중간값 구하기
if len(most_common_num) == 1:
    print(most_common_num[0][0])
else :
    if most_common_num[0][1] == most_common_num[1][1]:
        print(most_common_num[1][0])
    else :
        print(most_common_num[0][0])
print((lambda arr : max(arr) - min(arr))(arr))
