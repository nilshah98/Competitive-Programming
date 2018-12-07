def what_is_the_time(time_in_mirror):
    time=time_in_mirror.split(':')
    answer=[]
    z=0
    if int(time[1])>0:
        if int(time[0])<=10:
            z=11-int(time[0])
        elif int(time[0])==12:
            z=11
        elif int(time[0])==11:
            z=12
    if int(time[1])==0:
        z=12-int(time[0])
    answer.append(z)
    answer.append(60-int(time[1]))
    return str(answer[0])+':'+str(answer[1])

def what_is_the_time1(time_in_mirror):
    h, m = map(int, time_in_mirror.split(':'))
    return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60), h, m