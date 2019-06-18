#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,x,y;

    cin >> n;
    cin >> x;
    cin >> y;

    ll a[n];
    ll b[n];

    for(ll i=0; i<n; i++){
        cin >> a[i];
    }

    for(ll i=0; i<n; i++){
        cin >> b[i];
    }

    pair<ll,ll> diff[n];

    for(ll i=0; i<n; i++){
        diff[i] = make_pair(a[i]-b[i], i);
    }

    sort(diff,diff+n);

    ll ans = 0;

    ll left = 0;
    ll right = n-1;

    ll leftdiff, rightdiff;

    while(left <= right){
        leftdiff = abs(diff[left].first); // B first
        rightdiff = diff[right].first; // A first

        if(leftdiff > rightdiff){
            if(y > 0){
                y--;
                ans += b[diff[left].second];
                left ++;
            }
            else{
                x--;
                ans += a[diff[right].second];
                right--;
            }
        }
        else{
            if(x > 0){
                x--;
                ans += a[diff[right].second];
                right--;
            }
            else{
                y--;
                ans += b[diff[left].second];
                left ++;
            }
        }
    }

    cout << ans;
    
    return 0;
}