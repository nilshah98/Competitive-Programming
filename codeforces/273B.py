n,m=map(int, raw_input().split())
maxi=n-m+1
maxiposs=maxi*(maxi-1)/2
remteams=n%m
remteamsval=(n/m) + 1
miniposs=remteams*remteamsval*(remteamsval-1)/2
miniposs+=(m-remteams)*(n/m)*((n/m)-1)/2
print miniposs,maxiposs