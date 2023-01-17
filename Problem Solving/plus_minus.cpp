#include<iostream>
#include<vector>
using namespace std;

int main(){
    int n;
    cin>>n;

    vector<int> a(n);
    for(auto &i:a){
        cin>>i;
    }

    int pos,neg,zero;
    pos=0;neg=0;zero=0;
    for(int i=0;i<n;i++){
        if(a[i]>0){
            pos+=1;
        }
        else if(a[i]<0){
            neg+=1;
        }
        else{
            zero+=1;
        }
    }

    cout<<float(pos)/float(n)<<endl;
    cout<<float(neg)/float(n)<<endl;
    cout<<float(zero)/float(n)<<endl;   
}