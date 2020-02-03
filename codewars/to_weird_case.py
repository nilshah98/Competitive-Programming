def to_weird_case(string):
    answer=''
    for x in string.split( ):
        for i in range(len(x)):
            if (i+1)%2==0:
                answer+=x[i]
            else:
                answer+=x[i].upper()
        answer+=' '
    return answer