n = int(input())
binN = bin(n)
binN = binN[2:]
length = len(binN)

if n == 0:
    print(1)
    print(1)
elif "0" not in binN:
    print(0)
else:
    curr = "0"
    moves = 0
    nums = []
    for i in range(length):
        if binN[i] == curr:
            if curr == "0":
                moves += 1
                nums.append(length - i)
                curr = "1"
            else:
                moves += 3
                nums.append(length - i)
                curr = "0"
    print(moves)
    print(*nums)