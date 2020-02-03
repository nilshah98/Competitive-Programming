// including libraries and namespace
#include<bits/stdc++.h>
using namespace std;

// setting up constants in caps
const int AMOUNT = 5;
const int FILL = 10;

// defining macros that can speed up typing
#define ll 		long long
#define pb 		push_back
#define foreach(v, c) 	for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define forall(i,a,b)   for(int i=a;i<b;i++)
#define mp		make_pair

void vector_ops(){
	// initialising 1D vector

	// empty vector =>
	vector<int> v1;
	// filling with constant values =>
	vector<int> v2(AMOUNT, FILL);
	// initialize like arrays =>
	vector<int> v3{ 1, 2, 3, 4};
	// initialising from another array/vector, pass the start and end pointer =>
	vector<int> v4(v2.begin(), v2.end());

	// NOTE - v2.end() points to the element AFTER the last element of the vector

	// Adding elements to 1D vector

	// adding ALWAYS at the end =>
	v1.push_back(5);
	// using macros =>
	v1.pb(10);
	// adding at arbitrary position => .insert(<iterator>, val)
	v1.insert(v1.begin()+1, 30);

	// Iterating over all values

	// using iterators, should be of the same type as one iterating over
	vector<int>::iterator ptr;
	for(ptr  = v1.begin(); ptr != v1.end(); ptr++){
		cout << *ptr << " ";
	}
	cout << "\n";
	// using macros =>
	foreach(a,v2){
		cout << *a << " ";
	}
	cout << "\n";
	
	// NOTE - can use `auto` keyword to not type vector<int>::iterator each time
	
	// Removing elements

	// remove by index
	v1.erase(v1.begin());
	// can also remove a range of elements
	v2.erase(v2.begin(), v2.begin()+2);
	// Iterating and printing
	foreach(a,v1){
		cout << *a << " ";
	}
	cout << "\n";
	foreach(a,v2){
		cout << *a << " ";
	}
	cout << "\n";
	
	// Searching for element
	
	// can use search to search for a subsequence, here using find for single element =>
	auto rem = find(v1.begin(), v1.end(), 10);
	v1.erase(rem);
	foreach(a,v1) cout << *a << " ";
	cout << "\n";
}

void set_ops(){
	// Sets delaration
	set<int>s;

	// Inserting elements in set
	forall(i,0,10) s.insert(i);

	// Traversing elements
	foreach(a,s) cout << *a << " ";
	cout << "\n";
	
	// Erasing a value from set
	// That exists =>
	auto three = s.erase(3);
	// That does not exist =>
	auto hun = s.erase(100);
	// Returns 1 if element present and removed, else returns 0 if element not there
	cout << three << " " << hun << "\n";

	// Finding an element
	
	// Don't use this, as it is O(N) and looks at every element
	// auto rloc =find(s.begin(), s.end(), 5);
	// cout << *rloc << "\n";
	
	// Use the normal set.find(...) which is O(logN)
	auto rloc = s.find(5);
	cout << distance(s.begin(), rloc) << "\n" ;
}

void map_ops(){
	// Initialising a map
	map<string,int>c;
	
	// Inserting elements in map
	c.insert(mp("a",0));
	c.insert(mp("b",1));

	// Iterating a map
	foreach(a,c) cout << a->first << ":" << a->second << "\n";	
	
	// Removing elements from map
	auto rem = c.find("b");
	c.erase(rem);

	// Updating elements from map
	c["a"] += 10;
	foreach(a,c) cout << a->first << ":" << a->second << "\n";
}

void vector2_ops(){
	// Initialising a 2D vector
	vector<vector<int>>matrix;

	// Inserting elements in 2D vector	
	forall(i,0,3) {
		matrix.pb({}); 
		forall(j,0,3) matrix[i].pb(j);
	}
	
	// Traversing 2D vector
	foreach(a,matrix){
		foreach(b,*a) cout << *b << " ";
		cout << "\n";
	}
}

int main(){
	vector_ops();
	set_ops();
	map_ops();
	vector2_ops();
	return 0;
}
