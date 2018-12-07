def SieveOfEratosthenes(n):
     
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [1 for i in range(n+1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == 1):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = 2
        p += 1
    return prime
    # Print all prime numbers
k=int(raw_input())
ans=SieveOfEratosthenes(k+1)
if k<3:
    print 1
else:
    print 2
print " ".join(map(str,ans[2:]))