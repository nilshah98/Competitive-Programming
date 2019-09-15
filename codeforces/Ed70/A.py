t = int(input())

for _ in range(t):
    x = input()
    y = input()

    xmsb = -1
    ymsb = -1

    for i in range(len(x)-1,-1,-1):
        if x[i] == "1":
            xmsb = len(x) - i
            break
    
    for i in range(len(y)-1,-1,-1):
        if y[i] == "1":
            ymsb = len(y) - i
            break
    
    if xmsb == 1 and ymsb == 1:
        print(0)
    elif xmsb == 1:
        for i in range(len(x)-2,-1,-1):
            if x[i] == "1":
                xmsb = len(x) - i
                break

        if xmsb < ymsb:
            xmsb = ymsb
            while len(x)-xmsb >= 0:
                if(x[len(x)-xmsb] == "1"):
                    break
                xmsb += 1
            print(xmsb - ymsb)

        else:
            print(xmsb-ymsb)
    else:
        if xmsb < ymsb:
            xmsb = ymsb
            while len(x)-xmsb >= 0:
                if(x[len(x)-xmsb] == "1"):
                    break
                xmsb += 1
            print(xmsb - ymsb)
        else:
            print(xmsb-ymsb)
        