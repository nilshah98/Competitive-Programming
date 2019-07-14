n = int(input())
nums = []
neg = 0
pos = 0
negTot = 0
posTot = 0
negInt = 0
posInt = 0
for _ in range(n):
    temp = float(input())
    nums.append(temp)

    if temp > 0:
        pos += 1
        posTot += int(temp)
        if temp%1 == 0:
            posInt += 1
    else:
        neg += 1
        negTot += int(temp)
        if temp%1 == 0:
            negInt += 1
    
diff = posTot + negTot

if diff == 0:
    for i in nums:
        print(int(i))
elif diff > 0:
    for i in nums:
        if i < 0 and i%1 != 0:
            if diff > 0:
                print(int(i)-1)
                diff -= 1
            else:
                print(int(i))
        else:
            print(int(i))
else:
    for i in nums:
        if i > 0 and i%1 != 0:
            if diff < 0:
                print(int(i)+1)
                diff += 1
            else:
                print(int(i))
        else:
            print(int(i))