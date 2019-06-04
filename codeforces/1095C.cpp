#include<bits/stdc++.h>
#define ll long long
using namespace std;

ll getHighestSetBit(ll num){
    ll count = 0;

    while(num >>= 1){
        count++;
    }

    return count;
}

void printVectorLL(vector<ll> temp){
    for(vector<ll>::iterator it = temp.begin(); it < temp.end(); it++){
        cout << *it << " "; 
    }
    // cout << "\n";
    return;
}

void getSlices(ll num, ll numOfSlices){
    vector<ll> vals = {num};
    ll currSize;
    ll currElem;
    ll lastElem;


    while(true){
        // cout << "bef slices: " << numOfSlices << "\n";
        // printVectorLL(vals);

        lastElem = vals.back();
        currSize = 1 << getHighestSetBit(min(numOfSlices,lastElem));
        numOfSlices -= currSize;
        
        currElem = lastElem/currSize;
        vals.pop_back();

        for(ll i=0; i<currSize; i++){
            vals.push_back(currElem);
        }
        // cout << "after slices: " << numOfSlices << "\n";

        if(numOfSlices == 0){
            break;
        }

        numOfSlices++;
        sort(vals.begin(),vals.end());
    }

    printVectorLL(vals);

    return;

}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll num,lim;
    cin >> num;
    cin >> lim;

    bitset<30> binNum(num);

    // cout << binNum << "\n";

    ll minimum = binNum.count();
    ll maximum = num;

    if(lim > maximum || lim < minimum){
        cout  << "NO";
        return(0);
    }

    cout << "YES\n";

    ll diff = lim - minimum;
    // cout << "diff--> " << diff << "\n";
    vector<ll> vals;
    for(ll i=0; i<30; i++){
        if(binNum[i]){
            vals.push_back(1<<i);
        }
    }

    // printVectorLL(vals);
    // cout << "======================================\n";
    vector<ll>::iterator valsIterator = vals.begin();
    while(valsIterator != vals.end()){
        if(diff >= *valsIterator){
            for(ll i=0; i<*valsIterator; i++){
                cout << "1 ";
            }
            diff -= *valsIterator;
            diff++;
        }
        else if(diff == 0){
            cout << *valsIterator << " ";
        }
        else{
            diff++;
            getSlices(*valsIterator,diff);
            diff = 0;
        }

        ++valsIterator;
    }

    return(0);
}

/*
ERRORS =>
1. Can't define iterators at the top
2. vector.back() returns last element value
3. 
*/