#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
	ll n, count;
	bool flag = false;
	string word;

	unordered_set<char> vowels = {'a','e','i','o','u'};
	
	unordered_map< ll, vector<string> > tally;
	unordered_map< ll, vector<string> > tallyLast;


	cin >> n;

	for(ll i=0; i<n; i++){
		count = 0;
		flag = false;

		cin >> word;
	
		for(char& c : word){
			if(vowels.find(c) != vowels.end()){
				count += 1;
			}
		}

		if(vowels.find(word.back()) != vowels.end()){
			flag = true;
		}

		if(flag){
			if(tallyLast.find(count) != tallyLast.end()){
				tallyLast[count].push_back(word);
			}
			else{
				tallyLast[count] = {word};
			}
		}
		else{
			if(tally.find(count) != tally.end()){
				tally[count].push_back(word);
			}
			else{
				tally[count] = {word};
			}
		}

		for(auto a : tally){

			while(a.second.size() > 1){

				string a1 = a.second.back();
				a.second.pop_back();

				string a2 = a.second.back();
				a.second.pop_back();

				for(auto b : tallyLast){

					if(b.second.size() > 1){

						string b1 = b.second.back();
						b.second.pop_back();

						string b2 = b.second.back();
						b.second.pop_back();

						cout << a1 << " " << b1 << endl;
						cout << a2 << " " << b2 << endl;

						break;
					}

				}
			}
		}

	}
	return 0;
}

// Need to use both queues effectively