#include <bits/stdc++.h>
using namespace std;
int main(){
	long long n,i,ans=0;
	cin >> n;
	string size;
	unordered_map<string,long long> prev;
	for(i=0 ;i<n ;i++){
		cin >> size;
		prev[size]++;
	}
	
	for(i=0 ;i<n ;i++){
		cin >> size;
		if (prev[size] != 0){
			prev[size]--;
		}
		else{
			ans ++;
		}
	}

	cout << ans << '\n';
	return 0;
	}
