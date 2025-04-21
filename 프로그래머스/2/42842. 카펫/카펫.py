def solution(brown, yellow):
    """
    2(x + y) - 4 = brown
    (x - 2)(y - 2) = xy - 2(x + y) + 4 = xy - brown = yellow
    """
    sum_of_l = (brown + 4) // 2
    prod_of_l = yellow + brown
    
    answer = []
    for y in range(3, sum_of_l // 2 + 1):
        if y * (sum_of_l - y) == prod_of_l:
            answer = [sum_of_l - y, y]
            break
    return answer