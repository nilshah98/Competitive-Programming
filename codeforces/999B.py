n = int(input())
encrypt = ( input())

#finding factors here
factors = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        factors.append(i)
        factors.append(n//i)
factors =list( set(factors))
factors.sort()
for i in factors:
    encrypt = encrypt[0:i][::-1] + encrypt[i:]

print(encrypt)
