#Codewars Fundamentals IQ test
def iq_test(numbers):
    #your code here
    even=[]
    odd=[]
    numbers= numbers.split()
    for i in numbers:
        z=int(i)
        if z%2 != 0:
            odd.append(numbers.index(i)+1)
        else:
            even.append(numbers.index(i) + 1)
    if len(odd)>len(even):
        return even[0]
    else:
        return odd[0]

#Best Solution
def iq_test_best(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1