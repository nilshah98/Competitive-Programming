#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll t,n,num,ans,temp;
    ll zero,one,two;

    cin >> t;

    for(ll i=0; i<t; i++){
        cin >> n;
        zero = 0;
        one = 0;
        two = 0;
        ans = 0;

        for(ll j=0; j<n; j++){
            cin >> num;

            if(num%3 == 0){
                zero += 1;
            }
            else if(num%3==1){
                one += 1;
            }
            else{
                two += 1;
            }
        }

        ans += zero;
        temp = min(two,one);
        ans += temp;
        two -= temp;
        one -= temp;
        ans += one/3;
        ans += two/3;

        cout << ans << endl;
    }

    return 0;
}