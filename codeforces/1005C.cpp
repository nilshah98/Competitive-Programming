#include<bits/stdc++.h>
using namespace std;
int main(){
	long long n,ans,i,j,sum=0;
	cin >> n;
	ans = n;
	long long elems[n];
	long long mark[n] = {0};
	for(i=0;i<n;i++){
		cin>>elems[i];
	}
	for(i=0;i<n;i++){
		for(j=i+1;j<n;j++){
			sum = elems[i];
			sum += elems[j];
			if(((sum)&(sum-1)) == 0){
				mark[i] = 1;
				mark[j] = 1;
			}
		}
	}

	for(i=0;i<n;i++){
		ans -= mark[i];
	}

	cout << ans<< "\n";

	return 0;
}
