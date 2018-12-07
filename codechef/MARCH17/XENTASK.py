t=input()
for i in range(int(t)):
    n=input()
    xeny=list(map(int, input().split()))
    yana=list(map(int, input().split()))
    x=0
    y=0
    for j in range(int(n)):
        if j%2==0:
            x+=xeny[j]
        else:
            x+=yana[j]
    for j in range(int(n)):
        if j%2==0:
            y+=yana[j]
        else:
            y+=xeny[j]
    if y>x:
        print(x)
    else:
        print(y)