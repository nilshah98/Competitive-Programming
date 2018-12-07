t=input()
for i in range(int(t)):
    x=list(map(int, input().split()))
    lngth=x[0]
    k=x[1]
    singlesum=0
    multisum=0
    count_a=0
    count_b=0
    seq=list(input())
    for i in range(lngth):
    	if seq[i]=='a':
    		count_a+=1
    	if seq[i]=='b':
    		singlesum+=count_a
    		count_b+=1
    multisum=((k-1)*(k)*count_a*count_b)//2
    singlesum=singlesum*k
    print((singlesum+multisum)) 