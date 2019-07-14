#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t, n, m, temp, profit;
    
    cin >> t;

    for(ll i=0; i<t; i++){
        cin >> n;
        cin >> m;
        profit = 0;

        ll numDrink[m];
        ll customer[n][3];
        ll allot[n];
        unordered_set<ll> posDrink;

        for(ll j=0; j<m; j++){
            cin >> temp;
            numDrink[j] = temp;
            posDrink.insert(j);
        }

        for(ll j=0; j<n; j++){
            for(ll k=0; k<3; k++){
                cin >> temp;
                customer[j][k] = temp;
            }

            if(numDrink[customer[j][0] - 1] > 0){
                profit += customer[j][1];
                numDrink[customer[j][0] - 1] -= 1;

                if(numDrink[customer[j][0] - 1] == 0){
                    posDrink.erase(customer[j][0] - 1);
                }

                allot[j] = customer[j][0];
            }
            else{
                profit += customer[j][2];
                allot[j] = -1;
            }
        }

        for(ll j=0; j<n; j++){
            if(allot[j] == -1){
                allot[j] = *posDrink.begin()+1;
                numDrink[*posDrink.begin()] -= 1;
                
                if(numDrink[*posDrink.begin()] == 0){
                    posDrink.erase(*posDrink.begin());
                }
            }
        }

        cout << profit << endl;

        for(ll j=0; j<n; j++){
            cout << allot[j] <<" ";
        }

        cout << endl;

    }
    return 0;
}