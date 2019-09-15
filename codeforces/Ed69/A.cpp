#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t;
    cin >> t;

    for(ll i=0; i<t; i++){
        ll n, temp;
        ll max, secMax;
        max = -1;
        secMax = -2;
        
        cin >> n;

        for(ll j=0; j<n; j++){
            cin >> temp;
            if(temp >= max){
                secMax = max;
                max = temp;
            }
            else if(temp >= secMax){
                secMax = temp;
            }
        }

        cout << min(n-2,secMax-1) << endl;
    }
    return 0;
}