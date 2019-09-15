#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n, maxi, sum, temp;
    sum = 0;
    maxi = 0;
    vector<ll> vals;

    cin >> n;
    
    for(ll i=0; i<n; i++){
        cin >> temp;
        sum += temp;
        vals.push_back(temp);
    }

    maxi = *max_element(vals.begin(),vals.end());
    ll zero = 0;
    ll sum_accumulate = accumulate(vals.begin(),vals.end(),zero);

    cout << sum << endl;
    cout << sum_accumulate << endl;
    if(sum%2==1 || sum < 2*maxi){
        cout << "NO";
    }
    else{
        cout << "YES";
    }

    return 0;
}