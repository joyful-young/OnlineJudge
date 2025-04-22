def solution(phone_book):
    if len(phone_book) == 1:
        return True
    
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if len(phone_book[i - 1]) <= len(phone_book[i]) \
            and phone_book[i - 1] == phone_book[i][:len(phone_book[i - 1])]:
            return False
    
    return True