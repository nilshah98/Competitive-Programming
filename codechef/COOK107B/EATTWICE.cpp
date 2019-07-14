#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t,n,d,v,w;

    cin >> t;
    
    for(ll i=0; i<t; i++){
        cin >> n;
        cin >> d;

        ll dishes[d] = {0};

        for(ll j=0; j<n; j++){
            cin >> w;
            cin >> v;

            if(dishes[w-1] < v){
                dishes[w-1] = v;
            }
        }
        
        sort(dishes, dishes+d);
        cout << dishes[d-1] + dishes[d-2] << endl;
    }
    return 0;
}