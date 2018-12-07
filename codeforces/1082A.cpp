#include<bits/stdc++.h>
using namespace std;

void main(){
    long long t,i,n,x,y,d;
    vector<long long> startend;

    cin >> t;
    for(i=0; i<t; i++){
        cin >> n;
        cin >> x;
        cin >> y;
        cin >> d;

        if(abs(x-y)%d == 0){
            cout << abs(x-y)/d;
        }
        else{
            if(abs(y-1)%d == 0){
                startend.push_back(abs(x-1)/d + abs(y-1)/d + 1);
            }
            else if(abs(y-n)%d == 0){
                startend.push_back(abs(n-x)/d + abs(n-d)/d + 1);
            }
            else{
                startend.push_back(-1);
            }

            cout << min_element(startend.begin(), startend.end());
        }
    }
}
