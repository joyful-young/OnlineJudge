# 백준 2775

# 테스트케이스
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # n호까지면 리스트도 0 포함해서 길이 (n + 1)로 만들면 됨
    # 리스트들을 담을 빈 리스트
    result = []

    # 0층 거주민 수 리스트 추가
    result.append(list(range(n + 1)))
    # 층 수
    floor = 0

    # k층까지의 거주민 수 리스트 만들기
    while floor < k:
        # 새로운 층의 거주민 수
        floor += 1
        # 이전 층(result[-1])의 i호까지[0:i+1] 거주민 수를 합한 값이 i호의 거주민 수
        # 마지막 n호에서 슬라이싱할 때 끝점이 리스트 범위 벗어나지만 시작점이 범위 안에 있으면 에러 안 남 
        new_list = [sum(result[-1][0:i + 1]) for i in range(n + 1)]
        # 새로운 층의 거주민 수 리스트 결과에 추가
        result.append(new_list)

    # 반복이 끝나면 k층 각각에서 n호까지의 거주민 수 리스트가 나옴
    # k층, n호 거주민 수 출력
    print(result[k][n])