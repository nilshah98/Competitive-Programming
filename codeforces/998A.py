n = int(input())
packets = list(map(int, input().split()))

totsum = sum(packets)

greg = []

for i in range(n):
    if totsum%2 and packets[i] < totsum:
        greg.append(i+1)
        break
    elif totsum%2==0 and packets[i]<totsum and packets[i]!=totsum//2:
        greg.append(i+1)
        break

if len(greg)>0:
    print(len(greg))
    print(*greg)

else:
    print(-1)


