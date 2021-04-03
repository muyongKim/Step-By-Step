# 캐시 2018 kakao blind recruitment 2021/04/03
# Input
cacheSize = 0
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

def solution(cacheSize, cities):
    cache = []
    runtime = 0

    cities = [city.lower() for city in cities]

    for city in cities:
        # Miss
        if city not in cache:
            runtime += 5
            if len(cache) >= cacheSize and cacheSize:
                cache.pop(0)
                cache.append(city)
            elif cacheSize == 0:
                continue
            else:
                cache.append(city)
        # Hit
        else:
            runtime += 1
            cache.pop(cache.index(city))
            cache.append(city)
    return runtime

print(solution(cacheSize, cities))