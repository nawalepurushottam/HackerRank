#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;

    int i=0;
    int c=n-1;
    while(i<n){
        for(int k=0;k<c;k++){
            cout<<" ";
        }
        c--;
        for(int j=0;j<=i;j++){
            cout<<"#";
        }
        cout<<endl;
        i++;
        
    }
}