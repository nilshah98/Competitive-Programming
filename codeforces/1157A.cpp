#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	ll num, answer=0;
	cin >> num;

	if(num > 9){
		answer = 1;
	}

	while(num>9){
	answer += 9 - (num%10);
	num = num/10;
	}
	answer += 9;
	cout << answer;	
	return 0;
}
