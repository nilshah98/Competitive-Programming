#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll getRow(ll pos, ll c){
    return pos/c;
}

ll getCol(ll pos, ll c){
    return pos%c;
}

int main(){
    ll r,c;
    char temp;
    cin >> r;
    cin >> c;
    ll counter = 0;

    unordered_set<ll> filled = {};

    for(ll i=0; i<r; i++){
        for(ll j=0; j<c; j++){
    
            cin >> temp;
            if(string(1,temp) == "*"){
                filled.insert(counter);
            }

            counter += 1;
        }
    }

    if(filled.size() > 0){
        vector<ll> possibleCenter = {};
        ll curr;
        
        unordered_set<ll>:: iterator itr;
        for(itr = filled.begin(); itr != filled.end(); itr++){
            curr = *itr;
            // cout << curr << endl;
            if( filled.find(curr-1) != filled.end() && curr%c > 0 &&
                filled.find(curr+1) != filled.end() && curr%c < (c-1) &&
                filled.find(curr-c) != filled.end() && curr >= c &&
                filled.find(curr+c) != filled.end() && curr < c*(r-1) )
                {
                    
                    possibleCenter.push_back(curr);
                }
        }

        if(possibleCenter.size() == 1){
            ll center = possibleCenter[0];
            ll cRow = getRow(center, c);
            ll cCol = getCol(center, c);
            ll count = 1;
            ll temp = 1;

            while( filled.find(center - (temp*c)) != filled.end() && getCol(center - (temp*c), c) == cCol){
                temp += 1;
                count += 1;
            }

            temp = 1;
            while( filled.find(center + (temp*c)) != filled.end() && getCol(center + (temp*c), c) == cCol){
                temp += 1;
                count += 1;
            }

            temp = 1;
            while( filled.find(center - (temp*1)) != filled.end() && getRow(center - (temp*1), c) == cRow){
                temp += 1;
                count += 1;
            }

            temp = 1;
            while( filled.find(center + (temp*1)) != filled.end() && getRow(center + (temp*1), c) == cRow){
                temp += 1;
                count += 1;
            }

            if(count == filled.size()){
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }

        }else{
            cout << "NO" << endl;
        }
    }
    else{
        cout << "NO" << endl;    
    }
    return 0;
}