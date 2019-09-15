#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,i,k,temp;

    cin >> n;
    cin >> i;

    vector<ll> intensities;
    vector<ll> presum;

    presum.push_back(0);

    unordered_map<ll,ll> frequencyCounter;
    unordered_map<ll,ll>::iterator pointer;

    k = 1 << ((i*8)/n);

    for(ll i=0; i<n; i++){
        cin >> temp;
        intensities.push_back(temp);

        pointer = frequencyCounter.find(temp);
        if(pointer != frequencyCounter.end()){
            pointer->second += 1;
        }
        else{
            frequencyCounter.insert(make_pair(temp,1));
        }
    }

    for(pointer = frequencyCounter.begin(); pointer != frequencyCounter.end(); pointer++){
        presum.push_back(pointer->second + presum.back());
    }


    ll l,r,curr,maxCount,size;
    size = presum.size()-1;
    curr = 0;
    maxCount = 0;

    l = 1;
    r = min(k,size);

    // cout << l << " " << r << " " << size << endl;
    
    curr = presum[r] - presum[l-1];

    maxCount = curr;

    for(ll i=r+1; i<=size; i++){
        curr = presum[i];
        curr -= presum[(i-r+l-1)];

        if(curr > maxCount){
            maxCount = curr;
        }
    }

    cout << n-maxCount;

    return 0;
}