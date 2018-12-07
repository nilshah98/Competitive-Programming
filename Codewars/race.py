def race(v1, v2, g):
    if v1>v2: return None
    res = g*3600/(v2-v1)
    return [res/3600,res%3600/60,res%60]