words=["VAMPED", "VALVED", "PALMED"]
def longest_word(letters):
    b=[]
    answer=[]
    finale=[]
    for i in words:
       b.append(len([item for item in i if item not in letters]))
    for i in range(len(b)):
        if b[i]==0:
            answer.append(words[i])
    for i in answer:
        c=len(max(answer))
        if len(i)==c:
            finale.append(i)
    return sorted(finale)
#print longest_word("DVAVPALEM")