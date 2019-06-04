#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    ll length;
    cin >> length;
    ll nums[length];
    ll min = 100001;
    ll max = 0;
    ll smin = 100002;
    ll smax = -1;
    
    for(ll i=0; i<length; i++){
        cin >> nums[i];

        if(nums[i] > max){
            smax = max;
            max = nums[i];
        }
        else if(nums[i] > smax){
            smax = nums[i];
        }

        if(nums[i] < min){
            smin = min;
            min = nums[i];
        }else if(nums[i] < smin){
            smin = nums[i];
        }
    }

    ll diff = ((max - smax) > (smin - min)) ? (max - smax) : (smin - min);
    cout << (max - min - diff);

    return(0);
}