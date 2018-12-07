def ranks(a):
    x=a[:]
    a.sort(reverse=True)
    answer=[]
    for i in x:
        answer.append(a.index(i)+1)
    return answer