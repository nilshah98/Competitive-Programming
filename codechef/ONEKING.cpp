#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t,n,start,end;

    cin >> t;

    for(ll i=0; i<t; i++){
        cin >> n;

        vector< pair< pair< ll, ll>, ll> > kingdoms;
        
        for(ll j=0; j<n; j++){
            cin >> start;
            cin >> end;
            
            kingdoms.push_back(make_pair(make_pair(start,end), j));
        }

        sort(kingdoms.begin(),kingdoms.end());

        unordered_set<ll> kingdomInd;
        unordered_set<ll> startInd [2001];
        unordered_set<ll> endInd[2001];

        for(auto it = kingdoms.begin(); it != kingdoms.end(); it++){
            startInd[it->first.first].insert(it->second);
            endInd[it->first.second].insert(it->second);
        }

        ll ans = 0;

        for(ll i=0; i<=2000; i++){
            if(startInd[i].size() > 0){
                for(auto it = startInd[i].begin(); it != startInd[i].end(); it++){
                    kingdomInd.insert(*it);
                }
            }

            if(endInd[i].size() > 0){
                for(auto it = endInd[i].begin(); it != endInd[i].end(); it++){
                    if(kingdomInd.find(*it) != kingdomInd.end()){
                        ans ++;
                        kingdomInd.clear();
                        break;
                    }
                }
            }
        }

        cout << ans << endl;

    }

    return 0;
}