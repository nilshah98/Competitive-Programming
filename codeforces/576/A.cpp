#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,x,y,temp;
    cin >> n;
    cin >> x;
    cin >> y;

    vector<ll> rains;

    for(ll i=0; i<n; i++){
        cin >> temp;
        rains.push_back(temp);
    }

    bool flag = true;

    for(ll i=0; i<n; i++){
        flag = true;

        for(ll j=i-1; j>=i-x; j--){
            if(j>=0 && rains[j] <= rains[i]){
                flag = false;
                break;
            }
        }

        for(ll j=i+1; j<=i+y; j++){
            if(j<n && rains[j] <= rains[i]){
                flag = false;
                break;
            }
        }

        if(flag){
            cout << i+1;
            break;
        }
    }

    return 0;
}