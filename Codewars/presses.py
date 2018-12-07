def presses(phrase):
    l=[' ','a','d','g','j','m','p','t','w','b','e','h','k','n','q','u','x','0','g','f','i','l','o','r','v','y','s','z','2','3','4','5','6','8','7','9']
    l1=[]
    l2=[]
    for i in phrase:
        l1.append(l.index(i))
    for i in l1:
        if i in range(0,9):
            l2.append(1)
        elif i in range(9,18):
            l2.append(2)
        elif i in range(18,26):
            l2.append(3)
        elif i in range(26,34):
            l2.append(4)
        else:
            l2.append(5)
    return sum(l2)