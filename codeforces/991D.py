first = input()
second = input()
n = len(first)

up = 0
dw = 0
poss = 0
for i in range(n):
    if first[i] == "0" and second[i] == "0":
        up += 1
        dw += 1
        if up > dw:
            up -= 2
            dw -= 1
            poss += 1
        elif dw > up:
            dw -= 2
            up -= 1
            poss += 1
    elif first[i] == "0" and second[i] == "X":
        # reset down counter, since X is there, can't place from earlier places for next pieces
        # try to continue on up, since that remains connected
        both = min(up,dw)
        if both >= 3:
            poss += (both//3)*2
            up %= 3
            dw %= 3
        up += 1
        if dw > 1 and up >= 1:
            poss += 1
            up = 1
            dw = 0
        elif dw >= 1 and up > 1:
            poss += 1
            up = min(up-2, 1)
            dw = 0
        else:
            up = 1
            dw = 0
    elif first[i] == "X" and second[i] == "0":
        # reset down counter, since X is there, can't place from earlier places for next pieces
        # try to continue on up, since that remains connected
        both = min(up,dw)
        if both >= 3:
            poss += (both//3)*2
            up %= 3
            dw %= 3
        dw += 1
        if up > 1 and dw >= 1:
            poss += 1
            dw = 1
            up = 0
        elif up >= 1 and dw > 1:
            poss += 1
            dw = min(dw-2, 1)
            up = 0
        else:
            dw = 1
            up = 0
    else:
        both = min(up,dw)
        if both >= 3:
            poss += (both//3)*2
            up %= 3
            dw %= 3
        
        if max(up,dw) > 1 and min(up,dw) >= 1:
            poss += 1

        up = 0
        dw = 0

both = min(up,dw)
if both >= 3:
    poss += (both//3)*2
    up %= 3
    dw %= 3
        
if max(up,dw) > 1 and min(up,dw) >= 1:
    poss += 1


print(poss)




