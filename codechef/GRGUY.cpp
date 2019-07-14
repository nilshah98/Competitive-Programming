#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll traverse(vector<int> lane1,vector<int> lane2){
    ll ans = 0;
    if(lane1[0] == 1){
        return 1000000000;
    }
    else{
        bool lane = true;

        for(ll i=0; i<lane1.size(); i++){
            // cout << lane1[i];
            if(lane){
                if(lane1[i] == 1){
                    if(lane2[i] == 0){
                        ans += 1;
                        lane = false;
                    }
                    else{
                        return 1000000000;
                    }
                }
            }
            else{
                if(lane2[i] == 1){
                    if(lane1[i] == 0){
                        ans += 1;
                        lane = true;
                    }
                    else{
                        return 1000000000;
                    }
                }
            }
        }
        return ans;
    }
}

int main(){
    ll t;
    string lane;
    vector<int> lane1;
    vector<int> lane2;

    cin >> t;

    for(ll i=0; i<t; i++){
        lane1 = {};
        lane2 = {};
        cin >> lane;
        
        for(auto it=lane.begin(); it != lane.end(); ++it){
            if(*it == '.'){
                lane1.push_back(0);
            }
            else{
                lane1.push_back(1);
            }
        }

        cin >> lane;

        for(auto it=lane.begin(); it != lane.end(); ++it){
            if(*it == '.'){
                lane2.push_back(0);
            }
            else{
                lane2.push_back(1);
            }
        }
        // cout << endl;

        ll ans = min(traverse(lane1,lane2), traverse(lane2,lane1));
        if(ans < 1000000000){
            cout << "Yes" << endl << ans << endl;
        } 
        else{
            cout << "No" << endl;
        }
    }
    return 0;
}