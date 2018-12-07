n=int(raw_input())
seq=(raw_input())
currfreq=1
maxfreq=1
lastchar=seq[0]
for i in range(1,n):
	if seq[i] == lastchar:
		currfreq+=1
	else:
		currfreq=1
		lastchar=seq[i]
	if maxfreq<currfreq:
		maxfreq=currfreq
if maxfreq<currfreq:
	maxfreq=currfreq
alternating=1
lastchar=seq[0]
for i in range(1,n):
	if seq[i]!=lastchar:
		alternating+=1
		lastchar=seq[i]
# print alternating
if maxfreq==1:
	print min(alternating,n)
elif maxfreq==2:
	if n==2:
		print 2
	elif n==3:
		print 3
	elif n>=4:
		if ("0011" in seq) or ("1100" in seq):
			# print "Yes"
			print min(alternating+2,n)
		elif seq[0]==seq[1] and seq[-1]==seq[-2]:
			print min(alternating+2,n)
		# elif (seq[0]==seq[1]) or (seq[-1]==seq[-2]):
		# 	print alternating+1
		else:
			print min(alternating+2,n)
elif maxfreq>=3:
	print min(alternating+2,n)