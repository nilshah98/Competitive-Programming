#include<bits/stdc++.h>
#define ll long long

using namespace std;

int main(){
    ll t,n,k,ans;
    cin>>t;

    for(ll i=0; i<t; i++){
        cin>>n>>k;
        ans = 0;
        
        while(n>0){
            ans += n%k;
            n -= n%k;

            if(n==0){
                cout << ans << "\n";
                break;
            }

            n = n/k;
            ans += 1;
        }
    }
    return 0;
}