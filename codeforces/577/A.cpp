#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,m;

    cin >> n;
    cin >> m;

    string ans;
    vector<string> answers;
    for(ll i=0; i<n; i++){
        cin >> ans;
        answers.push_back(ans);
    }

    ll temp;
    vector<ll> marks;
    for(ll i=0; i<m; i++){
        cin >> temp;
        marks.push_back(temp);
    }

    ll fin = 0;
    vector<ll> count;

    for(ll i=0; i<5; i++){
        count.push_back(0);
    }

    for(ll i=0; i<m; i++){

        for(ll j=0; j<5; j++){
            count[j] = 0;
        }
        
        for(ll j=0; j<n; j++){
            count[answers[j][i] - 'A'] ++;
        }

        fin += *max_element(count.begin(), count.end())*marks[i];
    }

    cout << fin;
    return 0;
}