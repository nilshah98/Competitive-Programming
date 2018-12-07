from fractions import Fraction
import math

def cosp2(x,pow):
	# print x,pow
	if pow==1:
		return x
	else:
		return cosp2((2*(x**2)-1)%mod,pow/2)

def cossum(a,b):
	return ((a*b)%mod - ((( (1-a**2)%mod * (1-b**2)%mod )%mod)**0.5)%mod)%mod

t=int(raw_input())
mod=10**9+7
for _ in range(t):
        l,d,t=map(int, raw_input().split())
        fr=Fraction(d,l)
        p=fr.numerator
        q=fr.denominator
        r=pow(q,mod-2,mod)
        cos=(p*r)%mod
        cospows=[]
        i=0
        while 1<<i <= t:
        	if t&1<<i:
        		# print 1<<i
        		cospows.append(cosp2(cos,1<<i)%mod)
        	i+=1
        ans=cospows[0]
        if len(cospows)>=2:
        	for i in range(1,len(cospows)):
        		ans=cossum(ans,cospows[i])%mod
        # print cospows
        # print math.degrees(math.acos(ans))
        ans=ans*l
        print ans%mod


