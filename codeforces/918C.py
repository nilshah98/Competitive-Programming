msg = input()
poss = 0
for i in range(len(msg)):
    currsum = 0
    unused = []
    j = i
    while j < len(msg):
        if msg[j] == "(":
            j += 1
            if len(unused):
                if unused[-1] > 0:
                    unused[-1] += 1
                else:
                    unused.append(1)
            else:
                unused.append(1)
        elif msg[j] == "?":
            j += 1
            if len(unused):
                if unused[-1] > 0:
                    unused.append(-1)
                else:
                    unused[-1] -= 1
            else:
                unused.append(-1)
        else:
            if len(unused) <= 0:
                break
            else:
                neg = 1
                j += 1
                while j < len(msg) and  msg[j] == ")":
                    neg += 1
                    j += 1



    print(unused)
print(poss)
