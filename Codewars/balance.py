def balance(arr1, arr2):
    x=[]
    y=[]
    for i in set(arr1):
        x.append(arr1.count(i))
    for i in set(arr2):
        y.append(arr2.count(i))
    x.sort()
    y.sort()
    if x==y:
        return True
    else:
        return False
