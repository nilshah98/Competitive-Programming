n,m = map(int, input().split())

chests = list(map(int, input().split()))
keys = list(map(int, input().split()))

oddc = 0
evenc = 0
for i in chests:
    if i%2:
        oddc += 1
    else:
        evenc += 1


oddk = 0
evenk = 0
for i in keys:
    if i%2:
        oddk += 1
    else:
        evenk += 1

print(min(oddc,evenk) + min(evenc,oddk))