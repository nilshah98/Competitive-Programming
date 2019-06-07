#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t,val,ans=0, curr=1, ind=0, breakInd=0;
    // 2^32
    const ll limit = 4294967296;
    bool flag = true;
    vector<ll> cmdHist;
    string cmd;

    cin >> t;
    for(ll i=0; i<t; i++){
        cin >> cmd;
        if(cmd == "for"){
            cin >> val;
            if(flag){

                if(ind == breakInd){
                    if(limit%val){
                        if(limit/val >= curr){
                            curr *= val;
                            breakInd++;
                        }
                    }else{
                        if(limit/val > curr){
                            curr*=val;
                            breakInd++;
                        }
                    }
                }
            
                cmdHist.push_back(val);
                ind++;
            
            }
        }
        else if(cmd == "end"){
            if(flag){
                // alter the cmdHist
                if(ind == breakInd){
                    breakInd--;
                    curr /= cmdHist.back();
                }
                
                cmdHist.pop_back();
                ind--;
            }
        }
        else{
            if(flag){

                if((limit - curr) > ans && ind == breakInd){
                    ans += curr;
                }
                else{
                    flag = false;
                }
            }
        }
    }
    
    if(flag){
        cout << ans;
    }
    else{
        cout << "OVERFLOW!!!";
    }

    return 0;
}