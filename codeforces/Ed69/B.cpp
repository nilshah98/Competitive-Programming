#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,temp,max,index;

    vector<ll> vals;

    bool dup = false;
    max = -1;

    cin >> n;
    for(ll i=0; i<n; i++){
        cin >> temp;

        vals.push_back(temp);

        if(temp > max){
            max = temp;
            index = i;
            dup = false;
        }else if(temp == max){
            dup = true;
        }
    }

    if(dup){
        cout << "NO" << endl;
    }else{
        // Left traverse
        for(ll i=index-1; i>=0; i--){
            if(vals[i] >= vals[i+1]){
                dup = true;
                break;
            }
        }

        // Right traverse
        for(ll i=index+1; i<n; i++){
            if(vals[i] >= vals[i-1]){
                dup = true;
                break;
            }
        }

        if(dup){
            cout << "NO" << endl;
        }else{
            cout << "YES" << endl;
        }
    }
    return 0;
}