#include<bits/stdc++.h>
using namespace std;

void sum(long long time[], long long n, bool flag, long long tsum[]){
	long long total = 0, i;
	if(flag){
		i = 0;
	}
	else{
		i = 1;
		tsum[0] = 0;
	}
	for(i; i<n; i+=2){
		total += time[i+1] - time[i];
		tsum[i] = total;
		if(i+1<n){
			tsum[i+1] = total;
		}
	}
}

void display(long long time[], long long n){
	for(long long i=0;i<n;i++){
		cout << time[i] << ' ';
	}
	cout << '\n';
}

int main(){
	long long n,m,i,max,curr=0;
	cin >> n;
	cin >> m;
	long long time[n+2];
	time[0] = 0;
	for(i=1; i<n+1; i++){
	       cin >> time[i];
	}
	time[n+1] = m;
	long long esum[n+1];
	long long osum[n+1];
	sum(time,n+1,true,esum);
	sum(time,n+1,false,osum);
//	display(esum,n+1);
//	display(osum,n+1);
	max = esum[n];
	for(i=1;i<n+2;i+=2){
		if(time[i]>time[i-1]+1){
			curr = osum[n] - osum[i-1];
			curr += esum[i-1] - 1;
		}
		else if(time[i+1]>time[i]+1){
			curr = osum[n] - osum[i-1] - 1;
			curr += esum[i-1];
		}
		if (curr > max){
			max = curr;
		}
	}
	cout << max <<'\n';
	return 0;
}
