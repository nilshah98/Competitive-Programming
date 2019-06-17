#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t,n,k,minDist,startIndex,temp;
    vector<ll> points;

    cin >> t;

    for(ll i=0; i<t; i++){
    
        startIndex = 0;
        minDist = pow(10,9);
        points = {};

        cin >> n;
        cin >> k;

        for(ll j=0; j<n; j++){
            cin >> temp;

            if(j>=k && k>0){
                if(temp - points[j-k] <= minDist){
                    minDist = temp - points[j-k];
                    startIndex = j-k;
                }
            }

            points.push_back(temp);
        }

        // calculate answer
        ll ans;
        
        if(k>0){
            ans = points[startIndex] + ((points[startIndex+k] - points[startIndex])/2);
        }
        else{
            ans = points[0];
        }


        cout << ans << endl;
    }

    return 0;
}