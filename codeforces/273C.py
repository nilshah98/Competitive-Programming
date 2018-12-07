def removeZero(x):
	while (len(x)>0 and x[-1]==0):
		x.pop()
	return x
baloons=list(map(int, raw_input().split()))
totsum=sum(baloons)
baloons.sort(reverse=True)
baloons=removeZero(baloons)
if len(baloons)==3:
	dif=(baloons[0]-baloons[1])/2
	if( dif <= baloons[2]):
		baloons[0]-=2*dif
		baloons[2]-=dif
	else:
		baloons[0]-=2*baloons[2]
		baloons[2]-=baloons[2]
	baloons=removeZero(baloons)
if len(baloons)==3:
	dif=min(baloons)
	baloons[0]-=dif
	baloons[1]-=dif
	baloons[2]-=dif
	baloons=removeZero(baloons)
baloons.sort(reverse=True)
if len(baloons)==2:
	if(baloons[0]>=2*baloons[1]):
		baloons[0]-=2*baloons[1]
		baloons[1]-=baloons[1]
	else:
		dif=(baloons[0]-baloons[1])/2
		baloons[0]-=2*dif
		baloons[1]-=dif
	baloons=removeZero(baloons)
if len(baloons)==2:
	baloons[0]=baloons[0]%3
	baloons[1]=baloons[1]%3
	baloons=removeZero(baloons)
baloons=removeZero(baloons)
rem=0
if len(baloons)==0:
	rem=0
elif len(baloons)==1:
	rem=baloons[0]
else:
	rem=sum(baloons)%3
print (totsum-rem)/3