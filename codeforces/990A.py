n,m,a,b = map(int, input().split())
rem = n%m
buildcost = (m-rem)*a
destrcost = rem*b

print(min(buildcost,destrcost))