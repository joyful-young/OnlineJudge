def solution(want, number, discount):
    # 제품 종류
    N = len(want)
    goal = {i: number[i] for i in range(N)}
    labels = {want[i]: i for i in range(N)}
    ten_days = {i: 0 for i in range(N)}
    
    for product in discount[:10]:
        if product not in labels:
            continue
        
        label = labels[product]
        ten_days[label] += 1
    
    answer = 0 if ten_days != goal else 1
    if len(discount) == 10:
        return answer
    
    for i in range(10, len(discount)):
        if discount[i - 10] in labels:
            ten_days[labels[discount[i - 10]]] -= 1
            
        if discount[i] in labels:
            ten_days[labels[discount[i]]] += 1
            
        if ten_days == goal:
            answer += 1
    
    return answer