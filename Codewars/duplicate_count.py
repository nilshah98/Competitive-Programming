def duplicate_count(text):
    x=[]
    for i in text.lower():
        if text.lower().count(i)>1 and i not in x:
            x.append(i)
    return len(x)