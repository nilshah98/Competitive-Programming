t=input()
for i in range(int(t)):
    x=list(map(int, input().split()))
    a=x[0]
    b=x[1]
    counter_a=0
    counter_b=0
    a_candy=1
    b_candy=2
    while(a>=0):
        a-=a_candy
        a_candy+=2
        counter_a+=1
    while(b>=0):
        b-=b_candy
        b_candy+=2
        counter_b+=1
    if(counter_a>counter_b):
        print("Limak")
    else:
        print("Bob")