import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

nums = list(map(int, input().split()))
nums.sort()
x = nums[0]
y = nums[1]
k = 0
curr = lcm(x,y)

mod = y%x
if mod == 0:
    print("0")
else:
    '''
    we are taking remaining coins here,
    since k will be added to x and y, if we take out x from both
    rem is what essentially remains to divide in x+k
    '''
    rem = y-x
    '''
    Taking all factors, to divide the remaining coins in stack
    '''
    factors = []
    i = 1
    while i*i <= rem:
        if rem%i == 0:
            factors.append(i)
            factors.append(rem//i)
        i += 1
    factors.sort()

    for i in factors:
        '''
        considering i coins in a single stack here,
        so k will essentially be i - x,
        but x can be larger than i, and go in negative,
        so we need to essentially subtract the modulus
        '''
        temp = i - (x%i)

        if lcm(x+temp,y+temp) < curr:
            k = temp
            curr = lcm(x+k,y+k)

    print(k)
'''
Error =>
1. Didn't consider multiples, ie. x y, y = x*z, so the increment should be a*z times to keep mod constant
'''