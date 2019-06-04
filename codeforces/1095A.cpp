#include<bits/stdc++.h>
using namespace std;

int main(){
    int length;
    cin >> length;
    string encrypted;
    cin >> encrypted;

    string decrypted = "";
    int curr = 0;
    int diff = 0;

    for(curr = 0; curr < length; curr += diff){
        decrypted.push_back(encrypted[curr]);
        diff += 1;
    }

    cout << decrypted;

    return(0);
}