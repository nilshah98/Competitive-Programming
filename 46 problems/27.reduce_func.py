
#Q27
def reduce_func(x,y):
    if x>y:
        return x
    else:
        return y

lst=[1,5,68,9,4,2,8,10]
reduce(reduce_func, lst)
