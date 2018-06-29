def roundoff(n):
    if n%1 >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(input())
grades = list(map(int, input().split()))

average = roundoff(sum(grades)/n)

moves = 0

if average == 5:
    print(0)
else:
    sumogrades = sum(grades)
    grades.sort()
    for i in grades:
        moves += 1
        sumogrades += (5-i)
        average = roundoff(sumogrades/n)
        if average == 5:
            break
    print(moves)


