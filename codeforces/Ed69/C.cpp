#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,k,temp,sum;
    vector<ll> nums;
    vector<ll> diff;

    cin >> n;
    cin >> k;

    for(ll i=0; i<n; i++){
        cin >> temp;
        
        if(nums.size() >= 1 && nums.size() < n){
            diff.push_back(nums.back() - temp);
        }

        nums.push_back(temp);
    }

    sum = nums.back() - nums[0];
    sort(diff.begin(), diff.end());

    for(ll i=0; i < k-1; i++){
        sum += diff[i];
    }

    cout << sum << endl;
    
    return 0;
}

/*
Mistakes-
1. Didn't take into account single element subarrays

 */