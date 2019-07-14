#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll n,t,score;
    string correct,chef;

    cin >> t;

    for(ll i=0; i<t; i++){
        cin >> n;

        score = 0;

        cin >> correct;
        cin >> chef;

        for(ll j=0; j<n; j++){
            if(chef[j] == correct[j]){
                score += 1;
            }
            else if(chef[j] == 'N'){
                continue;
            }
            else{
                j++;
            }
        }

        cout << score << endl;
    }
    return 0;
}