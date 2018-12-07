def find_even_index(arr):
    x=0
    for i in arr:
        if sum (arr[:x])== sum (arr[x+1:]):
            return x
        x+=1
    else:
        return -1