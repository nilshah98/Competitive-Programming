t=input()
for i in range(int(t)):
    answer=0
    n=input()
    xeny=list(map(int, input().split()))
    xeny.sort()
    y=max(xeny)
    x=min(xeny)
    if y-1 not in xeny:
        xeny.remove(y)
        answer=(y)
    elif x+1 not in xeny:
        xeny.remove(x)
        answer=(x)
    else:
        for a in range(1,int(n)-1):
            if xeny[a]-xeny[a-1]!=1:
                answer=xeny[a-1]
                break
        if answer==0:
            answer=y
    print(answer) 