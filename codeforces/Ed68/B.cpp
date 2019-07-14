#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    ll q,n,m;
    string row;
    ll maxBlack;
    bool flag;
    ll ans;

    ll rowN,colN;

    ll maxRowBlack, maxColBlack;

    vector<ll> maxRow;
    vector<ll> maxCol;

    ll currBlack;

    vector<string> matrix;
    vector<string>::iterator it;


    cin >> q;

    for(ll i=0; i<q; i++){
        flag = false;
        maxBlack = 0;
        currBlack = 0;

        matrix.clear();
        maxRow.clear();

        cin >> n;
        cin >> m;

        for(ll j=0; j<n; j++){
            cin >>row;
            matrix.push_back(row);
        }

        // ROW CALC -
        for(ll k=0; k<matrix.size(); k++){
            row = matrix[k];
            currBlack = 0;

            for(ll j=0; j < row.size(); j++){
                if(row[j] == '*'){
                    currBlack += 1;
                }
            }

            if(currBlack > maxBlack){
                maxBlack = currBlack;
                maxRow.clear();
                maxRow = {k};
            }
            else if(currBlack == maxBlack){
                maxRow.push_back(k);
            
            }
        }
        maxRowBlack = maxBlack;

        // COL CALC -
        maxBlack = 0;
        for(ll j=0; j<m; j++){
            currBlack = 0;

            for(it = matrix.begin(); it != matrix.end(); it++){
                row = *it;
                if(row[j] == '*'){
                    currBlack += 1;
                }
            }

            if(currBlack > maxBlack){
                maxBlack = currBlack;
                maxCol.clear();
                maxCol = {j};
            }
            else if(currBlack == maxBlack){
                maxCol.push_back(j);
            }

        }
        maxColBlack = maxBlack;

        // FIN CALC-
        ans = (n - maxColBlack) + (m - maxRowBlack);
        ll zero = 0;
        for(ll j=0; j<maxRow.size(); j++){
            for(ll k=0; k<maxCol.size(); k++){

                rowN = maxRow[j];
                colN = maxCol[k];

                if(matrix[rowN][colN] == '.'){
                    cout << max(ans-1,zero) << endl;
                    flag = true;
                    break;
                }
            }

            if(flag){
                break;
            }
        }

        if(!flag){
            cout << max(ans,zero) << endl;
        }

    }


    return 0;
}