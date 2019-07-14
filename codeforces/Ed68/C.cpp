#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n;
    string s,t,p;

    ll sPointer, tPointer;

    unordered_map<char,ll> rem;
    unordered_map<char,ll>::iterator remPointer;

    bool done = false;

    cin >> n;

    for(ll i=0; i<n; i++){
        done = false;

        cin >> s;
        cin >> t;
        cin >> p;

        // STEP1 - Check relative order of chars in s and t;
        sPointer = 0;
        tPointer = 0;

        // STEP2 - adding and mapping remaining characters;
        rem.clear();

        while(sPointer < s.size()){
            while(tPointer < t.size()){

                if(sPointer < s.size() && s[sPointer] == t[tPointer]){
                    sPointer+=1;
                }

                else{
                    remPointer = rem.find(t[tPointer]);
                    if(remPointer != rem.end()){
                        remPointer->second += 1;
                    }
                    else{
                        rem.insert(make_pair(t[tPointer],1));
                    }
                }

                tPointer+=1;
            }

            if(sPointer < s.size()){
                cout << "NO" << endl;
                done = true;
                break;
            }
        }

        if(!done){
            for(ll j=0; j<p.size(); j++){
                remPointer = rem.find(p[j]);

                if(remPointer != rem.end()){
                    remPointer->second -= 1;

                    if(remPointer->second == 0){
                        rem.erase(remPointer);
                    }
                }
            }

            if(rem.size() == 0){
                cout << "YES" << endl;
            }
            else{
                cout << "NO" << endl;
            }
        }

    }

    return 0;
}