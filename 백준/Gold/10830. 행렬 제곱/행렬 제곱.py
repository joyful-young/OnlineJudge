# 백준 10830. 행렬 제곱 - 분할정복
import sys
input = sys.stdin.readline

# 행렬곱을 따로 정의해야겠다
def arr_mul(arr1, arr2, N):     # arr1 * arr2
    tmp_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                tmp_arr[i][j] += ((arr1[i][k] % 1000) * (arr2[k][j] % 1000)) % 1000

            tmp_arr[i][j] %= 1000
    return tmp_arr


def arr_square(arr, B, N):   # arr 라는 N * N 행렬을 B번 제곱
    if B == 1:
        # 1000 이상의 수가 나올 수 있나?
        for i in range(N):
            for j in range(N):
                arr[i][j] %= 1000
        return arr

    if B % 2:   # B가 홀수이면
        # 행렬 B//2 제곱 구해서 그걸 제곱하고 행렬A 한번 더 곱하기
        tmp = arr_square(arr, B // 2, N)
        tmp = arr_mul(tmp, tmp, N)
        return arr_mul(tmp, arr, N)

    # B가 짝수이면
    tmp = arr_square(arr, B // 2, N)
    return arr_mul(tmp, tmp, N)


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = arr_square(arr, B, N)

for ans_row in ans:
    print(*ans_row)