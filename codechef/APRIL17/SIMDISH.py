t=input()
for i in range(int(t)):
	list1=list(map(str, input().split()))
	list2=list(map(str, input().split()))
	length=len(list1)
	counter=0
	for i in list1:
		if i in list2:
			counter+=1
	if counter>=length/2:
		print("similar")
	else:
		print("dissimilar") 