#include<bits/stdc++.h>
using namespace std;

class Node
{
    public:
        int data;
        Node *next;
    
    public:
        Node(int data, Node *next){
            this->data = data;
            this->next = next;
        };
};

class SLL
{
    public:
        Node *HEAD = NULL;
    
    public:
        void push(int data){
            cout << "push called" << endl;
            
            Node *new_node = new Node(data,NULL);
            
            if(this->HEAD == NULL){
                cout << "alloting head" << endl;
                this->HEAD = new_node;
            }
            else{
                Node *curr = (this->HEAD);
                while((curr)->next != NULL){
                    // cout<< (*curr)->data << endl;
                    curr = (curr)->next;
                }
                cout << (curr)->data << endl;
                (curr)->next = new_node;
            }
        }

        void traverse(){
            Node *curr = this->HEAD;
            while(curr != NULL){
                cout << curr->data << "->";
                curr = curr->next;
            };
            cout << endl;
        }
};

int main(){
    SLL list;

    list.push(2);
    list.push(5);
    list.push(10);
    list.push(22);
    list.push(1);

    list.traverse();

    return 0;
}
