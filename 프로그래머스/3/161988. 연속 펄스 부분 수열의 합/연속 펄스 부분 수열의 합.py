def solution(sequence):

    # 1 부터 연속펄스 부분 수열을 곱한값 찾기 prefix sum 만들기 
    # maxV - minV 
    # 각각의 리스트에서 max()
    answer = 0
    prefixS = [0]
    for i in range(len(sequence)):
        pulse = 1 if i%2 ==0  else -1
        prefixS.append(prefixS[-1]+pulse*sequence[i])


    return abs(max(prefixS) - min(prefixS))