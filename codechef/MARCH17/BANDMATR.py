t=input()
for i in range(int(t)):
    n=input()
    n=int(n)
    one=0
    answer=0
    total=[]
    total.append(n)
    for j in range(n):
        xeny=list(map(int, input().split()))
        one+=sum(xeny)
    for k in range(1,n):
        y=max(total)
        x=2*(n-k)
        total.append(x+y)
    if one==0:
        answer=0
    elif one==n**2:
        answer=n-1
    else:
        for l in range(len(total)):
            if total[l]>=one:
                answer=l
                break
    print(answer)