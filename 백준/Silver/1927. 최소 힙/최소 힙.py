# 백준 1927. 최소 힙

import sys
input = sys.stdin.readline


def enq(item):
    global last
    last += 1       # 마지막 정점 자리 만들기
    heap[last] = item   # 마지막 정점에 저장
    c = last        # 부모와의 비교 위해
    p = c // 2
    while p > 0 and heap[p] > heap[c]:    # 부모가 있으면
        heap[p], heap[c] = heap[c], heap[p]     # 교환
        c = p   # 부모를 자식으로 해서 더 비교
        p = c // 2
    return


def deq():
    global last
    if last == 0:   # 힙이 비어있으면
        print(0)
        return
    else:
        tmp = heap[1]   # 루트 노드에 있는 최솟값 임시 저장
        heap[1] = heap[last]    # 마지막 정점 값을 루트로 이동
        last -= 1               # 마지막 정점 삭제
        p = 1
        c = p * 2       # 왼쪽 자식 번호
        while c <= last:    # 자식이 하나 이상 있으면
            if c + 1 <= last and heap[c] > heap[c + 1]:     # 오른쪽 자식도 있고, 오른쪽 자식의 값이 더 작으면
                c += 1      # 비교 대상을 오른쪽 자식으로
            if heap[p] > heap[c]:   # 자식이 부모보다 작으면
                heap[p], heap[c] = heap[c], heap[p]     # 교환
                p = c   # 자식을 부모로
                c = p * 2   # 왼쪽 자식
            else:
                break
        print(tmp)
        return tmp


N = int(input())

heap = [0] * (N + 1)    # 0에서 N번까지 완전이진트리
last = 0                # 완전이진트리의 마지막 정점 번호

# 음의 정수는 입력으로 주어지지 않음
for _ in range(N):
    x = int(input())

    if x:       # 입력이 자연수이면
        enq(x)      # 삽입
    else:       # 입력이 0이면
        deq()       # 삭제. 배열에서 가장 작은 값 출력, 그 값을 배열에서 제거
        