#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    string temp = "text";

    //iterating a string, always chars, even when you use iterators
    for(ll i=0; i<temp.size(); i++){

        if(temp[i] == 'a'){
            cout << "character !" << endl;
            
            // Getting ascii value of char 
            cout << "character ascii value- " << int(temp[i]) << endl;
        }

        // Converting to string =>
        string temp(1,temp[i]);
        if(temp == "a"){
            cout << "word !" << endl;
        }
    }

    //map declaration
    unordered_map<char,ll> counter;
    //pointer to the map declaration
    unordered_map<char,ll>::iterator point;

    //Iterators are very useful!
    //to find whether a key exists or not
    point = counter.find('k');

    //to erase a value
    counter.erase(point);

    //inserting
    counter.insert(make_pair('a',10));

    return 0;
}
