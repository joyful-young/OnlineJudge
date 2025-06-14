from collections import defaultdict


def solution(enroll, referral, seller, amount):
    organization = {enroll[i]: referral[i] for i in range(len(enroll))}
    
    answer = defaultdict(int)
    for i in range(len(seller)):
        s = seller[i]
        charge = amount[i] * 100
        p = charge // 10
        answer[s] += charge - p
        
        while p > 0:
            if organization[s] == "-":
                break
            
            s = organization[s]
            temp = p // 10
            answer[s] += p - temp
            p = temp
        
    return [answer[s] for s in enroll]