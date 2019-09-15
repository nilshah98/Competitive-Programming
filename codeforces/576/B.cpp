#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll H,L;

    cin >> H;
    cin >> L;

    long double ans;

    ans = ((L*L) - (H*H))/(2.0*H);

    cout << setprecision(10) << ans;
    return 0;
}