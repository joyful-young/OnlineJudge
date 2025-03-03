# 20210. 파일 탐색기
from functools import cmp_to_key
import sys
input = sys.stdin.readline

N = int(input())
arr = [input().rstrip() for _ in range(N)]

def compare_char(c1, c2):
    if c1.lower() != c2.lower():    # 둘이 다른 문자면 알파벳순
        return (c1.lower() > c2.lower()) - (c1.lower() < c2.lower())
    return c1.islower() - c2.islower()


def compare_num_str(s1, s2):
    num1, num2 = s1.lstrip('0'), s2.lstrip('0')

    if not num1:
        num1 = '0'
    if not num2:
        num2 = '0'

    if len(num1) != len(num2):      # 앞의 0을 없애고 남은 숫자가 긴 게 뒤로
        return len(num1) - len(num2)

    if num1 != num2:    # 숫자값이 큰 게 뒤로. 문자열로 비교하면 됨
        return (num1 > num2) - (num1 < num2)

    # 앞에 붙은 0의 개수가 적은 것(전체 길이가 더 긴 게 뒤로)
    return len(s1) - len(s2)


def compare(s1, s2):
    """
    두 문자열 s1, s2 를 비교
    s1이 더 앞에 와야 하면 음수, 더 뒤에 가야 하면 양수를 리턴해야.
    """
    idx1, idx2 = 0, 0
    len1, len2 = len(s1), len(s2)

    while idx1 < len1 and idx2 < len2:
        if s1[idx1].isalpha() and s2[idx2].isalpha():
            tmp = compare_char(s1[idx1], s2[idx2])
            if tmp!= 0:
                return tmp

            idx1 += 1
            idx2 += 1

        elif s1[idx1].isdecimal() and s2[idx2].isdecimal():
            # 숫자 비교
            # 숫자 문자열 범위 확인
            end1, end2 = idx1, idx2
            while end1 < len1 and s1[end1].isdecimal():
                end1 += 1
            while end2 < len2 and s2[end2].isdecimal():
                end2 += 1

            # 숫자가 매우 클 수 있음. 문자열인 상태로 비교
            tmp = compare_num_str(s1[idx1:end1], s2[idx2:end2])
            if tmp != 0:
                return tmp

            idx1, idx2 = end1, end2

        else:
            # c1이 숫자, c2가 문자면 c1이 먼저(음수 반환. F - T)
            # c1이 문자, c2가 숫자면 c2가 먼저(양수 반환. T - F)
            return s1[idx1].isalpha() - s2[idx2].isalpha()

    return len1 - len2

arr.sort(key=cmp_to_key(compare))
print(*arr, sep="\n")