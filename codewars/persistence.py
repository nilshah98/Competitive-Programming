def persistence(n):
    x=0
    while n>9:
        n=reduce(lambda x,y: x*y, map(int, str(n)))
        x+=1
    return x