t = int(input())
for _ in range(t):
    n = input()
    mod1 = 0
    mod2 = 0
    score = 0
    for digit in n:
        digit = int(digit)
        if digit == 6 or digit == 1:
            score += 10
            mod1 = 0
            mod2 = 0
        elif digit%3 == 1:
            if mod2 == 1:

