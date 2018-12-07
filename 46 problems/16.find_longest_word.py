#fina and print longest word Q16
def find_longest_word(phrase):
    lengths=[]
    a=0
    for i in phrase:
        lengths.append(len(i))
    for x in lengths:
        if x>a:
            a=x
    for y in range(len(lengths)):
        if lengths[y]==a:
            return lengths, a, phrase[y]
