#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,k,temp,count,curr,ans;
    vector<ll> vals;

    cin >> n;
    cin >> k;

    for(ll i=0; i<n; i++){
        cin >> temp;
        vals.push_back(temp);
    }

    sort(vals.begin(), vals.end());

    ans = -1;
    count = 0;
    curr = 0;
    
    // Calculate cost for leveling the field 
    for(ll i = n/2; i<n-1; i++){
        count++;
        curr += (vals[i+1]-vals[i])*count;

        // If overflown
        if(curr > k){
            ans = vals[i];

            // get the earlier remaining cost
            curr -= (vals[i+1]-vals[i])*count;
            // distribute them among the remaining elements
            ans += (k-curr)/((i+1) - (n/2));
            break;
        }
    }

    // If still k remains, distribute it
    if(ans == -1){
        cout << vals.back() + (k-curr)/((n/2)+1); 
    }
    else{
        cout << ans;
    }

    return 0;
}