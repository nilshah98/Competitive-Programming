a,b,c=map(int, raw_input().split())
x,y,z=map(int, raw_input().split())

stepsallowed=a+b+c-x-y-z
if a>x:
	outa=(a-x)/2 + (a-x)%2
	ina=(a-x)%2
else:
	outa=0
	ina=x-a
a=a-2*outa+ina
if b>y:
	outb=(b-y)/2 + (b-y)%2
	inb=(b-y)%2
else:
	outb=0
	inb=y-b
b=b-2*outb+inb
if c>z:
	outc=(c-z)/2 + (c-z)%2
	inc=(c-z)%2
else:
	outc=0
	inc=z-c
c=c-2*outc+inc

# print stepsallowed
# print outa,ina
# print outb,inb
# print outc,inc
equals=0
if a==x:
	equals+=1
if b==y:
	equals+=1
if c==z:
	equals+=1
if equals>=2:
	print "No"
elif outa+outb+outc >stepsallowed:
	print "No"
elif outa+outb+outc==stepsallowed:
	if outa+outb+outc==ina+inb+inc:
		print "Yes"
	else:
		print "No"
elif outa+outb+outc < stepsallowed:
	if a==x:
		outa=stepsallowed-(outb+outc)
		ina=2*outa
	elif b==y:
		outb=stepsallowed-(outa+outc)
		inb=2*outb
	elif c==z:
		outc=stepsallowed-(outa+outb)
		inc=2*outc
	if(outa+outb+outc==stepsallowed):
		if outa+outb+outc==ina+inb+inc:
			print "Yes"
		else:
			print "No"