#include<bits/stdc++.h>
#define ll long long 
using namespace std;

int main(){
    ll n,q,ans;
    cin >> n;

    string word,query;
    cin >> word;


    unordered_map<char,vector<ll>> wordCounter;
    unordered_map<char,vector<ll>>::iterator wordPoint;

    for(ll i=0; i<n; i++){
        wordPoint = wordCounter.find(word[i]);
        if(wordPoint == wordCounter.end()){
            wordCounter.insert(make_pair(word[i],vector<ll> {i}));
        }
        else{
            wordPoint->second.push_back(i);
        }
    }
    
    cin >> q;

    for(ll i=0; i<q; i++){

        cin >> query;
        ans = 0;
        
        unordered_map<char,ll> counter;
        unordered_map<char,ll>::iterator point;

        for(ll j=0; j<query.size(); j++){

            point = counter.find(query[j]);
            if(point != counter.end()){
                point->second += 1;
            }
            else{
                counter.insert(make_pair(query[j],1));
            }
        }

        for(point = counter.begin(); point != counter.end(); point++){
            if(wordCounter[point->first][point->second - 1] > ans){
                ans = wordCounter[point->first][point->second - 1];
            }
        }

        cout << ans + 1 << endl;
    }
    
    return 0;
}