#include<iostream>
#include<string>
using namespace std;

int main(){
    string a;
    cin>>a;
    
    string b;
    cin>>b;
    
    cout<<a.size()<<" ";
    cout<<b.size()<<endl;
    
    cout<<a+b<<endl;
    cout<<b[0]+a.substr(1)<<" ";
    cout<<a[0]+b.substr(1);

}