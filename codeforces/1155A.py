n = int(input())
string = input()

curr = string[0]
flag = True

for i in range(1,n):
    if string[i] < curr:
        flag = False
        print("YES")
        print(i,i+1)
        break
    else:
        curr = string[i]

if flag:
    print("NO")