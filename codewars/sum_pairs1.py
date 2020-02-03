def sum_pairs1(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i], cache
        cache.add(i)