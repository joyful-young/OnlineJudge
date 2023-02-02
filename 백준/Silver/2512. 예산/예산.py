# 백준 2512 예산
# 정해진 총액 이하에서 가능한 한 최대의 총 예산 배정
# 배정된 예산 중 최댓값 출력

N = int(input())

# 필요 예산 내림차순으로 받기
needs = sorted(list(map(int, input().split())), reverse=True)

M = int(input())

# 모든 요청이 배정될 수 있으면 요청 금액 그대로 배정
if sum(needs) <= M:
    print(max(needs))

# 모든 요청 배정 불가
# 특정 정수 상한액 계산, 그 이상인 예산요청에는 모두 상한액 배정
# 상한액 이하는 요청 금액 그대로
else:
    # 안 받은 지방 수 초기화
    not_received_cnt = N
    while True:
        divided = M // not_received_cnt        # 남은 예산 적당히 골고루 나눠준다 했을 때 이정도

        for i in range(not_received_cnt):
            # 골고루 나눠줄 때 주는 금액 이하로 요구하면 일단 줌
            # 처음 divided 이하의 금액이 나오면 그 지방부터 끝까지 다 줌
            if needs[i] <= divided:
                # 예산 변화
                M -= sum(needs[i:])
                # 준 지방은 빼기
                needs = needs[:i]
                # 안 받은 지방 수 갱신
                not_received_cnt = len(needs)
                break       # for문 break
        # divided보다 작은 값이 없어서 for문이 break되지 않고 다 돌면
        else:
            break               # while문 break
    print(divided)      # 나머지는 divided 만큼 줌

