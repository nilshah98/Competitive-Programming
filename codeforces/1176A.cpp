#include<bits/stdc++.h>
#define ll long long
using namespace std;

vector<ll> getFactorCount(ll num){
    vector<ll> factorCount;
    
    if(num == 1){
        factorCount = {0,0,0};
        return factorCount;
    }

    ll count = 0;
    while(num%2 == 0){
        count += 1;
        num /= 2;
    }
    factorCount.push_back(count);

    count = 0;
    while(num%3 == 0){
        count += 1;
        num /= 3;
    }
    factorCount.push_back(count);

    count = 0;
    while(num%5 == 0){
        count += 1;
        num /= 5;
    }
    factorCount.push_back(count);

    if(num > 1)
    factorCount.push_back(-1);

    return factorCount;
}

int main(){
    ll q,num,ans;
    vector<ll> factorCount;
    cin >> q;

    for(ll i=0; i<q; i++){
        ans = 0;
        cin >> num;
        factorCount = getFactorCount(num);

        if(factorCount.back() == -1){
            cout << -1 << endl;
        }
        else{
            ans += factorCount[0];
            ans += 2*factorCount[1];
            ans += 3*factorCount[2];
            cout << ans << endl;
        }

    }

    return 0;
}