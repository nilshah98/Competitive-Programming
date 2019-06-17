#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll getGCD(ll a, ll b){
    if(a%b == 0){
        return b;
    }else{
        getGCD(b,a%b);
    }
}

int main(){
    ll t,n,temp;

    cin >> t;

    for(ll i=0; i<t; i++){
        cin >> n;
        set<ll> nums = {};

        for(ll j=0; j<n; j++){
            cin >> temp;
            nums.insert(temp);
        }

        vector<ll> prefix = {};
        vector<ll> suffix = {};

        prefix.push_back(*nums.begin());
        suffix.push_back(*nums.rbegin());

        for(set<ll>::iterator it=++nums.begin(); it != nums.end(); it++){
            temp = getGCD(prefix.back(), *it);
            prefix.push_back(temp);
        }

        for(set<ll>::reverse_iterator it = ++nums.rbegin() ; it != nums.rend(); it++){
            temp = getGCD(suffix.back(), *it);
            suffix.push_back(temp);
        }

        ll ans = 1;
        ll index = 0;

        n = nums.size();

        if(n == 1){
            ans = *nums.begin() * 2;
        }
        else{
            for(set<ll>::iterator it = nums.begin(); it != nums.end(); it++){
                if(index == 0){
                    ans = max(suffix[n-2] + *it, ans);
                }
                else if(index == n-1){
                    ans = max(prefix[n-2] + *it, ans);
                }
                else{
                    ans = max(getGCD(prefix[index-1], suffix[n-1-index-1]) + *it, ans);
                
                }

                index++;
            }
        }

        cout << ans << endl;
    }

    return 0;
}