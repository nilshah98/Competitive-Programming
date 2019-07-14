#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    // Alice moves first
    // Who CANNOT make a move, loses the game
    // 1,2,k only 3 moves possible

    ll q,n,k;
    ll loc;
    ll div;
    cin >> q;

    for(ll i=0; i<q; i++){
        cin >> n;
        cin >> k;

        // First case
        if(k%3){
            if(n%3){
                cout << "Alice" << endl;
            }
            else{
                cout << "Bob" << endl;
            }
        }
        // Second case
        else{
            div = k/3;
            loc = n % ((div-1)*3 + 4);

            if(loc%3 || loc == ((div-1)*3 + 3)){
                cout << "Alice" << endl;
            }
            else{
                cout << "Bob" << endl;
            }
        }
    }
    return 0;
}