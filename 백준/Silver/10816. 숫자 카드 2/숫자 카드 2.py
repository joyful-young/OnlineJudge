# 백준 10816. 숫자 카드 2

N = int(input())

cards_dic = {}      # 숫자 카드 수 딕셔너리
for card in list(map(int, input().split())):
    if card in cards_dic:
        cards_dic[card] += 1
    else:
        cards_dic[card] = 1

M = int(input())
num_lst = list(map(int, input().split()))

ans = [0] * M
for i in range(M):
    if num_lst[i] not in cards_dic:
        ans[i] = 0
    else:
        ans[i] = cards_dic[num_lst[i]]

print(*ans)
