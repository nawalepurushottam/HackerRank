#include<bits/stdc++.h>
using namespace std;

void insertionSort(int n, vector<int> arr){
    int to_be_sorted=*(arr.end()-1);
    int i;

    for(i=n;i>1;i--){
        if(to_be_sorted<arr[i-2]){
            arr[i-1]=arr[i-2];
            for(int j=0;j<n;j++){
                cout<<arr[j]<<" ";
            }
            cout<<endl;
        }
        else{
            break;
        }
    }
    arr[i-1]=to_be_sorted;
    for(int j=0;j<n;j++){
        cout<<arr[j]<<" ";
    }
    cout<<endl;
}


int main(){
    int n;
    cin>>n;

    vector<int> arr;

    for(int i=0;i<n;i++){
        int temp;
        cin>>temp;
        arr.push_back(temp);
    }

    insertionSort(n,arr);

}