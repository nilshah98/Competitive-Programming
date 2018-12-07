#include<bits/stdc++.h>
#define long long ll
using namespace std;

ll sumdig(ll x)
{
	sum=0;
	while(x>0)
	{
		sum+=(x/10);
		x=x/10;
	}
}

int main()
{
	ll n,tot,curr;
	cin>>n;
	tot=0;
	curr=0;
	while(tot!=n)
	{
		if sumdig(n)==10
		{
			tot+=1
		}
		curr+=1
	}
	cout<<curr-1;

	return 0;
}
