
#filter long words Q17
def filter_long_words(phrase,b):
    lengths = []
    z=[]
    for i in phrase:
        lengths.append(len(i))
    for i, j in enumerate(lengths):
        if j>=b:
            z.append(i)
    for i in z:
        print phrase[i]
