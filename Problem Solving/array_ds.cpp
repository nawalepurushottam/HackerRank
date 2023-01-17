#include<iostream>
using namespace std;

void reverseArray(int arr[],int n){
    int array[n];
    
    for(int i=0;i<n;i++){
        int temp=arr[i];
        array[i]=arr[n-i-1];
        arr[n-i-1]=temp;
    }
    for(int i=0;i<n;i++){
        cout<<array[i]<<" ";
    }
}

int main(){
    int n;
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    reverseArray(arr,n);
}