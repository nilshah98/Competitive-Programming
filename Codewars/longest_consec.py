def longest_consec(strarr, k):
    l1=[]
    if len(strarr)==0 or len(strarr)<k or k<=0:
        return ''
    for i in range(len(strarr)-k+1):
        x=''
        for j in range(k):
            x+=strarr[i+j]
        l1.append(x)
    return reduce(lambda x,y: x if len(x)>len(y) else y, l1)

print longest_consec(["wlwsasphmxx","owiaxujylentrklctozmymu","wpgozvxxiu"], 2)