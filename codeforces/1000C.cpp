#include<bits/stdc++.h>
using namespace std;

int main(){
	long long n,s,e,i,curr=0,last = 0;
	long long answer[200005]={0}; 
	map<long long, long long>::iterator ptr;
	map<long long, long long> segments;
	cin >> n;
	for(i=0; i<n; i++){
		cin >> s;
		cin >> e;
		segments[s]++;
		segments[e+1]--;
	}

	for(ptr=segments.begin(); ptr!=segments.end(); ptr++){
		answer[curr] += ptr->first - last;
		curr += ptr->second;
		last = ptr->first;
	}


	for(i=1; i<n+1; i++){
		cout << answer[i] <<' ';
	}
	cout << '\n';

	return 0;
}
