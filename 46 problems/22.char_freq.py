#Q22
def char_freq(phrase):
    char=[]
    freq=[]
    final=[]
    for i in phrase:
        if i not in char:
            char.append(i)
    for i in char:
        a=0
        for j in phrase:
            if i==j:
                a+=1
        freq.append(a)
    for i in char:
        c=[]
        c.append(i)
        c.append(freq[char.index(i)])
        final.append(c)
    d=dict(final)
    return d