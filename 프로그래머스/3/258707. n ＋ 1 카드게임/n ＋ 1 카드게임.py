def solution(coin, cards):
    n = len(cards)
    initial_card_set = set(cards[:n // 3])
    m = n // 3
    
    answer = 1
    pending = []
    while coin >= 0 and m < n:
        pending.extend(cards[m:m + 2])
        m += 2
        
        throw_cards = False
        # 갖고 있는 카드 중에서 처리 가능 -> 코인 소모할 필요 없음
        for num in initial_card_set:
            if (n + 1 - num) in initial_card_set:
                initial_card_set.remove(num)
                initial_card_set.remove(n + 1 - num)
                throw_cards = True
                break
        if throw_cards:
            answer += 1
            continue
            
        # 갖고 있는 카드 중 하나 + 새로 뽑은 카드 중 하나 -> 코인 1 소모
        if coin >= 1 and initial_card_set:
            for num in pending:
                if (n + 1 - num) in initial_card_set:
                    pending.remove(num)
                    initial_card_set.remove(n + 1 - num)
                    coin -= 1
                    throw_cards = True
                    break
        if throw_cards:
            answer += 1
            continue
            
        # 새로 뽑은 카드 중 둘 -> 코인 2 소모
        if coin >= 2:
            pending_set = set(pending)
            for num in pending:
                if (n + 1 - num) in pending_set:
                    pending.remove(num)
                    pending.remove(n + 1 - num)
                    coin -= 2
                    throw_cards = True
                    break
        
        if throw_cards:
            answer += 1
        else:
            break
        
    return answer