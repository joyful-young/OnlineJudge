def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cached = {}
    
    answer = 0
    for i in range(len(cities)):
        if cities[i] in cached:
            # hit
            answer += 1
            cached[cities[i]] = i    # i번째에 마지막으로 사용됨
        elif len(cached) < cacheSize:
            # miss & 캐시 크기 남음
            answer += 5
            cached[cities[i]] = i
        else:
            # miss & 캐시 교체 필요
            answer += 5
            lru = i
            lru_city = ""
            for city, used in cached.items():
                if used < lru:
                    lru = used
                    lru_city = city
            del cached[lru_city]
            cached[cities[i]] = i
    
    return answer