def sum_pairs(ints, s):
    minimum=0
    maximum=0
    if s-max(ints)<=min(ints):
        minimum=s-max(ints)
    else:
        minimum=min(ints)
    if max(ints)>=s-min(ints):
        maximum=max(ints)
    else:
        maximum=s-min(ints)
    seen=range(minimum,maximum+2)
    seen.remove(1)
    for i in range(0,len(ints)):
        if seen[s-ints[i]]==True :
            return [s-ints[i],ints[i]]
        else:
            seen[ints[i]]=True
    return None