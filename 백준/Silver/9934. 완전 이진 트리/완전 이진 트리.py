def find_mid(s, e, level):
    mid = (s + e) // 2
    # print('s, e', s, e)
    # print('mid', mid)
    ans[level].append(inorder[mid])
    if mid == s or mid == e:
        return
    else:
        find_mid(s, mid - 1, level + 1)
        find_mid(mid + 1, e, level + 1)


K = int(input())

inorder = list(map(int, input().split()))

ans = [[] for _ in range(K)]

find_mid(0, 2 ** K - 1, 0)
# print(ans)
for nodes in ans:
    print(*nodes)