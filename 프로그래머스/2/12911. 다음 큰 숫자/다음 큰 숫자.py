def solution(n):
    ones = count_one(n)
    
    n += 1
    while count_one(n) != ones:
        n += 1
    
    return n

def count_one(number):
    ans = ""
    while number > 0:
        number, r = divmod(number, 2)
        ans = str(r) + ans
    return ans.count("1")