#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){

    unordered_map<string, unordered_set<string> > graph ({
        {"A",unordered_set<string> ({"F","E","B"})},
        {"B",unordered_set<string> ({"G","A","C"})},
        {"C",unordered_set<string> ({"H","B","D"})},
        {"D",unordered_set<string> ({"I","C","E"})},
        {"E",unordered_set<string> ({"J","D","A"})},
        {"F",unordered_set<string> ({"A","H","I"})},
        {"G",unordered_set<string> ({"B","I","J"})},
        {"H",unordered_set<string> ({"C","J","F"})},
        {"I",unordered_set<string> ({"D","F","G"})},
        {"J",unordered_set<string> ({"E","G","H"})},
    });

    unordered_map<string, ll> vals ({
        {"A",0},
        {"B",1},
        {"C",2},
        {"D",3},
        {"E",4},
        {"F",5},
        {"G",6},
        {"H",7},
        {"G",8},
        {"I",9}
    });

    ll t,index;
    string query;
    string curr,prev;

    vector<ll> ans;
    bool flag = false;
    bool out = true;

    cin >> t;
    for(ll i=0; i<t; i++){
        cin >> query;

        ans = {};
        flag = false;
        out = true;
        index=0;

        curr = *query.begin();

        for(auto it = ++query.begin(); it != query.end(); ++it){
            prev = curr;
            curr = *it;

            if(!flag){
                index++;

                if(curr != prev){
                    if(graph[string(prev)].find(string(curr)) != graph[string(prev)].end()){
                        flag = true;
                        if(index%2 == 0){
                            out = false;
                        }
                    }
                    else{
                        prev = string(1,char(prev[0]+5));
                        curr = string(1,char(curr[0]+5));
                        flag = true;

                        if(index%2){
                            out = false;
                        }

                    }
                }
            }
            else{

                if(curr == prev){
                    curr = string(1, char(curr[0] + 5));
                }
                else{
                    if(prev > "E" && string(1,char(curr[0]+5)) != prev){
                        curr = string(1, char(curr[0] + 5));
                    }
                }

                if( graph[string(prev)].find(string(curr)) == graph[string(prev)].end()){
                    ans.push_back(-1);
                    break;
                }
                else{
                    ans.push_back(vals[string(prev)]);
                }
            }
        }

        if(query.size() > 1){

            if(ans.size() > 0 && ans.back() == -1){
                cout << -1;
            }

            else{
                if(flag){
                    ans.push_back(vals[string(curr)]);
                }
                else{
                    if(query.size()%2 == 1){
                        ans.push_back(vals[string(1, *query.begin())]);
                    }
                    else{
                        ans.push_back(vals[string(1, char(*query.begin() + 5))]);
                    }
                }

                if(out){
                    for(ll i=0; i<index; ++i){
                        if(i%2==0){
                            cout << vals[string(1,query[0])];
                        }
                        else{
                            cout << vals[string(1, char(char(query[0])+5))];
                        }
                    }
                }else{
                    for(ll i=0; i<index; ++i){
                        if(i%2){
                            cout << vals[string(1,query[0])];
                        }
                        else{
                            cout << vals[string(1, char(char(query[0])+5))];
                        }
                    }
                }

                for(auto it = ans.begin(); it != ans.end(); ++it){
                    cout << *it;
                }
            }
        }

        else{
            cout << vals[query];
        }

        cout << endl;
    }

    return 0;
}