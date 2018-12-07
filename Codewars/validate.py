def validate(n):
    n=map(int, str(n))
    if len(n)%2==0:
        for i in n[::2]:
            n.remove(i)
            i=2*i
            if i>9:
                i-=9
                n.append(i)
            else:
                n.append(i)
    else:
        for i in n[1::2]:
            n.remove(i)
            i=2*i
            if i>9:
                i-=9
                n.append(i)
            else:
                n.append(i)
    if sum(n)%10==0:
        return True, n
    else:
        return False, n