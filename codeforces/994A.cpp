#include<bits/stdc++.h>
using namespace std;

int main(){
	long long n,f,i,fnum;
	cin >> n;
	cin >> f;
	long long seq[n];
	unordered_set<long long> finger;
	unordered_set<long long>::iterator ptr;

	for(i=0;i<n;i++){
		cin >> seq[i];
	}

	for(i=0;i<f;i++){
		cin >> fnum;
		finger.insert(fnum);
	}

	for(i=0;i<n;i++){
		ptr = finger.find(seq[i]);
		if(ptr != finger.end()){
			cout << seq[i] <<' ';
		}
	}
	cout << '\n';
	return 0;
}
