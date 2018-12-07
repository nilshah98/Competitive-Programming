def find_nb(m):
    answer=0
    n=1
    while m>answer:
        answer+=n**3
        n+=1
    if m==answer:
        return n-1
    elif m<answer:
        return -1