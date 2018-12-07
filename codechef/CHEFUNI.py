def removeZero(x):
	while (len(x)>0 and x[-1]==0):
		x.pop()
	return x
t=int(raw_input())
for _ in range(t):
	x,y,z,a,b,c=map(int, raw_input().split())
	planets=[x,y,z]
	planets.sort(reverse=True)
	cost=[[a/1.0,a,1],[b/2.0,b,2],[c/3.0,c,3]]
	cost.sort()
	energy=0
	if cost[0][2]==1:
		energy=sum(planets)*cost[0][1]
	elif cost[0][2]==3:
		planetscopy=planets[:]
		energy+=min(planets)*cost[0][1]
		rem=min(planets)
		planets[0]-=rem
		planets[1]-=rem
		planets[2]-=rem
		planets=removeZero(planets)
		planets.sort(reverse=True)
		if len(planets)==2:
			if cost[1][2]==2:
				energy+=planets[-1]*cost[1][1]
				rem=planets[-1]
				planets[0]-=rem
				planets[1]-=rem
			if cost[1][2]==1:
				energy+=sum(planets)*cost[1][1]
				planets[0]=0
				planets[1]=0
			planets=removeZero(planets)
		if len(planets)==1:
			if c+a<2*b:
				energy+=sum(planets)*a
			else:
				# print planetscopy,planets,energy
				# print min(sum(planets),min(planetscopy))
				energy-=min(sum(planets),min(planetscopy))*c
				energy+=2*min(sum(planets),min(planetscopy))*b
				energy+=(sum(planets)-min(sum(planets),min(planetscopy)))*a
	else:
		# print planets
		if((planets[0]-planets[1])<=planets[2]):
			dif=planets[0]-planets[1]
			energy+=dif*cost[0][1]
			planets[0]-=dif
			planets[2]-=dif
			# print planets,energy
			if(planets[0]>planets[2]):
				dif1=planets[0]-planets[2]
				energy+=dif1*cost[0][1]
				planets[0]-=dif1
				planets[1]-=dif1
			# print planets,energy
			dif2=planets[2]/2
			# print dif2
			energy+=3*dif2*cost[0][1]
			planets[0]-=2*dif2
			planets[1]-=2*dif2
			planets[2]-=2*dif2
			# print planets,energy
			if planets[2]==1:
				if a+b<c:
					energy+=(a+b)
				else:
					energy+=c
		else:
			dif=planets[2]
			energy+=dif*cost[0][1]
			planets[0]-=dif
			planets[2]-=dif
			planets=removeZero(planets)
			planets.sort(reverse=True)
			energy+=planets[1]*b
			energy+=(planets[0]-planets[1])*a
	print energy